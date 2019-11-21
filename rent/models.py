from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Room(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)


class User(models.Model):
    userid = models.CharField(max_length=20)
    userpw = models.CharField(max_length=40)


class History(models.Model):
    address = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE)
    stime = models.DateTimeField()
    etime = models.DateTimeField()



