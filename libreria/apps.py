from django.apps import AppConfig


class LibreriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'libreria'
    verbose_name = 'Gestión de usuarios'


    def ready(self):
        import libreria.signals
