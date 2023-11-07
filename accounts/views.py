from django.urls import reverse_lazy
from .models import CustomUser

from django.shortcuts import render
from django.shortcuts import redirect
# accounts > views.py
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
signup = CreateView.as_view(
    form_class=CustomUserCreationForm,  # 커스텀 폼으로 변경
    template_name='accounts/form.html',
    success_url='/accounts/login/'
)



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







class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('accounts:profile')# Change 'profile' to your profile view name

    def get_object(self, queryset=None):
        return self.request.user
    
post_file_update = ProfileUpdateView.as_view()

def change_password(request):
    success_url = reverse_lazy('accounts:profile')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important! to update the user's session
            return redirect(success_url)  # Redirect to the profile page after changing the password
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})