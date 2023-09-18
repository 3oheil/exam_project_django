from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', null=True, blank=True, verbose_name='تصویر کاربر ')
    email_activate_code = models.CharField(max_length=48, verbose_name='کد فعالسازی')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    address = models.CharField(max_length=150,null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email
