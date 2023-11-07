from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    # 다른 URL 매핑 추가
]
