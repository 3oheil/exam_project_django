# Generated by Django 4.2.4 on 2023-08-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0002_user_about_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='number',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile', verbose_name='تصویر کاربر '),
        ),
    ]
