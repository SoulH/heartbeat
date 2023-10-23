from django.db.models import CharField, DateTimeField, PositiveIntegerField, TimeField
from django.utils.timezone import now


class ResponseInfo:
    url = CharField(max_length=200)
    timestamp = DateTimeField(default=now)
    status: PositiveIntegerField(default=200)
    elapsed: TimeField()
    error = CharField(max_length=100, null=True, blank=True)
    reason = CharField(max_length=100, null=True, blank=True)
