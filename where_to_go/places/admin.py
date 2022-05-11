
from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('img_preview',)
    fields = ('img', 'img_preview')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


# Register your models here.
admin.site.register(Image)
