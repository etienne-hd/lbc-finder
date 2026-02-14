import os
import tempfile

from model import Parameters, Search
from searcher.searcher import Searcher


class FakeAd:
    def __init__(self, ad_id: str):
        self.id = ad_id


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_flaky_handler_test() -> None:
    calls = {"count": 0}

    def flaky_handler(ad, search_name):
        calls["count"] += 1
        if calls["count"] < 3:
            raise RuntimeError("forced transient failure")

    search = Search(
        name="retry-flaky",
        parameters=Parameters(),
        delay=1,
        handler=flaky_handler,
    )
    searcher = Searcher(searches=[])
    searcher._HANDLER_INITIAL_BACKOFF = 0.0
    ad = FakeAd("ad-flaky")

    success = searcher._handle_with_retry(search, ad)
    if success:
        searcher._id.add(ad.id)

    _assert(success, "flaky handler should eventually succeed")
    _assert(calls["count"] == 3, f"expected 3 attempts, got {calls['count']}")
    _assert(searcher._id.contains(ad.id), "ad should be marked as seen after success")


def run_always_fail_handler_test() -> None:
    calls = {"count": 0}

    def always_fail(ad, search_name):
        calls["count"] += 1
        raise RuntimeError("forced permanent failure")

    search = Search(
        name="retry-fail",
        parameters=Parameters(),
        delay=1,
        handler=always_fail,
    )
    searcher = Searcher(searches=[])
    searcher._HANDLER_INITIAL_BACKOFF = 0.0
    ad = FakeAd("ad-fail")

    success = searcher._handle_with_retry(search, ad)
    if success:
        searcher._id.add(ad.id)

    _assert(not success, "always-fail handler should return False")
    _assert(
        calls["count"] == searcher._HANDLER_MAX_ATTEMPTS,
        f"expected {searcher._HANDLER_MAX_ATTEMPTS} attempts, got {calls['count']}",
    )
    _assert(not searcher._id.contains(ad.id), "ad should not be marked as seen on failure")


def main() -> None:
    cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        try:
            run_flaky_handler_test()
            run_always_fail_handler_test()
        finally:
            os.chdir(cwd)
    print("All retry tests passed.")


if __name__ == "__main__":
    main()
