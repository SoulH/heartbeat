from heartbeat.models import HeartbeatRequestLog


class HeartbeatService:
    model = HeartbeatRequestLog

    @classmethod
    def log(cls, data: dict):
        fields = [x.name for x in cls.model._meta.fields]
        kwargs = {k: v for k, v in data.items() if k in fields}
        cls.model(**kwargs).save()
