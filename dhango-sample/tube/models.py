from django.db import models
from django.conf import settings



class Post(models.Model):
    CATEGORY_CHOICES = [
        ('bug', '버그'),
        ('quest', '퀘스트'),
        ('help', '도움'),
        ('rescue', '구조'),
    ]
 
    post_contents = models.ManyToManyField('PostContent', related_name='posts', blank=True)

    tags = models.ManyToManyField('Tag', blank=True, related_name='tags' ,db_index=True)

    title = models.CharField(max_length=100, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='bug', null=False)

    #작성자
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_written')
  
    

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    front_idx =  models.TextField(blank=True, null=True)
    back_idx =  models.TextField(blank=True, null=True)


    def __str__(self):
        return self.message
# 인데싱 걸기가 힘들고 튜닝이 어렵다 이유는 자주 변경 되는 로직이라서 
# 원래는 nosql 로 넣고 푸쉬를하고 애는 쓰기전용으로 해서 만일 값이 없을떄
# 다시 몽고디비에 넣어야하는데 하드 코드로 돌아가다가 일정이상 유저가모이면 캐싱처리 할거다.
#단 인설트하면 해당 레디스는 지워야한다.

class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postcontents', db_index=True)
    order = models.IntegerField()
    file_upload = models.ImageField(upload_to = "media/", null=True, blank=True)
    content = models.TextField(blank=True, null=True)

    
    

# 인데싱 걸기가 힘들고 튜닝이 어렵다 이유는 자주 변경 되는 로직이라서 
# 원래는 nosql 로 넣고 푸쉬를하고 애는 쓰기전용으로 해서 만일 값이 없을떄
# 다시 몽고디비에 넣어야하는데 하드 코드로 돌아가다가 일정이상 유저가모이면 캐싱처리 할거다.
#단 인설트하면 해당 레디스는 지워야한다.
class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posttags', db_index=True)
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


# 끝난거는 인데싱이 필요없어서 겹처도넣는다
# 이떄 카테고리랑 태그를 풀어서 넣는데 이는 인설트가 없다고 판단하기 때문이다.



class PostHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_contents = models.TextField()
    category = models.CharField(max_length=50, default='bug', null=False , db_index=True)
    tags = models.TextField()
    title = models.CharField(max_length=100, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clear_posts_written')
    view_count = models.PositiveIntegerField(default=0)
    post_comments = models.TextField(default='')
    images = models.ManyToManyField('Image', related_name='posts')
    def __str__(self):
        return self.title

class Image(models.Model):
    post = models.ForeignKey(PostHistory, on_delete=models.CASCADE, related_name='hisimg')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.image.url
