from uuid import uuid4
from contextlib import suppress
import meilisearch
from meilisearch.errors import MeilisearchApiError
from config._env import MEILISEARCH_URL


def get_uuid_filename(filename: str) -> str:
    filename = filename.split("/")[-1]
    new_name = "{}-{}".format(uuid4().hex, filename)
    return new_name


def index_meilisearch_data(json_data: dict, index_name: str):
    client = meilisearch.Client(MEILISEARCH_URL)
    with suppress(MeilisearchApiError):
        client.index(index_name).update_documents(json_data)


def search_meilisearch(index_name: str, query: str):
    client = meilisearch.Client(MEILISEARCH_URL)
    return client.index(index_name).search(query)
