from config import CONFIG
from searcher import Searcher


def main() -> None:
    searcher = Searcher(searches=CONFIG)
    searcher.start()


if __name__ == "__main__":
    main()
