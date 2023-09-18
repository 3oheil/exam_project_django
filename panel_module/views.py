from django.http import HttpRequest
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import logout
from account_module.models import User
from .forms import EditProfile, ChangePasswordForm


# Create your views here.


class UserPanelDashboard(TemplateView):
    template_name = 'panel_module/panel_user_page.html'


class UserEditProfileView(View):
    def get(self, request: HttpRequest):
        correct_user: User = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfile(instance=correct_user)
        context = {
            'edit_form': edit_form,
            'correct_user': correct_user
        }
        return render(request, 'panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        correct_user: User = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfile(request.POST, request.FILES, instance=correct_user)

        if edit_form.is_valid():
            edit_form.save()

        context = {
            'edit_form': edit_form,
            'correct_user': correct_user
        }
        return render(request, 'panel_module/edit_profile_page.html', context)


class ChangePasswordView(View):
    def get(self, request: HttpRequest):
        context = {
            'form': ChangePasswordForm()
        }
        return render(request, 'panel_module/Change_password_page.html', context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('password')):
                current_user.set_password(form.cleaned_data.get('new_password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login-page'))
            else:
                form.add_error('password', 'کلمه عبور وارد شده اشتباه می باشد')
        context = {
            'form': form
        }
        return render(request, 'panel_module/Change_password_page.html', context)


def user_panel_component(request: HttpRequest):
    return render(request, 'panel_module/panel_component/user_panel_component.html')
