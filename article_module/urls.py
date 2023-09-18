from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleView.as_view(), name='article-page'),
    path('cat/<str:category>', views.ArticleView.as_view(), name='article_by_category_page'),
    path('<pk>/', views.ArticleDetailView.as_view(), name='article_detail_page'),
    path('add_article_commend', views.add_article_commend, name='add_article_commend')
]
