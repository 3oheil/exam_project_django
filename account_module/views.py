from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.http import Http404, HttpRequest

from .forms import RegisterForm, LoginForm, ForgetPassForm, ResetPassForm
from .models import User


# Create your views here.


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری است')
            else:
                new_user = User(
                    email=user_email,
                    email_activate_code=get_random_string(55),
                    username=user_email,
                    is_active=False
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('login-page'))

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_pass_correct = user.check_password(user_pass)
                    if is_pass_correct:
                        login(request, user)
                        return redirect(reverse('index-page'))
                    else:
                        login_form.add_error('email', 'اطلاعات وارد شده اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login-page'))


class ActivateAccount(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_activate_code__exact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_activate_code = get_random_string(55)
                user.save()
                # todo: show a success message for user
                return redirect(reverse('login-page'))
            else:
                # todo: show your account was activate massage to user
                pass
        raise Http404


class ForgetPasswordView(View):
    def get(self, request):
        forget_pass_form = ForgetPassForm()
        context = {
            'forget_pass_form': forget_pass_form
        }
        return render(request, 'account_module/forget_password_page.html', context)


class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_activate_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login-page'))

        reset_pass_form = ResetPassForm()

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }

        return render(request, 'account_module/reset_password_page.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPassForm(request.POST)
        user: User = User.objects.filter(email_activate_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login-page'))
            new_user_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(new_user_pass)
            user.email_activate_code = get_random_string(55)
            user.is_active = True
            user.save()
            return redirect(reverse('login-page'))
        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'account_module/reset_password_page.html', context)
