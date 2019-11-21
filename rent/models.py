from django.db import models

# Create your models here.


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



