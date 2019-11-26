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
    post = models.ForeignKey('rent.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


def approved_comments(self):
    return self.comments.filter(approved_comment=True)


class Time(models.Model):
    time = models.CharField(max_length=100, primary_key=True)  # 시간. 몇교시인지 적기
    # 요일(예약되어있는지 boolean)
    sun = models.BooleanField(default=False)
    mon = models.BooleanField(default=False)
    tue = models.BooleanField(default=False)
    wed = models.BooleanField(default=False)
    thu = models.BooleanField(default=False)
    fri = models.BooleanField(default=False)
    sat = models.BooleanField(default=False)


class Building(models.Model):
    building = models.CharField(max_length=100)


class Floor(models.Model):
    floor = models.CharField(max_length=100)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)


class Room(models.Model):
    room_name = models.CharField(max_length=100)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)


#
#
# class History(models.Model):
#     address = models.ForeignKey(Room, on_delete=models.CASCADE)
#     stime = models.DateTimeField()
#     etime = models.DateTimeField()



