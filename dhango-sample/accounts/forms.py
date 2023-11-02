from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    department_CHOICES = [
        ('as부서', 'as부서'),
        ('cs부서', 'cs부서'),
        ('판매마케팅부서', '판매마케팅부서'),
        ('경영부서', '경영부서'),
    ]
    department = forms.ChoiceField(choices=department_CHOICES)

    position_CHOICES = [
        ('현장직', '현장직'),
        ('관리직', '관리직'),
        ('사원', '사원'),
        ('대리', '대리'),
        ('관리자', '관리자'),
        ('사장', '사장'),
        ('팀장', '팀장'),
        ('사수', '사수'),
    ]
    position = forms.ChoiceField(choices=position_CHOICES)





    class Meta:
        model = CustomUser
        fields = ['username',  'department', 'position', 'full_name']
