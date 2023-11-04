
from django.urls import path
from . import views

app_name = 'tube'

# {% url 'tube:post_list' %}
# {% url 'tube:post_detail' post.pk %}

urlpatterns = [
    path('', views.post_main, name='post_main'),
    path('list/', views.post_list, name='post_list'),
    path('new/', views.post_createView, name='post_create'),
    path('new/<int:pk>/', views.post_create_detailView, name='post_create_detail'),
    path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('main/', views.post_main, name='post_main'),
    path('<int:pk>/comment/', views.comment_new, name='comment_new'),
    path('post/<int:pk>/delete/<int:tag_id>', views.delete_tag, name='tag_delete'),  
    path('<int:pk>/add_tag', views.add_tag, name='add_tag'),
    path('<int:pk>/post_new', views.add_post, name='add_post'),

]