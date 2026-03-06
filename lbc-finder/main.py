from searcher import Searcher
from config import CONFIG

def main() -> None:
    searcher = Searcher(searches=CONFIG)
    searcher.start()

if __name__ == "__main__":
    main()