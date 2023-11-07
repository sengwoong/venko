from django.contrib import admin
from .models import PostHistory,Post, Comment, Tag

admin.site.register(Post)
admin.site.register(PostHistory)
admin.site.register(Comment)
admin.site.register(Tag)