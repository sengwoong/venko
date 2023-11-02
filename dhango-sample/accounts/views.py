from django.shortcuts import render

# accounts > views.py
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login

signup = CreateView.as_view(
    form_class=CustomUserCreationForm,  # 커스텀 폼으로 변경
    template_name='accounts/form.html',
    success_url='/accounts/login/'
)


from django.contrib.auth import authenticate, login

class CustomLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'accounts/form.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(self.request, user)  # 충돌을 피하기 위해 login 함수를 auth_login으로 수정
            self.request.session['permission'] = user.permission  # 세션에 추가 정보 저장
            self.request.session['department'] = user.department
            self.request.session['position'] = user.position
            self.request.session['full_name'] = user.full_name
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
        
        
login = CustomLoginView.as_view()

logout = LogoutView.as_view(
    next_page = '/accounts/login/'
)

@login_required
def profile(request):
    user = request.user
    context = {
        'permission': user.permission,
        'department': user.department,
        'position': user.position,
        'full_name': user.full_name,
    }
    return render(request, 'accounts/profile.html', context)





