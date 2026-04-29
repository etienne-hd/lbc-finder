import lbc


def handle(ad: lbc.Ad, search_name: str):
    print(f"[{search_name}] New ads!")
    print(f"Title : {ad.subject}")
    print(f"Price : {ad.price} €")
    print(f"URL : {ad.url}")
    print("-" * 40)
