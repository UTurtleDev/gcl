# config/context_processors.py
from django.conf import settings

def cabinet_info(request):
    """
    Rend les informations du cabinet disponibles dans tous les templates.
    """
    return {
        'CABINET_NAME': settings.CABINET_NAME,
        'CABINET_ADDRESS': settings.CABINET_ADDRESS,
        'CABINET_EMAIL': settings.CABINET_EMAIL,
        'CABINET_PHONE': settings.CABINET_PHONE,
    }