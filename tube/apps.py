from django.apps import AppConfig


class TubeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tube'
    def ready(self):
        import tube.postHistory  