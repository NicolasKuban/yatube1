from django.contrib import admin
from .models import CD


class CDAdmin(admin.ModelAdmin):
    ## В админ-зоне должны быть видны такие поля:
    ##    название альбома
    ##    дата релиза
    ##    артист
    ##    жанр
    list_display = ("title", "date", "artist", "genre")

    ##    Должна быть фильтрация записей по полям:
    ##        дата релиза
    ##        жанр
    list_filter = ("date", "genre")

    ## Пустые поля в записях должны заполняться строкой -пусто-
    empty_value_diplay = "-пусто-"

##  при регистрации модели Post источником конфигурации для неё
## назначаем класс CDAdmin
admin.site.register(CD, CDAdmin)
