from django.http import HttpRequest, HttpResponse
# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from jalali_date import datetime2jalali
from .models import Article, ArticleCategory, ArticleCommend


# Create your views here.


class ArticleView(ListView):
    template_name = 'article_module/article_page.html'
    paginate_by = 1
    model = Article
    context_object_name = 'articles'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleView, self).get_context_data(*args, **kwargs)
        context['data'] = datetime2jalali(self.request.user.date_joined)
        return context

    def get_queryset(self):
        query = super(ArticleView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)

        return query


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article-detail_page.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article: Article = kwargs.get('object')
        context['commends'] = ArticleCommend.objects.filter(article_id=article.id, parent=None).order_by('-create_date').prefetch_related('articlecommend_set')
        context['commend_count'] = ArticleCommend.objects.filter(article_id=article.id).count()
        return context


def article_categories_component(request: HttpRequest):
    article_categories = ArticleCategory.objects.prefetch_related('articlecategory_set').filter(is_active=True,
                                                                                                parent=None)

    context = {
        'article_categories': article_categories
    }
    return render(request, 'article_module/component/article_categories_component.html', context)


# def add_article_commends(request: HttpRequest):
#     if request.user.is_authenticated:
#         article_id = request.GET.get('article_id')
#         article_commends = request.GET.get('article_commends')
#         parent_id = request.GET.get('parent_id')
#         print(article_id, article_commends, parent_id)
# 
#         new_comment = ArticleCommend(article_id=article_id, text=article_commends, user_id=request.user.id)
#         new_comment.save()
#     return HttpResponse('response')


# def add_article_commends(request: HttpRequest):
#     article_id = request.GET.get('article_id')
#     article_commends = request.GET.get('article_commends')
#     parent_id = request.GET.get('parent_id')
#     print(article_id, article_commends, parent_id)
#
#     return HttpResponse('Response')


def add_article_commend(request: HttpRequest):
    if request.user.is_authenticated:
        article_comment = request.GET.get('article_comment')
        article_id = request.GET.get('article_id')
        parent_id = request.GET.get('parent_id')

        print(article_id, article_comment, parent_id)

        new_article = ArticleCommend(article_id=article_id, text=article_comment, user_id=request.user.id, parent_id=parent_id)
        new_article.save()
        context = {
            'comments': ArticleCommend.objects.filter(article_id=article_id, parent=None).order_by('-create_date').prefetch_related(
            'articlecommend_set'),
            'comment_counts': ArticleCommend.objects.filter(article_id=article_id).count()
        }
        return render(request, 'article_module/includes/article_comment_partial.html', context)
    return HttpResponse('Response')
