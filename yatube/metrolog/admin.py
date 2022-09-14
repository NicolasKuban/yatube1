from django.contrib import admin
from .models import Mesuarements

# Register your models here.

class MesuarementsAdmin(admin.ModelAdmin):
    list_display = (
        "device_type",
        "device_name",
        "device_number",
        "device_date_manufacture",
        "type_measurements"
    )

    list_filter = (
        "device_name",
        "device_number",
    )

## Пустые поля в записях должны заполняться строкой -пусто-
    empty_value_diplay = "-пусто-"

##  при регистрации модели Post источником конфигурации для неё
## назначаем класс CDAdmin
admin.site.register(Mesuarements, MesuarementsAdmin)
