from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


# Register your models here.
admin.site.register(Image)
