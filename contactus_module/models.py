from django.db import models


class ContactUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    massage = models.TextField(verbose_name='متن پیام')
    create_date = models.DateTimeField(verbose_name='تاریخ ارسال شده', auto_now_add=True)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    image = models.ImageField(upload_to='images')
