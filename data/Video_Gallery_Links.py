from taxila.models import VideoCategory, Video
import pandas

for index, item in enumerate(pandas.read_json("./Video Gallery Links.json").to_dict(orient="records")):
    print(index)
    category = VideoCategory.objects.get_or_create(name=item["CATEGORY"])[0]
    Video.objects.create(
        category=category,
        title=item["TITLE"],
        video_url=item["LINK"],
        company=item["COMPANY"],
    )
