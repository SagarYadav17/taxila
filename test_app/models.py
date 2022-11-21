from django.db import models


class KitchenCategory(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Vendor(models.Model):
    name = models.CharField(max_length=255)


class Material(models.Model):
    slug = models.SlugField(max_length=255, blank=True, null=True)
    ranking = models.PositiveBigIntegerField(default=0)
    name = models.CharField(max_length=255)
    images = models.TextField(blank=True, null=True)
    origin_country = models.CharField(max_length=255, blank=True, null=True)
    level = models.PositiveBigIntegerField(default=0)
    care_instruction = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    finish = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.images}"


class Feature(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    chip = models.TextField(blank=True, null=True)
    heat = models.TextField(blank=True, null=True)
    stain = models.TextField(blank=True, null=True)
    scratch = models.TextField(blank=True, null=True)
    water = models.TextField(blank=True, null=True)
    frost = models.TextField(blank=True, null=True)


class Application(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    countertops = models.TextField(blank=True, null=True)
    floorings = models.TextField(blank=True, null=True)
    walls = models.TextField(blank=True, null=True)
    shower = models.TextField(blank=True, null=True)
    fireplace = models.TextField(blank=True, null=True)
    outdoor = models.TextField(blank=True, null=True)


class TechnicalSpecification(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    petrographic_denomination = models.TextField(blank=True, null=True)
    hardness = models.TextField(blank=True, null=True)
    water_absorption = models.TextField(blank=True, null=True)
    apparent_density = models.TextField(blank=True, null=True)
    open_porosity = models.TextField(blank=True, null=True)
    abrasion_strength = models.TextField(blank=True, null=True)
    compressive_strength = models.TextField(blank=True, null=True)
    attachement = models.TextField(blank=True, null=True)


class KitchenItem(models.Model):
    ranking = models.PositiveBigIntegerField(default=0)
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
    images = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.category.name}"
