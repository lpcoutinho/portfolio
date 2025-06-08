from django.contrib import admin
from .models import AnalyticsEvent, VisitorSession, PageView

@admin.register(AnalyticsEvent)
class AnalyticsEventAdmin(admin.ModelAdmin):
    list_display = ['event_type', 'timestamp', 'ip_address', 'page_url', 'session_id']
    list_filter = ['event_type', 'timestamp']
    search_fields = ['ip_address', 'page_url', 'session_id']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'

@admin.register(VisitorSession)
class VisitorSessionAdmin(admin.ModelAdmin):
    list_display = ['session_id_short', 'ip_address', 'first_seen', 'last_seen', 'page_views', 'total_time_seconds', 'country']
    list_filter = ['first_seen', 'country']
    search_fields = ['session_id', 'ip_address', 'city']
    readonly_fields = ['session_id', 'first_seen', 'last_seen']
    
    def session_id_short(self, obj):
        return obj.session_id[:8] if obj.session_id else ''
    session_id_short.short_description = 'Session ID'

@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ['page_url', 'timestamp', 'session_short', 'time_on_page', 'scroll_depth']
    list_filter = ['timestamp', 'page_url']
    search_fields = ['page_url', 'page_title', 'session__session_id']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'
    
    def session_short(self, obj):
        return obj.session.session_id[:8] if obj.session else ''
    session_short.short_description = 'Session'
