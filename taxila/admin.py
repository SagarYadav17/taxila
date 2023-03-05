from django.contrib import admin
from taxila.models import (
    MaterialApplication,
    MaterialCategory,
    MaterialFeature,
    KitchenCategory,
    KitchenItem,
    Material,
    MaterialTechnicalSpecification,
    MaterialVendor,
    MaterialImage,
    KitchenItemImage,
    MetaData,
    ParentCategory,
    Inspiration,
    InspirationCategory,
    Video,
    VideoCategory,
)


@admin.register(KitchenCategory)
class KitchenCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    list_filter = ("is_active",)


@admin.register(MaterialCategory)
class MaterialCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    list_filter = ("is_active",)


@admin.register(MaterialVendor)
class MaterialVendorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    list_filter = ("is_active",)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "name", "is_active")
    list_filter = ("is_active",)


@admin.register(MaterialImage)
class MaterialImageAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "material")
    search_fields = ("item",)


@admin.register(MaterialFeature)
class MaterialFeatureAdmin(admin.ModelAdmin):
    list_display = ("id", "material")
    search_fields = ("item",)


@admin.register(MaterialApplication)
class MaterialApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "material")
    search_fields = ("item",)


@admin.register(MaterialTechnicalSpecification)
class MaterialTechnicalSpecificationAdmin(admin.ModelAdmin):
    list_display = ("id", "material")
    search_fields = ("item",)


@admin.register(KitchenItem)
class KitchenItemAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "name", "is_active")
    list_filter = ("is_active",)


@admin.register(KitchenItemImage)
class KitchenItemImageAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "item")
    search_fields = ("item",)


@admin.register(ParentCategory)
class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "name", "is_active")
    search_fields = ("name",)


@admin.register(MetaData)
class MetaDataAdmin(admin.ModelAdmin):
    list_display = ("id", "slug")
    search_fields = ("slug", "title")


@admin.register(InspirationCategory)
class InspirationCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    search_fields = ("name",)


@admin.register(Inspiration)
class InspirationAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "category", "title", "is_active")
    search_fields = ("tite",)
    list_filter = ("is_active", "category")


@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    search_fields = ("name",)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "category", "video_url", "is_active")
    search_fields = ("video_url",)
    list_filter = ("is_active", "category")
