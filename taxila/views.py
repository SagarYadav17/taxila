from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from taxila.serializers import (
    KitchenCategorySerializer,
    KitchenItemSerializer,
    MaterialCategorySerializer,
    MaterialSerializer,
    MaterialVendorSerializer,
)
from taxila.models import (
    Inspiration,
    InspirationCategory,
    KitchenCategory,
    KitchenItem,
    Material,
    MaterialCategory,
    MaterialVendor,
)


class HomepageAPIView(APIView):
    # Cache page for the requested url
    @method_decorator(cache_page(60 * 15))
    def get(self, request):
        data = {}
        data["kitchen_category"] = KitchenCategory.objects.filter(is_active=True).values()
        data["material_category"] = MaterialCategory.objects.filter(is_active=True).values()
        data["inspiration_category"] = InspirationCategory.objects.filter(is_active=True).values()
        return Response(data)


class KitchenCategoryListView(ListAPIView):
    serializer_class = KitchenCategorySerializer
    queryset = KitchenCategory.objects.filter(is_active=True)

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MaterialCategoryListView(ListAPIView):
    serializer_class = MaterialCategorySerializer
    queryset = MaterialCategory.objects.filter(is_active=True)

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MaterialVendorListView(ListAPIView):
    serializer_class = MaterialVendorSerializer
    queryset = MaterialVendor.objects.filter(is_active=True)

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MaterialListView(ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.filter(is_active=True, category__is_active=True, vendor__is_active=True)

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class KitchenItemListView(ListAPIView):
    serializer_class = KitchenItemSerializer
    queryset = KitchenItem.objects.filter(is_active=True, category__is_active=True)

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class InspirationListView(ListAPIView):
    serializer_class = MaterialCategorySerializer
    queryset = Inspiration.objects.filter(is_active=True, category__is_active=True)

    def get(self, *args, **kwargs):
        data = super().get(*args, **kwargs)
        data["category"] = InspirationCategory.objects.filter(is_active=True).values()
        return data

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
