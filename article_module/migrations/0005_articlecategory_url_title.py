# Generated by Django 4.2.4 on 2023-08-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0004_article_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecategory',
            name='url_title',
            field=models.CharField(max_length=100, null=True, verbose_name='عنوان'),
        ),
    ]
