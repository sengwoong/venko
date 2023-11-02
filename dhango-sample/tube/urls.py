
from django.urls import path
from . import views

app_name = 'tube'

# {% url 'tube:post_list' %}
# {% url 'tube:post_detail' post.pk %}

urlpatterns = [
    path('', views.post_main, name='post_main'),
    path('list/', views.post_list, name='post_list'),
    path('new/', views.post_createView, name='post_create'),
    path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('main/', views.post_main, name='post_main'),
    path('<int:pk>/comment/', views.comment_new, name='comment_new'),
]