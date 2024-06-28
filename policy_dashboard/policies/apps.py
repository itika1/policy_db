# policies/apps.py

from django.apps import AppConfig

class PoliciesConfig(AppConfig):
    """
    Configuration class for the policies application.

    Attributes:
        default_auto_field (str): Specifies the type of auto field to use for the primary key.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'policies'

    def ready(self):
        """
        Method called when the Django application is ready.

        This method is used to import and register the signal handlers for the policies application.
        """
        import policies.signals  # This will register the signal
