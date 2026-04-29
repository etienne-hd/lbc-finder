from .logger import logger

import os
import json

MAX_ID: int = 10_000


class ID:
    def __init__(self):
        self._ids: list[str] = self._get_ids()

    @property
    def ids(self) -> list[str]:
        return self._ids

    def _get_ids(self) -> list[str]:
        ids: list[str] = []
        id_path = os.path.join("data", "id.json")
        if os.path.exists(id_path):
            with open(id_path, "r") as f:
                try:
                    ids = json.load(f)
                except json.JSONDecodeError:
                    os.remove(id_path)
                except Exception:
                    logger.exception(
                        "An error occurred while attempting to open the id.json file."
                    )
        return ids

    def contains(self, id_: str) -> bool:
        return id_ in self._ids

    def add(self, id_: str) -> bool:
        id_path = os.path.join("data", "id.json")
        if id_ not in self._ids:
            self._ids.append(id_)
            with open(id_path, "w") as f:
                json.dump(self._ids[-MAX_ID:], f, indent=3)
            self._ids = self._ids[-MAX_ID:]
            return True
        return False
