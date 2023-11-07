
from django.urls import path
from . import views

app_name = 'tube'

# {% url 'tube:post_list' %}
# {% url 'tube:post_detail' post.pk %}
urlpatterns = [
    path('list/', views.post_list, name='post_list'),
    path('new/', views.post_createView, name='post_create'),
    path('new/<int:pk>/', views.post_create_detailView, name='post_create_detail'),
    path('history_list/', views.history_list, name='history_list'),
    path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('historydetail/<int:pk>/', views.posthistory_detail, name='post_historydetail'),


    path('delete-history/<int:pk>/', views.post_delete_history, name='post_delete_history'),
    path('fine/<int:pk>/', views.post_fine, name='post_fine'),


    path('<int:pk>/comment', views.comment_new, name='comment_new'),
    path('<int:pk>/comment/<int:parent_pk>', views.comment_reply_new, name='comment_reply_new'),

    path('post/<int:pk>/delete/<int:tag_id>', views.delete_tag, name='tag_delete'),  
    path('<int:pk>/add_tag', views.add_tag, name='add_tag'),
    path('<int:pk>/post_new', views.add_post, name='add_post'),

    # 수정, 삭제 관련 URL 패턴 추가
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/content_delete/', views.content_delete, name='content_delete'),
    path('comment/<int:pk>/edit/<int:commentpk>', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/<int:commentpk>', views.comment_delete, name='comment_delete'),
]


# 이미지-> 베이스64 대댓글 https://curryyou.tistory.com/474
