from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField(blank=True)
    lng = models.FloatField(blank=True)
    lat = models.FloatField(blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    img_id = models.IntegerField(default=1)
    name = models.CharField(max_length=200)
    img = models.ImageField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.img_id} {self.place}'
