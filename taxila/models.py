from django.db import models
from django.core.cache import cache

from config.utils import get_uuid_filename


def upload_to_path(instance, filename):
    new_filename = get_uuid_filename(filename=filename)
    return f"{instance._meta.app_label}/{instance._meta.model_name}/{new_filename}"


class TimestampedModel(models.Model):
    ranking = models.PositiveBigIntegerField(default=0)

    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("ranking",)

    def save(self, *args, **kwargs) -> None:
        cache.clear()
        return super().save(*args, **kwargs)


class HomepageBanner(TimestampedModel):
    BANNER_TYPES = (
        ("desktop", "desktop"),
        ("mobile", "mobile"),
    )
    banner_type = models.CharField(max_length=20, choices=BANNER_TYPES)
    image = models.FileField(upload_to=upload_to_path)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "%s - %s - %s" % (self.id, self.banner_type, self.image)


class ParentCategory(TimestampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class MetaData(TimestampedModel):
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    og_title = models.CharField(max_length=255, blank=True, null=True)
    twitter_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)
    twitter_description = models.TextField(blank=True, null=True)
    script = models.JSONField(default=dict)

    def __str__(self) -> str:
        return self.slug


class KitchenCategory(TimestampedModel):
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class MaterialCategory(TimestampedModel):
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    banner_image = models.FileField(upload_to=upload_to_path, blank=True, null=True)
    sub_image = models.FileField(upload_to=upload_to_path, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    feature_chip = models.PositiveIntegerField(default=0)
    feature_heat = models.PositiveIntegerField(default=0)
    feature_stain = models.PositiveIntegerField(default=0)
    feature_scratch = models.PositiveIntegerField(default=0)
    feature_water = models.PositiveIntegerField(default=0)
    feature_frost = models.PositiveIntegerField(default=0)
    pros = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class MaterialVendor(TimestampedModel):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Material(TimestampedModel):
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    main_image = models.FileField(upload_to=upload_to_path, blank=True, null=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE, blank=True, null=True)
    origin_country = models.CharField(max_length=255, blank=True, null=True)
    level = models.PositiveBigIntegerField(default=0)
    care_instruction = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    finish = models.TextField(blank=True, null=True)
    vendor = models.ForeignKey(MaterialVendor, on_delete=models.CASCADE, blank=True, null=True)

    # Applications
    application_countertops = models.BooleanField(default=False)
    application_floorings = models.BooleanField(default=False)
    application_walls = models.BooleanField(default=False)
    application_shower = models.BooleanField(default=False)
    application_fireplace = models.BooleanField(default=False)
    application_outdoor = models.BooleanField(default=False)

    # Technical Specification
    technical_specification_petrographic_denomination = models.TextField(blank=True, null=True)
    technical_specification_hardness = models.TextField(blank=True, null=True)
    technical_specification_water_absorption = models.TextField(blank=True, null=True)
    technical_specification_apparent_density = models.TextField(blank=True, null=True)
    technical_specification_open_porosity = models.TextField(blank=True, null=True)
    technical_specification_abrasion_strength = models.TextField(blank=True, null=True)
    technical_specification_compressive_strength = models.TextField(blank=True, null=True)
    technical_specification_attachement = models.FileField(upload_to=upload_to_path)

    def __str__(self) -> str:
        return self.name


class MaterialImage(TimestampedModel):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    image = models.FileField(upload_to=upload_to_path)

    def __str__(self) -> str:
        return "%s - %s" % (self.item.name, self.id)


class KitchenItem(TimestampedModel):
    order = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    category = models.ForeignKey(KitchenCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description_en = models.TextField(blank=True, null=True)
    description_it = models.TextField(blank=True, null=True)
    base_unit = models.TextField(blank=True, null=True)
    wall_unit = models.TextField(blank=True, null=True)
    tall_unit = models.TextField(blank=True, null=True)
    design_solution = models.TextField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)

    wall_unit_with_grip_recessed = models.BooleanField(default=False)
    wall_unit_with_handle = models.BooleanField(default=False)
    tall_unit_with_grip_recessed = models.BooleanField(default=False)
    tall_unit_with_handle = models.BooleanField(default=False)
    modular_base_unit = models.BooleanField(default=False)
    living_room_base_unit = models.BooleanField(default=False)
    tall_corner_walk_pantry = models.BooleanField(default=False)
    tall_unit_with_extended_door = models.BooleanField(default=False)
    hole_tall_unit = models.BooleanField(default=False)
    modular_wall_unit = models.BooleanField(default=False)
    living_and_open_box_unit = models.BooleanField(default=False)
    sliding_counter = models.BooleanField(default=False)
    boiserie = models.BooleanField(default=False)
    glass_unit = models.BooleanField(default=False)
    custom_on_request = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.category.name)


class KitchenItemImage(TimestampedModel):
    item = models.ForeignKey(KitchenItem, on_delete=models.CASCADE)
    image = models.FileField(upload_to=upload_to_path)

    def __str__(self) -> str:
        return "%s - %s" % (self.item.name, self.id)


class InspirationCategory(TimestampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Inspiration(TimestampedModel):
    category = models.ForeignKey(InspirationCategory, on_delete=models.CASCADE)
    main_image = models.FileField(upload_to=upload_to_path)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "%s - %s - %s" % (self.id, self.category.name, self.title)


class InspirationDetail(TimestampedModel):
    inspiration = models.ForeignKey(Inspiration, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to=upload_to_path)

    def __str__(self) -> str:
        return "%s - %s" % (self.inspiration.title, self.title)


class VideoCategory(TimestampedModel):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Video(TimestampedModel):
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.URLField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "%s - %s" % (self.title, self.category.name)


class MediaCategory(TimestampedModel):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Media(TimestampedModel):
    category = models.ForeignKey(MediaCategory, on_delete=models.CASCADE)
    image = models.FileField(upload_to=upload_to_path)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=255)
    source = models.CharField(max_length=255, blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "%s - %s - %s" % (self.title, self.category.name, self.publish_date)
