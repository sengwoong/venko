
# accounts/forms.py
from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
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
        fields = ['username', 'email', 'password', 'department', 'position', 'full_name']


class CustomUserChangeForm(forms.ModelForm):
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
        fields = ['username', 'email', 'department', 'position', 'full_name']
