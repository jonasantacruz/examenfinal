from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

class Libro(models.Model):
    isbn = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999999)])
    #author = models.ForeignKey('auth.User')
    author = models.CharField(max_length=40)
    title = models.CharField(max_length=200)
    editorial = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    anio = models.IntegerField()
#imagen de libro Portada
    #portada = models.ImageField(upload_to=upload_location,
    #        null=True, blank=True,
    #        width_field='width_field',
    #        height_field='height_field')

    #text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
