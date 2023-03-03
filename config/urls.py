from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from taxila.views import (
    KitchenCategoryListView,
    KitchenItemListView,
    MaterialCategoryListView,
    MaterialListView,
    MaterialVendorListView,
)

admin.site.site_header = "Taxila Stone Administration"
admin.site.index_title = "Taxila Stone"
admin.site.site_title = "Administration"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django_prometheus.urls")),
    path("kitchen-category/", KitchenCategoryListView.as_view(), name="kitchen-category"),
    path("material-category/", MaterialCategoryListView.as_view(), name="material-category"),
    path("material-vendor/", MaterialVendorListView.as_view(), name="material-vendor"),
    path("material/", MaterialListView.as_view(), name="material"),
    path("kitchen/", KitchenItemListView.as_view(), name="kitchen"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
