from pathlib import Path
import game.config as gc
import json


def logs_to_dict() -> dict[str: dict]:
    temp: dict = {}
    for file in Path(gc.LOGS_DIR).glob('*.json'):
        with open(file, 'r') as f:
            temp[file.stem] = json.load(f)
    return temp
