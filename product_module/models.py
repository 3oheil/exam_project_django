from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from account_module.models import User


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url_title = models.CharField(max_length=100, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال')
    is_delete = models.BooleanField(verbose_name='حذف')

    class Meta:
        verbose_name = 'دسته یندی'
        verbose_name_plural = 'دسته بندی محصولات'

    def __str__(self):
        return f"{self.title}"


class ProductBrand(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='برند')
    url_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال')

    class Meta:
        verbose_name = 'برند محصول'
        verbose_name_plural = 'برند محصولات'

    def __str__(self):
        return self.title


class Product(models.Model):  # Model for all protocol and the information
    title = models.CharField(max_length=100, verbose_name='عنوان')
    price = models.IntegerField(verbose_name='قیمت')
    category = models.ManyToManyField(ProductCategory, related_name='product_category',
                                      verbose_name='دسته بندی محصولات')
    brand = models.ForeignKey(ProductBrand, db_index=True, on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name='برند')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    short_description = models.CharField(max_length=100, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات تکمیلی')
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')
    slug = models.SlugField(default="", null=False, db_index=True, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title


class ProductTag(models.Model):
    caption = models.CharField(max_length=100, verbose_name='تگ محصول')
    product = models.ForeignKey(Product, db_index=True, on_delete=models.CASCADE, related_name='product_caption',
                                null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.caption


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=100, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return f"{self.product.title}/ {self.ip}"

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید محصولات'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    images = models.ImageField(upload_to='images/gallery', verbose_name="تصویر محصول")

    class Meta:
        verbose_name = 'گالری تصویر'
        verbose_name_plural = 'گالری تصاویر'

    def __str__(self):
        return self.product.title
