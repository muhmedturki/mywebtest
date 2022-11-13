from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig
class BlogAdminConfig(AdminConfig):
   default_site='pages.admin.BlogAdminArea'

class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

class BlogConfig(AppConfig):
    name: str= 'blog'
