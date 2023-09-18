from django.db import models


# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='عنوان سایت')
    site_url = models.CharField(max_length=100, verbose_name='دامنه سایت')
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='آدرس')
    about_site = models.CharField(max_length=100, verbose_name='درباره ما')
    fax = models.CharField(max_length=100, null=True, blank=True, verbose_name='فکس')
    phone = models.CharField(max_length=100, null=True, blank=True, verbose_name='تلفن')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.CharField(max_length=100, verbose_name='متن کپی رایت')
    site_logo = models.ImageField(upload_to='images/site_setting', verbose_name='لوکو سایت')
    is_main_site = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات اصلی'
        verbose_name_plural = 'تنظیمات اصلی سایت'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.CharField(max_length=500, verbose_name='لینک')
    footer_link = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title


# user name for login admin panel ===>>>  soheil
# email for login in admin panel ===>>>   zahra@soheil.com
# password for login in admin panel ===>>>   85208520


class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.CharField(max_length=100, verbose_name='لینک')
    url_title = models.CharField(max_length=100, verbose_name='عنوان لینک')
    descriptions = models.TextField(verbose_name='توضیحات اسلایدر')
    images = models.ImageField(upload_to='images/slider', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال شده / نشده')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title


class SiteBanner(models.Model):
    class SiteBannerPosition(models.TextChoices):
        product_list = 'product_list', 'صفحه لیست محصولات',
        product_detail = 'product_detail', 'صفحه توضیحات محصولات',
        about_us = 'about_us', 'صفحه درباره ما',

    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.CharField(max_length=100, verbose_name='لینک')
    image = models.ImageField(upload_to='images/banner', verbose_name='تصویر')
    is_active = models.BooleanField(default=False, verbose_name='فعال/ عیرفعال')
    position = models.CharField(max_length=100, choices=SiteBannerPosition.choices, verbose_name='جایگاه نمایشی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنر های تبلیغاتی'
