# views.py
from django.db.models import Prefetch

# write는 로그인 해야만
# update와 delete는 업로드한 사용자여야만
from django.db.models import Subquery, OuterRef
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.db.models.query import QuerySet
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView 
from .models import Post, Comment,Tag , PostContent
from .forms import PostForm, CommentForm ,TagForm,PostContent,PostContentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

post_list = PostListView.as_view()

from django.shortcuts import redirect

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_form'] = PostForm()
        context['tag_form'] = TagForm()
        context['content_form'] = PostContentForm()
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        print("post.__dict__")
        print("post.__dict__")

        print(post.__dict__)
        print("post.__dict__")
        post.save()

        tag_form = TagForm(self.request.POST)
        print(tag_form)
        if tag_form.is_valid():
            tag = tag_form.save(commit=False)
            tag.post = post
            print("tag")
            print(tag.__dict__)
            print("tag")
            tag.save()

        comment_form = PostContentForm(self.request.POST)
        print(comment_form)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            print("comment.__dict__")
            print("comment.__dict__")
            print(comment.__dict__)
            comment.save()


        return redirect(self.success_url)

post_createView = PostCreateView.as_view()





class PostDetailView(DetailView):

    # context_object_name = 'licat_objects' # {{licat_objects.title}} 이런식으로 사용 가능

    def get_context_data(self, **kwargs):
        '''
        여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
        '''
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')

        try:
            post = Post.objects.get(pk=pk)

            # comments = post.comments.all()  
            comments = post.posttags.all()  
            print("comments")
# posttags
# postcontents
            print(comments)
            print("comments")
            # view_count를 증가시키고 저장합니다.
            post.view_count += 1
            post.save()
            print(post.__dict__)
            return post
        except Post.DoesNotExist:
            raise Http404("Post does not exist")

post_detail = PostDetailView.as_view()


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user


post_edit = PostUpdateView.as_view()


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('tube:post_list')

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user

post_delete = PostDeleteView.as_view()

class PostMain(ListView):
    model = Post
    template_name = 'tube/main.html'
    def get_queryset(self):
        qs = super().get_queryset()
        print("qs")
        print(Post)
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

post_main = PostMain.as_view()


@login_required
def comment_new(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('tube:post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'tube/form.html', {
        'form': form,
    })
