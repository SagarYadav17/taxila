from rest_framework import serializers
from taxila.models import (
    Inspiration,
    InspirationDetail,
    KitchenItem,
    KitchenItemImage,
    Material,
    MaterialCategory,
    MaterialImage,
    Media,
    MetaData,
    ParentCategory,
    StaticContent,
    Team,
    Video,
)


class MaterialCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialCategory
        fields = "__all__"


class MaterialShortDetailSerializer(serializers.ModelSerializer):
    category__name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Material
        fields = ("id", "slug", "name", "main_image", "category_id", "category__name")


class ParentMaterialDetailSerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    meta_data = serializers.SerializerMethodField()

    class Meta:
        model = ParentCategory
        fields = "__all__"

    def get_sub_categories(self, obj):
        queryset = MaterialCategory.objects.filter(parent_category_id=obj.id)
        return MaterialCategorySerializer(queryset, many=True).data

    def get_products(self, obj):
        queryset = Material.objects.filter(category__parent_category_id=obj.id)
        return MaterialShortDetailSerializer(queryset, many=True).data

    def get_meta_data(self, obj):
        try:
            queryset = MetaData.objects.get(slug=obj.slug)
            return MetaDataSerializer(queryset).data
        except MetaData.DoesNotExist:
            return None


class MaterialCategoryDetailSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    parent_category_name = serializers.ReadOnlyField(source="parent_category.name")

    class Meta:
        model = MaterialCategory
        fields = "__all__"

    def get_products(self, obj):
        queryset = Material.objects.filter(category_id=obj.id)
        return MaterialShortDetailSerializer(queryset, many=True).data


class MaterialDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    catergory_name = serializers.ReadOnlyField(source="category.name")
    parent_category_name = serializers.ReadOnlyField(source="category.parent_category.name")
    category_banner_image = serializers.ImageField(source="category.banner_image", read_only=True)
    meta_data = serializers.SerializerMethodField()

    class Meta:
        model = Material
        fields = "__all__"

    def get_images(self, obj):
        return [item.image.url for item in MaterialImage.objects.filter(material_id=obj.id)]

    def get_meta_data(self, obj):
        try:
            queryset = MetaData.objects.get(slug=obj.slug)
            return MetaDataSerializer(queryset).data
        except MetaData.DoesNotExist:
            return None


class KitchenItemSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    category = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = KitchenItem
        fields = "__all__"

    def get_images(self, obj) -> list:
        return [item.image.url for item in KitchenItemImage.objects.filter(item_id=obj.id)]


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        fields = "__all__"


class InspirationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspirationDetail
        fields = ("id", "title", "image")
        read_only_fields = ("id", "title", "image")


class InspirationSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")
    detail = serializers.SerializerMethodField()

    class Meta:
        model = Inspiration
        fields = "__all__"

    def get_detail(self, obj):
        return InspirationDetailSerializer(InspirationDetail.objects.filter(inspiration_id=obj.id), many=True).data


class VideoSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Video
        fields = "__all__"


class MediaSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Media
        fields = ("id", "category", "image", "title", "url", "source", "publish_date", "category_name")
        read_only_fields = fields


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name", "designation", "linkedin", "mail", "phone_number", "profile")
        read_only_fields = fields


class StaticContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticContent
        fields = ("id", "title", "file")
        read_only_fields = fields
