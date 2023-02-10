

from typing import Dict
import json

def load_config(path: str) -> Dict:
    with open(path) as file:
        return json.load(file)