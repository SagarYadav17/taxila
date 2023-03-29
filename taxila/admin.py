from django.contrib import admin
from taxila.models import (
    HomepageBanner,
    InspirationDetail,
    MaterialCategory,
    KitchenCategory,
    KitchenItem,
    Material,
    MaterialVendor,
    MaterialImage,
    KitchenItemImage,
    Media,
    MediaCategory,
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
    search_fields = ("material__name",)


@admin.register(KitchenItem)
class KitchenItemAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "name", "is_active")
    list_filter = ("is_active",)


@admin.register(KitchenItemImage)
class KitchenItemImageAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "item")
    search_fields = ("item__name",)


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


@admin.register(InspirationDetail)
class InspirationDetailAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "inspiration", "title")
    search_fields = ("title",)


@admin.register(HomepageBanner)
class HomepageBannerAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "banner_type", "is_active")
    search_fields = ("is_active", "banner_type")


@admin.register(MediaCategory)
class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    search_fields = ("name",)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking", "title", "category", "is_active")
    search_fields = ("title",)
    list_filter = ("is_active", "category")
