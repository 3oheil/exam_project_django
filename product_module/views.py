from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from site_module.models import SiteBanner
from .models import Product, ProductCategory, ProductBrand, ProductGallery
from utils.convert import grouped_list


# Create your views here.

class ProductListView(ListView):
    template_name = 'product_module_/product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()

        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_min_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPosition.product_list)

        # user_ip = get_client_ip(self.request)
        # user_id = None
        # if self.request.user.is_authenticated:
        #     user_id = self.request.user.id
        #
        # has_been_visit = ProductVisit.objects.filter(ip__iexact=user_ip).first()
        # if not has_been_visit:
        #     new_visit = ProductVisit(ip=user_ip, user_id=user_id)
        #     new_visit.save()

        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        category_brand = self.kwargs.get('brand')
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')

        if start_price is not None:
            query = query.filter(price__gte=start_price)

        if end_price is not None:
            query = query.filter(price__lte=end_price)

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)

        if category_brand is not None:
            query = query.filter(brand__url_title__iexact=category_brand)
        return query


class ProductDetailView(DetailView):
    template_name = 'product_module_/product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        # loaded_product = self.object
        # request = self.request
        # favorite_product_id = request.session['product_favorite']
        # context['is_favorite'] = favorite_product_id == loaded_product
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPosition.product_detail)
        context['gallery_products'] = grouped_list(list(ProductGallery.objects.all()), 3)
        return context


#
# class AddProductFavorite(View):
#     def post(self, request):
#         product_id = request.POST['product_id']
#         product = Product.objects.get(pk=product_id)
#         request.session['product_favorite'] = product
#         return redirect(product.get_absolute_url())


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'product_categories': product_categories
    }
    return render(request, 'product_module_/product_component/product_component_page.html', context)


def product_brands_component(request: HttpRequest):
    product_brand = ProductBrand.objects.annotate(product_count=Count('product')).filter(is_active=True).filter()
    context = {
        'product_brand': product_brand
    }
    return render(request, 'product_module_/product_component_page/product_component_page.html', context)
