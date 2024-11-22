from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sales"

    def ready(self):
        import sales.signals  # Import signals to register the signal handler

    def ready(self):
        import sales.models  # This imports the signals    
