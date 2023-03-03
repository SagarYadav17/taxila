from enum import Enum, auto
from django.core.cache import cache


class ExtendedEnum(Enum):
    @classmethod
    def list_value(cls):
        return [item.value for item in cls]

    @classmethod
    def list_name(cls):
        return [item.name for item in cls]


class CacheKeys(ExtendedEnum):
    homepage = auto()
    kitchen_category = auto()
    material_category = auto()
    material_vendor = auto()
    material = auto()
    kitchen_item = auto()
    inspiration = auto()


def delete_all_cache():
    cache.adelete_many(CacheKeys.list_value())
    return True
