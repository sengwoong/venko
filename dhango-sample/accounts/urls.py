from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_change/', views.post_file_update, name='profile_change'),
    path('profile_change/pass/', views.change_password, name='profile_change_pass'),
]
# - 비밀번호 변경기능
# - 프로필 수정
# - 닉네임 추가
# 11.