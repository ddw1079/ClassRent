from django.contrib import admin
from .models import Post, Comment, Room, Building, Floor

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Room)
