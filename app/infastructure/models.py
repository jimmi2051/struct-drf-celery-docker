# Third Party
from django.db import models
from django.utils.timezone import now

# Create your models here.


class AuditMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Created At', editable=False, default=now, db_index=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated At', editable=False, default=now, db_index=True
    )

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        dt = now()
        if not self.pk or not self.created_at:
            self.created_at = dt
        self.updated_at = dt
        super(AuditMixin, self).save(force_insert, force_update, using, update_fields)

    def clone_instance(self):
        new_instance = self.__class__()
        for field in self._meta.fields:
            setattr(new_instance, field.name, getattr(self, field.name))
        return new_instance

    class Meta:
        abstract = True
