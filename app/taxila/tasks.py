import threading
from config.utils import index_meilisearch_data


class IndexMaterialThread(threading.Thread):
    def __init__(self, **kwargs):
        super().__init__(name="Index Material Thread", **kwargs)

    def run(self):
        from taxila.models import Material

        data = list(
            Material.objects.filter(
                is_active=True,
                category__is_active=True,
                category__parent_category__is_active=True,
            ).values("id", "name", "slug", "category__name")
        )

        index_meilisearch_data(json_data=data, index_name="material")
