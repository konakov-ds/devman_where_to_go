from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = HTMLField(blank=True)
    lng = models.FloatField(blank=True)
    lat = models.FloatField(blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    img_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    img = models.ImageField()
    place = models.ForeignKey(
        Place,
        related_name='images',
        on_delete=models.CASCADE
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
