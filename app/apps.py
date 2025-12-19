from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    verbose_name = "Техносервис"

    def ready(self):
        from django.contrib.admin.sites import site
