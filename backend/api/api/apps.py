"""Application configuration
"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configuration for the API application.

    Args:
        AppConfig (apps.AppConfig): base class for configuration classes
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
