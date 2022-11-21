from django.contrib import admin
from test_app.models import Application, Category, Feature, KitchenCategory, KitchenItem, Material, TechnicalSpecification, Vendor


admin.site.register(KitchenCategory)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Material)
admin.site.register(Feature)
admin.site.register(Application)
admin.site.register(TechnicalSpecification)
admin.site.register(KitchenItem)
