from model import Search
from lbc import Client, Sort
from .id import ID
from .logger import logger

import time
import threading
from typing import List, Union

class Searcher:
    _HANDLER_MAX_ATTEMPTS: int = 3
    _HANDLER_INITIAL_BACKOFF: float = 2.0

    def __init__(self, searches: Union[List[Search], Search], request_verify: bool = True):
        self._searches: List[Search] = searches if isinstance(searches, list) else [searches]
        self._request_verify = request_verify
        self._id = ID()

    def _handle_with_retry(self, search: Search, ad) -> bool:
        for attempt in range(1, self._HANDLER_MAX_ATTEMPTS + 1):
            try:
                search.handler(ad, search.name)
                return True
            except Exception:
                if attempt == self._HANDLER_MAX_ATTEMPTS:
                    logger.exception(
                        f"[{search.name}] Handler failed for ad {ad.id} after {attempt} attempts."
                    )
                    return False

                delay = self._HANDLER_INITIAL_BACKOFF * (2 ** (attempt - 1))
                logger.warning(
                    f"[{search.name}] Handler failed for ad {ad.id}. "
                    f"Retrying in {delay:.0f}s ({attempt}/{self._HANDLER_MAX_ATTEMPTS})."
                )
                time.sleep(delay)
        return False

    def _search(self, search: Search) -> None:
        client = Client(proxy=search.proxy, request_verify=self._request_verify)
        while True:
            before = time.time()
            try:
                response = client.search(**search.parameters._kwargs, sort=Sort.NEWEST)
                logger.debug(f"Successfully found {response.total} ad{'s' if response.total > 1 else ''}.")
                ads = [ad for ad in response.ads if not self._id.contains(ad.id)]
                if len(ads):
                    logger.info(f"Successfully found {len(ads)} new ad{'s' if len(ads) > 1 else ''}!")

                notified = 0
                for ad in ads:
                    if self._handle_with_retry(search, ad) and self._id.add(ad.id):
                        notified += 1

                if len(ads) and notified != len(ads):
                    logger.warning(
                        f"[{search.name}] {len(ads) - notified} ad{'s were' if len(ads) - notified > 1 else ' was'} not marked as seen and will be retried."
                    )
            except Exception:
                logger.exception(f"An error occured.")
            time.sleep(search.delay - (time.time() - before) if search.delay - (time.time() - before) > 0 else 0)

    def start(self) -> bool:
        if not len(self._searches):
            logger.warning("No search rules have been set. Please create search rules in config.py (see example in README.md).")
            return False

        for search in self._searches:
            threading.Thread(target=self._search, args=(search,), name=search.name).start()
            time.sleep(5) # Add latency between each thread to prevent spam
        return True
