from django.contrib.gis.db import models


# Create your models here.

class Incidences(models.Model):
    name = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=210)
    punto = models.PointField()
    object = models.GeoManager()

    def __str__(self):
        return self.name
