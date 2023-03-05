from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from taxila.serializers import (
    InspirationSerializer,
    KitchenItemSerializer,
    MaterialSerializer,
    MetaDataSerializer,
    VideoSerializer,
)
from taxila.models import (
    Inspiration,
    InspirationCategory,
    KitchenCategory,
    KitchenItem,
    Material,
    MaterialCategory,
    MetaData,
    ParentCategory,
    Video,
)
from django.conf import settings


class HomepageAPIView(APIView):
    # Cache page for the requested url
    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
    def get(self, request):
        parent_category_objs = ParentCategory.objects.filter(is_active=True)
        parent_data = {}

        for obj in parent_category_objs:
            parent_data[obj.name.lower()] = MaterialCategory.objects.filter(
                parent_category_id=obj.id, is_active=True
            ).values()

        data = {
            "material_category": parent_data,
            "kitchen_category": KitchenCategory.objects.filter(is_active=True).values(),
            "inspiration_category": InspirationCategory.objects.filter(is_active=True).values(),
        }

        return Response(data)


class MaterialView(ListAPIView):
    serializer_class = MaterialSerializer

    def get_queryset(self):
        queryset = Material.objects.filter(is_active=True, category__is_active=True, vendor__is_active=True)

        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category_id=category)

        return queryset

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class KitchenView(ListAPIView):
    serializer_class = KitchenItemSerializer

    def get_queryset(self):
        queryset = KitchenItem.objects.filter(is_active=True, category__is_active=True)

        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category_id=category)

        return queryset

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class InspirationView(ListAPIView):
    serializer_class = InspirationSerializer

    def get_queryset(self):
        queryset = Inspiration.objects.filter(is_active=True, category__is_active=True)

        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category_id=category)

        return queryset

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class VideoView(ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        queryset = Video.objects.filter(is_active=True, category__is_active=True)

        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category_id=category)

        return queryset

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MetaDataView(RetrieveAPIView):
    serializer_class = MetaDataSerializer
    queryset = MetaData.objects
    lookup_field = "slug"

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
