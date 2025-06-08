from django.conf import settings

def analytics(request):
    """
    Context processor para disponibilizar configurações de analytics nos templates.
    """
    return {
        'GOOGLE_ANALYTICS_GTAG_PROPERTY_ID': getattr(settings, 'GOOGLE_ANALYTICS_GTAG_PROPERTY_ID', ''),
    }