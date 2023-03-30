# %%
from taxila.models import (
    Material,
    MaterialCategory,
    MaterialVendor,
    MaterialTechnicalSpecification,
    MaterialApplication,
    MaterialFeature,
    ParentCategory,
)
import pandas
import re


# %%
for index, item in enumerate(pandas.read_json("./granite.json").to_dict(orient="records")):
    try:
        level = re.findall("[0-9]+", item["LEVEL"])[0]
    except Exception:
        level = 0
    pc = ParentCategory.objects.get_or_create(name="name")[0]
    cagtegory_obj = MaterialCategory.objects.get_or_create(name=item["Category"], parent_category=pc)[0]

    if item["VENDOR"] is not None:
        vendor_obj = MaterialVendor.objects.get_or_create(name=item["VENDOR"])[0]
    else:
        vendor_obj = None
    material_obj = Material.objects.get_or_create(
        name=item["Material"],
        origin_country=item["COUNTRY_OF_ORIGIN"],
        level=level,
        care_instruction=item["CARE_INSTRUCTIONS"],
        meta_description=item["META_DESCRIPTION"],
        color=item["COLOR"],
        finish=item["FINISH"],
        category=cagtegory_obj,
        vendor=vendor_obj,
    )[0]
    material_obj.save()

    MaterialTechnicalSpecification.objects.get_or_create(
        material=material_obj,
        petrographic_denomination=item["TECHNICAL_SPECIFICATIONS"]["Petrographic_Denomination"],
        hardness=item["TECHNICAL_SPECIFICATIONS"]["Hardness"],
        water_absorption=item["TECHNICAL_SPECIFICATIONS"]["Water_Absorption"],
        apparent_density=item["TECHNICAL_SPECIFICATIONS"]["Apparent_Density"],
        open_porosity=item["TECHNICAL_SPECIFICATIONS"]["Open_Porosity"],
        abrasion_strength=item["TECHNICAL_SPECIFICATIONS"]["Abrasion_Strength"],
        compressive_strength=item["TECHNICAL_SPECIFICATIONS"]["Compressive_Strength"],
    )

    MaterialApplication.objects.get_or_create(
        material=material_obj,
        countertops=item["APPLICATIONS"]["Countertops"],
        floorings=item["APPLICATIONS"]["Floorings"],
        walls=item["APPLICATIONS"]["Walls"],
        shower=item["APPLICATIONS"]["Shower"],
        fireplace=item["APPLICATIONS"]["Fireplace"],
        outdoor=item["APPLICATIONS"]["Outdoor"],
    )

    MaterialFeature.objects.get_or_create(
        material=material_obj,
        chip=item["FEATURES"]["Chips"],
        heat=item["FEATURES"]["Heat"],
        stain=item["FEATURES"]["Stain"],
        scratch=item["FEATURES"]["Scratch"],
        water=item["FEATURES"]["Water"],
        frost=item["FEATURES"]["Frost"],
    )
