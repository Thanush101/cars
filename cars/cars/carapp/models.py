from django.db import models
from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cars/')
    details = models.TextField()

    def __str__(self):
        return self.title

