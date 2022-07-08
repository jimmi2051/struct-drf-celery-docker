# Standard Library
import json
from datetime import timedelta

# Third Party
from appcenter.configs.constants import INVALID_FORMAT
from appcenter.configs.constants import INVALID_KEY
from appcenter.configs.constants import TYPE_ATTRIBUTE
from appcenter.configs.constants import TYPE_PROPERTY
from appcenter.configs.constants import logger_console
from django.db.models import Q
from django.utils.dateparse import parse_datetime
from django.utils.timezone import localtime
from django.utils.timezone import now
from infastructure.helpers import convert_str_datetime
from rest_framework.exceptions import ValidationError

logger = logger_console


def process_filter_and_search(
    request, allow_fields_sort, allow_fields_filter, allow_fields_search, query_set
):
    '''
    Format:
    1. Sort: sortBy=<key1:string>:<value1:string>,<key2:string>:<value2:string>
    2. Filter: filterBy=<key1:string>:<value1:string>,<key2:string>:<value2:string>
    '''
    sort_query_params = request.query_params.get('sortBy', None)
    filter_params = request.query_params.get("filterBy", None)
    key_search = request.query_params.get("keySearch", None)
    from_str = request.query_params.get("from", None)
    to_str = request.query_params.get("to", None)
    if filter_params:
        filter_parsed_attribute = {}
        filter_parsed_property = {}
        fields = filter_params.split(",")
        for field in fields:
            field_convert = field.split(":")
            if len(field_convert) != 2:
                raise ValidationError(INVALID_FORMAT)
            key = field_convert[0]
            value = field_convert[1]
            try:
                type_filter = TYPE_ATTRIBUTE
                model_field = allow_fields_filter[key]
                if "__property" in model_field:
                    type_filter = TYPE_PROPERTY
                    model_field = model_field.replace("__property", "")

            except KeyError:
                raise ValidationError(INVALID_KEY)
            try:
                value = json.loads(value)
            except ValueError:
                pass
            if type_filter == TYPE_ATTRIBUTE:
                values = str(value).split("|")
                filter_parsed_attribute[f'{model_field}__in'] = values
            if type_filter == TYPE_PROPERTY:
                filter_parsed_property[model_field] = value

        query_set = query_set.filter(**filter_parsed_attribute)
        if filter_parsed_property:
            temp = query_set.all()
            ids = []
            for attr, value in filter_parsed_property.items():
                values = str(value).split("|")
                ids += [x.id for x in temp if getattr(x, attr) in values]
            query_set = query_set.filter(id__in=ids)

    if key_search:
        key_search = key_search.strip()
        key_search_parsed = [Q(**{field: key_search}) for field in allow_fields_search]
        query = Q()
        for key in key_search_parsed:
            query |= key
        query_set = query_set.filter(query)

    if sort_query_params:
        sort_parsed = []
        fields = sort_query_params.split(",")
        for field in fields:
            try:
                model_field = allow_fields_sort[field]
            except KeyError:
                raise ValidationError(INVALID_KEY)
            sort_parsed.append(model_field)

        query_set = query_set.order_by(*sort_parsed)

    today = localtime(now())
    nextday = localtime(today - timedelta(days=1)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )

    if from_str:
        from_str = convert_str_datetime(from_str)
        from_date = parse_datetime(from_str)
        if not from_date:
            from_date = today.replace(hour=0, minute=0, second=0, microsecond=0)
        query_set = query_set.filter(created_at__gte=from_date)

    if to_str:
        to_str = convert_str_datetime(to_str)
        to_date = parse_datetime(to_str)
        if not to_date:
            to_date = nextday
        query_set = query_set.filter(created_at__lte=to_date)

    return query_set
