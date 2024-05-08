from django.apps import AppConfig # type: ignore


class IceCreamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ice_cream'
    verbose_name = 'Каталог мороженого'