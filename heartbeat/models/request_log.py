from django.db.models import CharField, DateTimeField, PositiveIntegerField, TimeField, Model
from django.utils.timezone import now


class HeartbeatRequestLog(Model):
    url = CharField(max_length=200)
    timestamp = DateTimeField(default=now)
    status = PositiveIntegerField(default=200)
    elapsed = PositiveIntegerField()
    error = CharField(max_length=100, null=True, blank=True)
    reason = CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "heartbeat_request_log"
