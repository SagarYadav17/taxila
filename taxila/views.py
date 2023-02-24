from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from taxila.serializers import (
    KitchenCategorySerializer,
    KitchenItemSerializer,
    MaterialCategorySerializer,
    MaterialSerializer,
    MaterialVendorSerializer,
)
from taxila.models import KitchenCategory, KitchenItem, Material, MaterialCategory, MaterialVendor


class KitchenCategoryListView(ListAPIView):
    serializer_class = KitchenCategorySerializer
    queryset = KitchenCategory.objects.filter(is_active=True)

    # Cache page for the requested url
    @method_decorator(cache_page(60 * 15, key_prefix="kitchen_category"))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class MaterialCategoryListView(ListAPIView):
    serializer_class = MaterialCategorySerializer
    queryset = MaterialCategory.objects.filter(is_active=True)

    # Cache page for the requested url
    @method_decorator(cache_page(60 * 15, key_prefix="material_category"))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class MaterialVendorListView(ListAPIView):
    serializer_class = MaterialVendorSerializer
    queryset = MaterialVendor.objects.filter(is_active=True)

    # Cache page for the requested url
    @method_decorator(cache_page(60 * 15, key_prefix="material_vendor"))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class MaterialListView(ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.filter(is_active=True, category__is_active=True, vendor__is_active=True)

    # Cache page for the requested url
    @method_decorator(cache_page(60 * 15, key_prefix="material"))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class KitchenItemListView(ListAPIView):
    serializer_class = KitchenItemSerializer
    queryset = KitchenItem.objects.filter(is_active=True, category__is_active=True)

    # Cache page for the requested url
    @method_decorator(cache_page(60 * 15, key_prefix="kitchen_item"))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
