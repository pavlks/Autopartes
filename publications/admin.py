from django.contrib import admin

from .models import Publication, Comment, Image

admin.site.register(Publication)
admin.site.register(Comment)