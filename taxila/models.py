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


class ParentCategory(TimestampedModel):
    name = models.CharField(max_length=255)
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
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class MaterialVendor(TimestampedModel):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Material(TimestampedModel):
    slug = models.SlugField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    origin_country = models.CharField(max_length=255, blank=True, null=True)
    level = models.PositiveBigIntegerField(default=0)
    care_instruction = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    finish = models.TextField(blank=True, null=True)
    category = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE, blank=True, null=True)
    vendor = models.ForeignKey(MaterialVendor, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class MaterialImage(TimestampedModel):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    image = models.FileField(upload_to=upload_to_path)

    def __str__(self) -> str:
        return "%s - %s" % (self.item.name, self.id)


class MaterialFeature(TimestampedModel):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    chip = models.TextField(blank=True, null=True)
    heat = models.TextField(blank=True, null=True)
    stain = models.TextField(blank=True, null=True)
    scratch = models.TextField(blank=True, null=True)
    water = models.TextField(blank=True, null=True)
    frost = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.material.name


class MaterialApplication(TimestampedModel):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    countertops = models.TextField(blank=True, null=True)
    floorings = models.TextField(blank=True, null=True)
    walls = models.TextField(blank=True, null=True)
    shower = models.TextField(blank=True, null=True)
    fireplace = models.TextField(blank=True, null=True)
    outdoor = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.material.name


class MaterialTechnicalSpecification(TimestampedModel):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    petrographic_denomination = models.TextField(blank=True, null=True)
    hardness = models.TextField(blank=True, null=True)
    water_absorption = models.TextField(blank=True, null=True)
    apparent_density = models.TextField(blank=True, null=True)
    open_porosity = models.TextField(blank=True, null=True)
    abrasion_strength = models.TextField(blank=True, null=True)
    compressive_strength = models.TextField(blank=True, null=True)
    attachement = models.FileField(upload_to=upload_to_path)

    def __str__(self) -> str:
        return self.material.name


class KitchenItem(TimestampedModel):
    order = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(KitchenCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description_en = models.TextField(blank=True, null=True)
    description_it = models.TextField(blank=True, null=True)
    base_unit = models.TextField(blank=True, null=True)
    wall_unit = models.TextField(blank=True, null=True)
    tall_unit = models.TextField(blank=True, null=True)
    design_solution = models.TextField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)
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
