from django.urls import path
from . import views

urlpatterns = [
    # path('add-to-order', views.add_product_to_order, name='add_product_to_order')
    path('add-order', views.add_product_to_order, name='add_to_order_box')
]
