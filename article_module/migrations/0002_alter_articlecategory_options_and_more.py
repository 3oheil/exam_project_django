# Generated by Django 4.2.4 on 2023-08-21 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'verbose_name': 'دسته بندی مقاله', 'verbose_name_plural': 'دسته بندی های مقالات'},
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article_module.articlecategory', verbose_name='دسته بندی والد'),
        ),
    ]
