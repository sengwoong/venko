# views.py
from django.db.models import Prefetch

# write는 로그인 해야만
# update와 delete는 업로드한 사용자여야만
from django.db.models import Subquery, OuterRef
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.db.models.query import QuerySet
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView 
from .models import Post, Comment, PostHistory,Tag , PostContent
from .forms import PostForm, CommentForm ,TagForm,PostContent,PostContentForm
from django.urls import reverse_lazy , reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F


from django.db.models import Q
def blog_select_method(qs, q, category, selecttag):
    if q and category and selecttag:
        qs = qs.filter(Q(title__icontains=q) & Q(category=category) & Q(tags__tag_name=selecttag))
    elif q and category:
        qs = qs.filter(Q(title__icontains=q) & Q(category=category))
    elif q:
        qs = qs.filter(title__icontains=q)
    elif category:
        qs = qs.filter(category=category)
   


    elif selecttag:
        qs = qs.filter(tags__tag_name=selecttag)
    return qs

class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        category = self.request.GET.get('category', '') 
        selecttag = self.request.GET.get('selecttag', '')
        print(category)
        print(selecttag)
        print(q)
        return blog_select_method(qs, q, category, selecttag)

   

post_list = PostListView.as_view()



class PostHistoryListView(ListView):
    model = PostHistory
    template_name = 'tube/post_history_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        category = self.request.GET.get('category', '') 
        selecttag = self.request.GET.get('selecttag', '')
        return blog_select_method(qs, q, category, selecttag)
      

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_history_list'] = self.get_queryset()
        return context



history_list = PostHistoryListView.as_view()
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'tube/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_form'] = PostForm()
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect(reverse('tube:post_create_detail', kwargs={'pk': post.pk}))

post_createView = PostCreateView.as_view()


class PostCreateDetailView(LoginRequiredMixin, DetailView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form_detail.html'


    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        try:
            post = Post.objects.get(pk=pk)
            return post
        except Post.DoesNotExist:
            raise Http404("Post does not exist")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_form'] = TagForm()
        context['content_form'] = PostContentForm()
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()

        tag_form = TagForm(self.request.POST)
        if tag_form.is_valid():
            tag = tag_form.save(commit=False)
            tag.post = post
            tag.save()

        comment_form = PostContentForm(self.request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        return redirect(self.success_url)

post_create_detailView = PostCreateDetailView.as_view()


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

            # view_count를 증가시키고 저장합니다.
            post.view_count += 1
            post.save()
            print(post.__dict__)
            return post
        except Post.DoesNotExist:
            raise Http404("Post does not exist")

from django.shortcuts import get_object_or_404

class PostHistoryDetailView(DetailView):
    # context_object_name = 'licat_objects' # {{licat_objects.title}} 이런식으로 사용 가능

    def get_context_data(self, **kwargs):
        '''
        여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
        '''
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        post_contents = self.object.post_contents.strip('[]') if self.object.post_contents else ''
        tags = self.object.tags.strip('[]') if self.object.tags else ''
        print("self.object.post_contents")
        print(self.object.post_contents)
        print("self.object.tags")
        print(self.object.tags)
        post_contents_list = [item.strip() for item in post_contents.split(',') if item.strip()]
        tags_list = [item.strip() for item in tags.split(',') if item.strip()]
        print("tags_list")
        print(tags_list)
        formatted_post_contents_list = []
        for item in post_contents_list:
            if ':' in item:
                parts = item.split(':')
                order = parts[0]
                content = ":".join(parts[1:])
                formatted_post_contents_list.append({'order': order, 'content': content})


        context['post_contents_list'] = formatted_post_contents_list
        print(formatted_post_contents_list)
        context['tags_list'] = tags_list
        print(tags)
        return context
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        post = get_object_or_404(PostHistory, pk=pk)
        # Increment the view_count and save
        post.view_count += 1
        post.save()
        return post

post_detail = PostDetailView.as_view()
posthistory_detail = PostHistoryDetailView.as_view()




class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user


post_edit = PostUpdateView.as_view()

@login_required
def post_delete_history(request, pk):
    print("history")
    post = get_object_or_404(PostHistory, pk=pk)
    print(post)
    if post.author == request.user:
        post.delete()
        print("실행")
        return HttpResponseRedirect(reverse_lazy('tube:history_list'))
    else:
        # 처리되지 않은 사용자의 경우 어떤 동작을 수행할지 여기에 추가할 수 있습니다.
        print("실패")
        pass


class PostFineView(DeleteView):
    model = Post
    success_url = reverse_lazy('tube:post_list')

    def test_func(self):
        return self.get_object().author == self.request.user

post_fine = PostFineView.as_view()


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
@login_required
def add_tag(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name')
        if not post.tags.filter(tag_name=tag_name).exists(): 
            post.tags.create(tag_name=tag_name, post=post)
        url = request.POST.get('redirect_url')
        if url == "creat":  # 수정된 부분
            return redirect('tube:post_create_detail', pk)
        elif url == "detail":  # 수정된 부분
            return redirect('tube:post_detail', pk)
    return HttpResponse("Some default response")

@login_required
def delete_tag(request, pk, tag_id):
    post = Post.objects.get(pk=pk)
    tag = post.tags.get(pk=tag_id)

    if request.method == 'POST':
        tag.delete()

        url = request.POST.get('redirect_url')
        print(url)
        if url == "creat":
            return redirect('tube:post_create_detail', pk)
        elif url == "detail":
            return redirect('tube:post_detail', pk)
    return HttpResponse("Some default response")


@login_required
def add_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostContentForm(request.POST)

        url = request.POST.get('redirect_url')
        print("url")
        print(url)
        if form.is_valid():
            print("valid")
            comment = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
            comment.post = post
            comment.author = request.user
            comment.save()
        if url == "creat":  # 수정된 부분
            return redirect('tube:post_create_detail', pk)
        elif url == "detail":  # 수정된 부분
            return redirect('tube:post_create_detail', pk)

    return HttpResponse("Some default response")



from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

# 게시물 수정

# 게시물 수정# 게시물 수정
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        print("post_edit")
        # POST 요청 처리
        content_id = request.POST.get('content_id')  # 수정할 PostContent의 ID를 가져옵니다
        new_content = request.POST.get('new_content')  # 새로운 content 데이터를 가져옵니다
        print("content_id")
        print(content_id)
        print(new_content)
        if content_id and new_content:
            print(content_id)
            post_content = PostContent.objects.get(pk=content_id) 
            print(post_content) # 해당하는 PostContent 객체를 가져옵니다
            post_content.content = new_content  # content를 업데이트합니다
            post_content.save()  # 변경된 내용을 저장합니다
        return redirect('tube:post_create_detail', pk=post.pk)

    return redirect('tube:post_create_detail', pk=post.pk)

from django.shortcuts import redirect

# 게시물 삭제
def content_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    content_id = request.POST.get('content_id')  # 수정할 PostContent의 ID를 가져옵니다
    post_content = PostContent.objects.get(pk=content_id) 
    if request.method == "POST":
        post_content.delete()
        return redirect('tube:post_detail', pk=post.pk)
    return redirect('tube:post_detail', pk=post.pk)


# 댓글 수정
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        new_message = request.POST.get('new_message')  # 수정할 새로운 댓글 메시지를 가져옵니다
        if new_message:
            comment.message = new_message  # 댓글을 업데이트합니다
            comment.save()  # 변경된 내용을 저장합니다
        return redirect('tube:post_detail', pk=comment.post.pk)
    return render(request, 'comment_edit.html', {'comment': comment})


# 댓글 삭제
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        comment.delete()
        return redirect('tube:post_detail', pk=comment.post.pk)
    return render(request, 'comment_delete.html', {'comment': comment})
