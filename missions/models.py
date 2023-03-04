from django.db import models

# Create your models here.


class Photos(models.Model):
    display = models.ImageField(null=True, blank=True)


class Message(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name