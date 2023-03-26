from rest_framework import serializers
from taxila.models import (
    Inspiration,
    InspirationDetail,
    KitchenItem,
    KitchenItemImage,
    Material,
    MaterialApplication,
    MaterialFeature,
    MaterialImage,
    MaterialTechnicalSpecification,
    MetaData,
    Video,
)


class MaterialFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialFeature
        fields = "__all__"


class MaterialApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialApplication
        fields = "__all__"


class MaterialTechnicalSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialTechnicalSpecification
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    category = serializers.ReadOnlyField(source="category.name")
    vendor = serializers.ReadOnlyField(source="vendor.name")
    feature = serializers.SerializerMethodField()
    application = serializers.SerializerMethodField()
    technical_specification = serializers.SerializerMethodField()

    class Meta:
        model = Material
        fields = "__all__"

    def get_images(self, obj):
        return [item.image.url for item in MaterialImage.objects.filter(material_id=obj.id)]

    def get_feature(self, obj):
        try:
            queryset = MaterialFeature.objects.get(material_id=obj.id)
            return MaterialFeatureSerializer(queryset).data
        except MaterialFeature.DoesNotExist:
            return None

    def get_application(self, obj):
        try:
            queryset = MaterialFeature.objects.get(material_id=obj.id)
            return MaterialApplicationSerializer(queryset).data
        except MaterialFeature.DoesNotExist:
            return None

    def get_technical_specification(self, obj):
        try:
            queryset = MaterialTechnicalSpecification.objects.get(material_id=obj.id)
            return MaterialTechnicalSpecificationSerializer(queryset).data
        except MaterialTechnicalSpecification.DoesNotExist:
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
        fields = "__all__"


class InspirationSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")
    detail = serializers.SerializerMethodField()

    class Meta:
        model = Inspiration
        fields = "__all__"

    def get_detail(self, obj):
        try:
            queryset = InspirationDetail.objects.filter(inspiration_id=obj.id)
            return InspirationDetailSerializer(queryset, many=True).data
        except InspirationDetail.DoesNotExist:
            return None


class VideoSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Video
        fields = "__all__"
