from .logger import logger

from typing import List, Final
import os
import json

MAX_ID: Final[int] = 10_000

class ID:
    def __init__(self):
        self._ids: List[str] = self._get_ids()

    @property
    def ids(self) -> List[str]:
        return self._ids

    def _get_ids(self) -> List[str]:
        ids: List[str] = []
        if os.path.exists("id.json"):
            with open("id.json", "r") as f:
                try:
                    ids = json.load(f)
                except json.JSONDecodeError:
                    os.remove("id.json")
                except:
                    logger.exception("An error occurred while attempting to open the id.json file.")
        return ids

    def contains(self, id_: str) -> bool:
        return id_ in self._ids

    def add(self, id_: str) -> bool:
        if not id_ in self._ids:
            self._ids.append(id_)
            with open("id.json", "w") as f:
                json.dump(self._ids[-MAX_ID:], f, indent=3)
            self._ids = self._ids[-MAX_ID:]
            return True
        return False
