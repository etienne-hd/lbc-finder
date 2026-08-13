from collections.abc import Callable
from dataclasses import dataclass

from lbc import Ad, Proxy

from .parameters import Parameters


@dataclass
class Search:
    name: str
    parameters: Parameters
    delay: float
    handler: Callable[[Ad, str], None]
    proxy: Proxy | None = None
