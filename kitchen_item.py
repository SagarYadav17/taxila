from taxila.models import (
    KitchenItem,
    ParentCategory,
    KitchenCategory,
)
import pandas

pc = ParentCategory.objects.get_or_create(name="default")[0]
category = KitchenCategory.objects.get_or_create(parent_category=pc, name="Minotticucine")[0]

for index, item in enumerate(pandas.read_json("./kitchen_item.json").to_dict(orient="records")):
    print(index)
    KitchenItem.objects.create(
        category=category,
        name=item["RANGE"],
        description_en=item["DESCRIPTION_ENGLISH"],
        description_it=item["DESCRIPTION_ITALIAN"],
    )
