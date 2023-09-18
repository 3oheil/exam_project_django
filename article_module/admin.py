from django.contrib import admin
from django.http import HttpRequest

from . import models
from .models import Article


# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'parent', 'is_active']
    list_editable = ['url', 'parent', 'is_active']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'auther']

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
            obj.auther = request.user
        return super().save_model(request, obj, form, change)


class ArticleCommendAdmin(admin.ModelAdmin):
    list_display = ['user', 'create_date', 'parent']


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.ArticleCommend, ArticleCommendAdmin)
