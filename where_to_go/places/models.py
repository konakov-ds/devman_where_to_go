from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Локация')
    description_short = models.TextField(blank=True, verbose_name='Короткое описание')
    description_long = HTMLField(blank=True, verbose_name='Полное описание')
    lng = models.FloatField(blank=True, verbose_name='Долгота')
    lat = models.FloatField(blank=True, verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    img_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200, verbose_name='Название')
    img = models.ImageField(verbose_name='Изображение')
    place = models.ForeignKey(
        Place,
        related_name='images',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Локация'
    )

    def img_preview(self):
        return format_html(
            '<img src="{url}" style="max-height:200px"/>',
            url=self.img.url,
        )

    class Meta:
        ordering = ['img_id']

    def __str__(self):
        return f'{self.img_id} {self.place}'
