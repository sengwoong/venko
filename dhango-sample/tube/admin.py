from django.contrib import admin
from .models import ClearPost,Post, Comment, Tag

admin.site.register(Post)
admin.site.register(ClearPost)
admin.site.register(Comment)
admin.site.register(Tag)