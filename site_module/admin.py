from django.contrib import admin
from . import models


# Register your models here.

# email for login in admin panel ===>>>   zahra@soheil.com
# password for login in admin panel ===>>>   85208520

class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'position']


admin.site.register(models.SiteSetting)
admin.site.register(models.SiteBanner, SiteBannerAdmin)
admin.site.register(models.FooterLinkBox)
admin.site.register(models.Slider)
admin.site.register(models.FooterLink, FooterLinkAdmin)
