
from django.contrib import admin
# из файла models импортируем модель Post
from .models import Events
admin.site.register(Events)
