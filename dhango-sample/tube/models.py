from django.db import models
from django.conf import settings



class Post(models.Model):

    post_contents = models.ManyToManyField('PostContent', related_name='posts', blank=True)


    tags = models.ManyToManyField('Tag', blank=True, related_name='tags' , db_index=True)

    title = models.CharField(max_length=100, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.CharField(max_length=50, default='bug', null=False)
    #작성자
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_written')
    #너꼭읽어
    read_author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                    on_delete=models.CASCADE, related_name='posts_read')
    

    view_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/tube/{self.pk}/'
    class Meta:
        abstract = False  # change from True to False


# 인데싱 걸기가 힘들고 튜닝이 어렵다 이유는 자주 변경 되는 로직이라서 
# 원래는 nosql 로 넣고 푸쉬를하고 애는 쓰기전용으로 해서 만일 값이 없을떄
# 다시 몽고디비에 넣어야하는데 하드 코드로 돌아가다가 일정이상 유저가모이면 캐싱처리 할거다.
#단 인설트하면 해당 레디스는 지워야한다.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    finecheck = models.TextField(db_index=True, default="BUG")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   


    def __str__(self):
        return self.message
# 인데싱 걸기가 힘들고 튜닝이 어렵다 이유는 자주 변경 되는 로직이라서 
# 원래는 nosql 로 넣고 푸쉬를하고 애는 쓰기전용으로 해서 만일 값이 없을떄
# 다시 몽고디비에 넣어야하는데 하드 코드로 돌아가다가 일정이상 유저가모이면 캐싱처리 할거다.
#단 인설트하면 해당 레디스는 지워야한다.

class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postcontents', db_index=True)
    order = models.IntegerField()
    file_upload = models.FileField(upload_to='tube/files/%Y/%m/%d/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    
    

# 인데싱 걸기가 힘들고 튜닝이 어렵다 이유는 자주 변경 되는 로직이라서 
# 원래는 nosql 로 넣고 푸쉬를하고 애는 쓰기전용으로 해서 만일 값이 없을떄
# 다시 몽고디비에 넣어야하는데 하드 코드로 돌아가다가 일정이상 유저가모이면 캐싱처리 할거다.
#단 인설트하면 해당 레디스는 지워야한다.
class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posttags', db_index=True)
    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


# 끝난거는 인데싱이 필요없어서 겹처도넣는다
# 이떄 카테고리랑 태그를 풀어서 넣는데 이는 인설트가 없다고 판단하기 때문이다.



class ClearPost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_contents = models.TextField()
    category = models.CharField(max_length=50, default='bug', null=False)
    tags = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=100, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clear_posts_written')
    read_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clear_posts_read')
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_custom_tags_list(self):
        if self.custom_tags:
            return [tag.strip() for tag in self.custom_tags.split(',')]
        return []

    def get_post_contents_list(self):
        if self.post_contents:
            return [content.strip() for content in self.post_contents.split(',')]
        return []
