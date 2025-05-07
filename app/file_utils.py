import json



def read_json(file_path):
    if hasattr(file_path, 'read'):
        return json.load(file_path)
    else:
        with open(file_path, 'r') as f:
            return json.load(f)
