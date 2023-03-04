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


class Sermon(models.Model):
    topic = models.CharField(max_length=80)
    sermon = models.FileField()
    location = models.CharField(max_length=100)
    speaker = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.topic} - {self.location}"


class Testimony(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    tel = models.CharField(max_length=12)
    testimony = models.TextField()


class Event(models.Model):
    title = models.CharField(max_length=30)
    venue = models.CharField(max_length=200)
    flier = models.ImageField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title