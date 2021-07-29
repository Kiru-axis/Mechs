from django.apps import AppConfig


class OkoaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'okoa'

    def ready(self):
        import okoa.signals
