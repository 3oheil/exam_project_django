from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index-page'),
    path('about-us/', views.AboutView.as_view(), name='about-us-page'),
]
