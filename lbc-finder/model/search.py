from lbc import Proxy, Ad
from .parameters import Parameters
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass
class Search:
    name: str
    parameters: Parameters
    delay: float
    handler: Callable[[Ad, str], None]
    proxy: Optional[Proxy] = None