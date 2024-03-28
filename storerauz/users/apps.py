from __future__ import unicode_literals
 
from django.apps import AppConfig

 
 
class ProfilesConfig(AppConfig):
    name = 'users'
 
    def ready(self):
        import users.signals