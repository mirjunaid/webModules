from django.apps import AppConfig


class SitemodeulesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'siteModeules'

    def ready(self):
        import siteModeules.signals
