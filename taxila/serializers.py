from rest_framework import serializers
from taxila.models import (
    KitchenCategory,
    KitchenItem,
    KitchenItemImage,
    Material,
    MaterialApplication,
    MaterialCategory,
    MaterialFeature,
    MaterialImage,
    MaterialTechnicalSpecification,
    MaterialVendor,
)


class KitchenCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenCategory
        fields = "__all__"


class MaterialCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialCategory
        fields = "__all__"


class MaterialVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialVendor
        fields = "__all__"


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
    category = serializers.CharField(source="category.name")
    vendor = serializers.CharField(source="vendor.name")
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
            return MaterialFeatureSerializer(queryset).data
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
    category = serializers.CharField(source="category.name")

    class Meta:
        model = KitchenItem
        fields = "__all__"

    def get_images(self, obj):
        return [item.image.url for item in KitchenItemImage.objects.filter(item=obj)]
