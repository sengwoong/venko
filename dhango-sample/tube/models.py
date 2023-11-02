from django.db import models
from django.conf import settings

class Post(models.Model):

    post_contents = models.ManyToManyField('PostContent', related_name='posts', blank=True)


    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_written')
    read_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_read')
    title = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    category = models.CharField(max_length=50, db_index=True, default='bug', null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/tube/{self.pk}/'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postcontents', db_index=True)
    order = models.IntegerField()
    file_upload = models.FileField(upload_to='tube/files/%Y/%m/%d/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)


class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posttags', db_index=True)
    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
