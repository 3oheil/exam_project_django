# Generated by Django 4.2.4 on 2023-08-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس'),
        ),
    ]
