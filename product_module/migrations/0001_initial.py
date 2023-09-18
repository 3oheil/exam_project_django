# Generated by Django 4.2.4 on 2023-08-15 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('short_description', models.CharField(max_length=100, null=True, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(verbose_name='توضیحات تکمیلی')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف')),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='برند')),
                ('is_active', models.BooleanField(verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'برند محصول',
                'verbose_name_plural': 'برند محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('url_title', models.CharField(max_length=100, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(verbose_name='فعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف')),
            ],
            options={
                'verbose_name': 'دسته یندی',
                'verbose_name_plural': 'دسته بندی محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100, verbose_name='تگ محصول')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_caption', to='product_module.product')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': 'تگ های محصولات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.productbrand', verbose_name='برند'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_category', to='product_module.productcategory', verbose_name='دسته بندی محصولات'),
        ),
    ]