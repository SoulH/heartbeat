from django.contrib.admin import ModelAdmin, register

from heartbeat.models import HeartbeatRequestLog


@register(HeartbeatRequestLog)
class HeartbeatRequestLogAdmin(ModelAdmin):
    list_display = ["url", "timestamp", "status", "elapsed", "error", "reason"]
    search_fields = ["url", "error", "reason"]
    list_filter = ["status", "error"]
