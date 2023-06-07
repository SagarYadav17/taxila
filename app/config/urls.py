from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from taxila.views import (
    BannerImagesView,
    HomeView,
    HomepageAPIView,
    InspirationView,
    KitchenCategoryView,
    KitchenView,
    MaterialCategoryDetailView,
    MediaCategoryView,
    MediaView,
    ParentMaterialDetailView,
    MaterialCategoryView,
    MaterialDetailView,
    MetaDataView,
    ProductSlugVerifyView,
    StaticContentListView,
    TeamsListView,
    VideoCategoryView,
    VideoView,
    InspirationCategoryView,
    MaterialView,
    MaterialSearchView,
)

admin.site.site_header = "Taxila Stone Administration"
admin.site.index_title = "Taxila Stone"
admin.site.site_title = "Administration"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django_prometheus.urls")),
    path("", HomeView.as_view(), name="home"),
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
    path("meta-data/<slug:slug>/", MetaDataView.as_view(), name="meta-data"),
    path("parent-material/<int:id>/", ParentMaterialDetailView.as_view(), name="parent-material"),
    path("material/<str:query>/", MaterialDetailView.as_view(), name="material-detail"),
    path(
        "material-category-detail/<str:query>/", MaterialCategoryDetailView.as_view(), name="material-category-detail"
    ),
    path("material/", MaterialView.as_view(), name="material"),
    path("slug-verify/<slug:slug>/", ProductSlugVerifyView.as_view(), name="slug-verify"),
    path("teams/", TeamsListView.as_view(), name="teams"),
    path("static-content/", StaticContentListView.as_view(), name="static-content"),
    path("material-search/<str:query>/", MaterialSearchView.as_view(), name="material-search"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
