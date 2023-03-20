# %%
from taxila.models import InspirationCategory, Inspiration
import pandas

# %%
for index, item in enumerate(pandas.read_json("./InspirationData.json").to_dict(orient="records")):
    category = InspirationCategory.objects.get_or_create(name=item["Category"])[0]
    Inspiration.objects.get_or_create(
        title=item["title"],
        description=item["Description"],
        category=category,
    )
