from tube.models import Post, Comment, Tag

Post.objects.all().delete()
Comment.objects.all().delete()
Tag.objects.all().delete()
