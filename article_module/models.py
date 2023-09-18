from django.db import models
from jalali_date import date2jalali

from account_module.models import User


# Create your models here.


class ArticleCategory(models.Model):
    parent = models.ForeignKey(to='ArticleCategory', on_delete=models.CASCADE, verbose_name='دسته بندی والد', null=True,
                               blank=True)
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url_title = models.CharField(max_length=100, verbose_name='نام آدرس', null=True)
    url = models.CharField(max_length=100, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقالات'


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=111, db_index=True, allow_unicode=True, verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/article', verbose_name='تصویر')
    short_descriptions = models.CharField(max_length=125, verbose_name='توضیحات کوتاه')
    text = models.TextField(verbose_name="متن مقاله")
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name='دسته بندی')
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='نویسنده')
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ایجاد')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def get_jalali_create_data(self):
        return date2jalali(self.create_date)

    def get_jalali_create_time(self):
        return self.create_date.strftime('%H: %M')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مفاله'
        verbose_name_plural = 'مقالات'


class ArticleCommend(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('ArticleCommend', null=True, blank=True, on_delete=models.CASCADE, verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

