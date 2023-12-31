from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from product_module.models import Product
from .models import Order, OrderDetail


# Create your views here.


# if request.user.is_authenticated:
#     product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
#     if product is not None:
#         current_order, created = Order.objects.get_or_create(is_pain=False, user_id=request.user.id)
#         current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
#
#         if current_order_detail is not None:
#             current_order_detail.count += int(count)
#             current_order_detail.save()
#         else:
#
#             new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
#             new_detail.save()
#
#             # new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
#             # new_detail.save()
#             return JsonResponse({
#                 'status': 'success full'
#             })
# def add_product_to_order(request: HttpRequest):
#     product_id = request.GET.get('product_id')
#     count = request.GET.get('count')
#
#     if request.user.is_authenticated:  # check for login user
#         product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
#         if product is not None:
#             current_order, created = Order.objects.get_or_create(is_pain=False, user_id=request.user.id)
#             current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
#             if current_order_detail is not None:
#                 current_order_detail.count += int(count)
#                 current_order_detail.save()
#             else:
#                 new_detail = OrderDetail(order_id=current_order.id, roduct_id=product, count=count)
#                 new_detail.save()
#             return JsonResponse({'status': 'is done'})
#         else:
#             return JsonResponse({'status': 'not found'})
#     else:
#         return JsonResponse({'status': 'not_auth'})


def add_product_to_order(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False)
        if product is not None:
            pass
        else:
            return JsonResponse({
                'status': 'not found'
            })
    else:
        return JsonResponse({
            'status': 'not auth'
        })


def order_detail_page(request: HttpRequest):
    product = Product.objects.filter(is_active=True, is_delete=False).first()
    context = {
        'product': product
    }
    return render(request, 'order_module/order_detail_page.html', context)
