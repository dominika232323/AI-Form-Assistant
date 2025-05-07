import json


def read_json(file):
    if hasattr(file, 'read'):
        return json.load(file)
    else:
        with open(file, 'r') as f:
            return json.load(f)
        