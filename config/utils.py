from uuid import uuid4


def get_uuid_filename(filename: str) -> str:
    filename = filename.split('/')[-1]
    new_name = "{}-{}".format(uuid4().hex, filename)
    return new_name
