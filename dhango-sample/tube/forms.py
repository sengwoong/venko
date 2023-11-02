from django import forms
from .models import Post, Comment, Tag, PostContent

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['read_author', 'title','category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name']

class PostContentForm(forms.ModelForm):
    class Meta:
        model = PostContent
        fields = ['content','file_upload','order']

