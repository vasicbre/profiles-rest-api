from django.contrib import admin
from profiles_api import models

#https://www.youtube.com/watch?v=UmljXZIypDc - Django tutorial
admin.site.register(models.UserProfile)