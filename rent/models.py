from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import authenticate, login
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


def publish(self):
    self.published_date = timezone.now()
    self.save()


class Comment(models.Model):
    post = models.ForeignKey('rent.post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Room(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)


class History(models.Model):
    address = models.ForeignKey(Room, on_delete=models.CASCADE)
    stime = models.DateTimeField()
    etime = models.DateTimeField()



