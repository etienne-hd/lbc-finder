from model import Search, Parameters
import lbc

from .handler import handle

location = lbc.City(
    lat=48.85994982004764,
    lng=2.33801967847424,
    radius=10_000,  # 10 km
    city="Paris",
)

CONFIG = [
    Search(
        name="Location Paris",
        parameters=Parameters(
            text="maison",
            locations=[location],
            category=lbc.Category.IMMOBILIER,
            square=[200, 400],
            price=[300_000, 700_000],
        ),
        delay=60 * 5,  # Check every 5 minutes
        handler=handle,
    ),
]
