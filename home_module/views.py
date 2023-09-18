from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import TemplateView

from product_module.models import Product, ProductCategory
from site_module.models import SiteSetting, FooterLinkBox, Slider
from utils.convert import grouped_list


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(is_active=True)
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        context['latest_products'] = grouped_list(latest_products)
        categories = list(
            ProductCategory.objects.filter(is_active=True, is_delete=False)[:6])
        categories_products = []
        for category in categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': category.product_category.all()[:4]
            }
            categories_products.append(item)
        context['categories_products'] = categories_products
        return context


def header_partial_view(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_site=True).first()
    context = {
        'setting': setting
    }
    return render(request, 'shared/site_header_partial.html', context)


def footer_partial_view(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_site=True).first()
    footer_link_boxs = FooterLinkBox.objects.all()

    for item in footer_link_boxs:
        item.footerlink_set
    context = {
        'setting': setting,
        'footer_link_box': footer_link_boxs
    }
    return render(request, 'shared/site_footer_partial.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_site=True).first()
        context['setting'] = site_setting
        return context
