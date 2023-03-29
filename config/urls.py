from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from taxila.views import (
    BannerImagesView,
    HomepageAPIView,
    InspirationView,
    KitchenCategoryView,
    KitchenView,
    MediaCategoryView,
    MediaView,
    ParentMaterialDetailView,
    MaterialCategoryView,
    MaterialDetailView,
    MetaDataView,
    ProductSlugVerifyView,
    VideoCategoryView,
    VideoView,
    InspirationCategoryView,
    MaterialView,
)

admin.site.site_header = "Taxila Stone Administration"
admin.site.index_title = "Taxila Stone"
admin.site.site_title = "Administration"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django_prometheus.urls")),
    path("banner-images/", BannerImagesView.as_view(), name="banners-images"),
    path("kitchen-category/", KitchenCategoryView.as_view(), name="kitchen-category"),
    path("inspiration-category/", InspirationCategoryView.as_view(), name="inspiration-category"),
    path("material-category/", MaterialCategoryView.as_view(), name="material-category"),
    path("video-category/", VideoCategoryView.as_view(), name="video-category"),
    path("media-category/", MediaCategoryView.as_view(), name="media-category"),
    path("homepage/", HomepageAPIView.as_view(), name="homepage"),
    path("videos/", VideoView.as_view(), name="videos"),
    path("media/", MediaView.as_view(), name="media"),
    path("inspiration/", InspirationView.as_view(), name="inspiration"),
    path("kitchen/", KitchenView.as_view(), name="kitchen"),
    path("meta-data/<str:slug>/", MetaDataView.as_view(), name="meta-data"),
    path("parent-material/<int:id>/", ParentMaterialDetailView.as_view(), name="material"),
    path("material/<str:query>/", MaterialDetailView.as_view(), name="material"),
    path("material/", MaterialView.as_view(), name="material"),
    path("slug-verify/<slug:slug>/", ProductSlugVerifyView.as_view(), name="slug-verify"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
