from django.db.models import CharField, DateTimeField, PositiveIntegerField, Model, FloatField
from django.utils.timezone import now


class HeartbeatRequestLog(Model):
    url = CharField(max_length=200)
    timestamp = DateTimeField(default=now)
    status = PositiveIntegerField(default=200)
    elapsed = FloatField()
    error = CharField(max_length=100, null=True, blank=True)
    reason = CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "heartbeat_request_log"
        verbose_name = "Request Log"
        verbose_name_plural = "Request Log"
