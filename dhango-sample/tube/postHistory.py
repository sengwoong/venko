import json
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Post, PostHistory

@receiver(pre_delete, sender=Post)
def pre_delete_post(sender, instance, **kwargs):
    print("postsender")

    post_contents = []
    for content in instance.postcontents.all():
        content_description = f"{content.order}: {content.content}"
        if content.file_upload:
            content_description += f", {content.file_upload}"
        post_contents.append(content_description)
    print(post_contents)

    commentAllid = {}
    for comment in instance.comments.all():
        commentAllid[comment.id] = {
            "Front": comment.front_idx,
            "Back": comment.back_idx,
            "Context": comment.message,
            "Author": comment.author.username
            
        }

    print("commentFrontid")
    print(commentAllid)

    tags = ", ".join([tag.tag_name for tag in instance.tags.all()])

    post_history = PostHistory.objects.create(
        post_contents=json.dumps(post_contents),
        category=instance.category,
        title=instance.title,
        author=instance.author,
        view_count=instance.view_count,
        tags=tags,
        post_comments=json.dumps(commentAllid)
    )
