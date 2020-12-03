from django.db import models
from django.utils.timezone import localtime, now


class AuditMixin(models.Model):
    created_on = models.DateTimeField(verbose_name='Created At',
                                      editable=False,
                                      default=localtime(now()),
                                      db_index=True)
    updated_on = models.DateTimeField(verbose_name='Updated At',
                                      editable=False,
                                      default=localtime(now()),
                                      db_index=True)

    def save(self,
             force_insert=False,
             force_update=False,
             using=None,
             update_fields=None):
        dt = localtime(now())
        if not self.pk or not self.created_on:
            self.created_on = dt
        self.updated_on = dt
        super(AuditMixin, self).save(force_insert, force_update, using,
                                     update_fields)

    class Meta:
        abstract = True
