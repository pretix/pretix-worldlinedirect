from pretix_worldlinedirect.urls import get_event_patterns, get_urlpatterns

event_patterns = get_event_patterns("payonedirect")
urlpatterns = get_urlpatterns("payonedirect")
