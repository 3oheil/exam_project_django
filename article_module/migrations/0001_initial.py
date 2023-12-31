# Generated by Django 4.2.4 on 2023-08-21 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('url', models.CharField(max_length=100, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article_module.articlecategory', verbose_name='دسته بندی والد')),
            ],
            options={
                'verbose_name': 'دسته بندی محصول',
                'verbose_name_plural': 'دسته بندی های محصولات',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, max_length=111, verbose_name='عنوان در url')),
                ('image', models.ImageField(upload_to='images/article', verbose_name='تصویر')),
                ('short_descriptions', models.CharField(max_length=125, verbose_name='توضیحات کوتاه')),
                ('text', models.TextField(verbose_name='متن مقاله')),
                ('selected_categories', models.ManyToManyField(to='article_module.articlecategory', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'مفاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]
