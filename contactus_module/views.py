from builtins import super

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView, CreateView

from site_module.models import SiteSetting
from .forms import ContactModelForm, ProfileForm
from .models import UserProfile


class contactusview(FormView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactModelForm
    success_url = '/contact-us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        setting: SiteSetting = SiteSetting.objects.filter(is_main_site=True).first()
        context['setting'] = setting
        return context


def story_file(file):
    with open('temp/image.jpg', "wb+") as dest:
        for chunk in file.chunk():
            dest.write(chunk)


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile/'
