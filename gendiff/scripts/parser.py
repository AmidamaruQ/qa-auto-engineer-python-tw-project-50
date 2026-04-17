from os import PathLike
import json

import yaml


def parse_file(filepath):
    path = str(filepath) if isinstance(filepath, PathLike) else filepath

    with open(path) as f:
        if path.endswith(('.yaml', '.yml')):
            return yaml.safe_load(f)
        elif path.endswith('.json'):
            return json.load(f)
        raise ValueError(f'Unsupported file format: {path}')
