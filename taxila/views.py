from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from taxila.serializers import (
    InspirationSerializer,
    KitchenItemSerializer,
    ParentMaterialDetailSerializer,
    MaterialSerializer,
    MetaDataSerializer,
    VideoSerializer,
)
from taxila.models import (
    HomepageBanner,
    Inspiration,
    InspirationCategory,
    KitchenCategory,
    KitchenItem,
    Material,
    MaterialCategory,
    MetaData,
    ParentCategory,
    Video,
    VideoCategory,
)
from django.conf import settings


class HomepageAPIView(APIView):
    # Cache page for the requested url
    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
    def get(self, request):
        parent_category_objs = ParentCategory.objects.filter(is_active=True)
        parent_data = []

        for obj in parent_category_objs:
            data = {
                "id": obj.id,
                "name": obj.name,
                "items": MaterialCategory.objects.filter(parent_category_id=obj.id).values("id", "slug", "name"),
            }
            parent_data.append(data)

        data = {
            "material_category": parent_data,
            "kitchen_category": KitchenCategory.objects.filter(is_active=True).values(),
        }

        return Response(data)


class ParentMaterialDetailView(RetrieveAPIView):
    serializer_class = ParentMaterialDetailSerializer
    queryset = ParentCategory.objects.filter(is_active=True)
    lookup_field = "id"

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MaterialView(RetrieveAPIView):
    serializer_class = MaterialSerializer
    lookup_field = "id"

    def get_queryset(self):
        queryset = Material.objects.filter(
            is_active=True,
            category__is_active=True,
            vendor__is_active=True,
            category__parent_category__is_active=True,
        )
        return queryset

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
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

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
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

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
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

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MetaDataView(RetrieveAPIView):
    serializer_class = MetaDataSerializer
    queryset = MetaData.objects
    lookup_field = "slug"

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class InspirationCategoryView(APIView):
    def get(self, request):
        queryset = InspirationCategory.objects.filter(is_active=True).values()
        return Response(queryset)

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class KitchenCategoryView(APIView):
    def get(self, request):
        queryset = KitchenCategory.objects.filter(is_active=True).values()
        return Response(queryset)

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MaterialCategoryView(APIView):
    def get(self, request):
        queryset = MaterialCategory.objects.filter(is_active=True).values()
        return Response(queryset)

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class VideoCategoryView(APIView):
    def get(self, request):
        queryset = VideoCategory.objects.filter(is_active=True).values()
        return Response(queryset)

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class BannerImagesView(APIView):
    def get(self, request):
        queryset = HomepageBanner.objects.filter(is_active=True)

        desktop_urls = [item.image.url for item in queryset.filter(banner_type="desktop")]
        mobile_urls = [item.image.url for item in queryset.filter(banner_type="mobile")]

        data = {
            "desktop": desktop_urls,
            "mobile": mobile_urls,
        }

        return Response(data)

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductSlugVerifyView(APIView):
    def get(self, request, slug):
        exists = Material.objects.filter(slug=slug).exists()
        return Response({"exists": exists})

    @method_decorator(cache_page(settings.CACHE_DEFAULT_TIMEOUT))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
