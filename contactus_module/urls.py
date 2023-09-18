from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactusview.as_view(), name='contact-us'),
    path('create-profile/', views.CreateProfileView.as_view(), name='create-profile/')
]
