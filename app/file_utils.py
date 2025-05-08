import json
from typing import Union, IO


def read_json(file_path: Union[str, IO]) -> dict:
    if hasattr(file_path, 'read'):
        return json.load(file_path)
    else:
        with open(file_path, 'r') as f:
            return json.load(f)
