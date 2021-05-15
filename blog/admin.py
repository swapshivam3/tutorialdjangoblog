from django.contrib import admin

# Register your models here.

from .models import Post, Comment, Upload_XL

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Upload_XL)