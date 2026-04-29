import lbc
import requests
from datetime import datetime

WEBHOOK_URL: str = ...


def handle(ad: lbc.Ad, search_name: str) -> None:
    timestamp = datetime.strptime(ad.index_date, "%Y-%m-%d %H:%M:%S").timestamp()

    payload = {
        "content": None,
        "embeds": [
            {
                "title": ad.title,
                "description": f"```{ad.body[:4087]}...```"
                if len(ad.body) >= 4090
                else f"```{ad.body[:4090]}```",
                "url": ad.url,
                "color": 14381568,
                "author": {"name": ad.user.name, "icon_url": ad.user.profile_picture},
                "image": {"url": ad.images[0] if ad.images else None},
                "fields": [
                    {
                        "name": "🕒 Publication",
                        "value": f"<t:{int(timestamp)}:R>",
                        "inline": True,
                    },
                    {"name": "💰 Price", "value": f"`{ad.price}€`", "inline": True},
                    {
                        "name": "📍 Location",
                        "value": f"`{ad.location.city_label}`",
                        "inline": True,
                    },
                ],
            }
        ],
        "username": search_name,
        "attachments": [],
    }

    response = requests.post(WEBHOOK_URL, json=payload)
    response.raise_for_status()
