# lbc-finder
[![GitHub license](https://img.shields.io/github/license/etienne-hd/lbc?style=for-the-badge)](https://github.com/etienne-hd/lbc/blob/master/LICENSE)

**Stay notified when new ads appear on Leboncoin**

```python
from model import Search, Parameters
import lbc

def handle(ad: lbc.Ad, search_name: str):
    print(f"[{search_name}] New ads!")
    print(f"Title : {ad.subject}")
    print(f"Price : {ad.price} €")
    print(f"URL : {ad.url}")
    print("-" * 40)

location = lbc.City( 
    lat=48.85994982004764,
    lng=2.33801967847424,
    radius=10_000, # 10 km
    city="Paris"
)

CONFIG = [
    Search(
        name="Location Paris",
        parameters=Parameters(
            text="maison",
            locations=[location],
            category=lbc.Category.IMMOBILIER,
            square=[200, 400],
            price=[300_000, 700_000]
        ),
        delay=60 * 5, # Check every 5 minutes 
        handler=handle
    ),
    ... # More
]
```
*lbc-finder is not affiliated with, endorsed by, or in any way associated with Leboncoin or its services. Use at your own risk.*

This project uses [lbc](https://github.com/etienne-hd/lbc), an unofficial library to interact with Leboncoin API.

## Features
* Advanced Search (text, category, price, location, square, etc.)
* Proxy Support for anonymity and bypassing rate limits
* Custom Logger with log file
* Configurable search interval (delay)
* Handler function triggered on new ads for full customization
* Multiple simultaneous searches with threading
* Easy integration with notifications (Discord, Telegram, email…) via handler

## Installation

Required **Python 3.9+**
1. **Clone the repository**
    ```bash
    git clone https://github.com/etienne-hd/lbc-finder.git
    cd lbc-finder
    ```
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Docker

You can run **lbc-finder** using Docker without installing Python locally.

### Pull the image

The easiest way is to use the prebuilt image from Docker Hub:

```bash
docker pull etiennehode/lbc-finder:latest
```

### Build locally

If you prefer to build the image yourself:

```bash
docker build -t lbc-finder .
```

### Run the container

```bash
docker run -d \
  --name lbc-finder \
  -v lbc_data:/app/data \
  -v $(pwd)/config.py:/app/config.py \
  etiennehode/lbc-finder:latest
```

### Volumes

Two volumes are used:

| Volume           | Description                         |
| ---------------- | ----------------------------------- |
| `/app/config.py` | Your search configuration file      |
| `/app/data`      | Persistent storage for detected ads |

Example:

```bash
-v $(pwd)/config.py:/app/config.py
```

This mounts your local `config.py` file into the container so you can easily edit your searches without rebuilding the image.

## Configuration
A [config.py](config.py) file is provided by default in the project, it contains a basic configuration.

Inside this file, you must define a `CONFIG` variable, which is an list of `Search` objects.

Each `Search` object should be configured with the rules for the ads you want to track.

For example, if you want to track ads for a **Porsche 944** priced between 0€ and 25,000€ anywhere in France:
```python
from model import Search, Parameters

Search(
    name="Porsche 944",
    parameters=Parameters(
        text="Porsche 944",
        category=lbc.Category.VEHICULES_VOITURES,
        price=[0, 25_000]
    ),
    delay=60 * 5, # Every 5 minutes
    handler=handle,
    proxy=None
)
```
### Name
A descriptive label for the Search.

It has no impact on the actual query, it’s only used to identify the search.

### Parameters

All available parameters are documented in the [lbc](https://github.com/etienne-hd/lbc) repository.

### Delay

The time interval between each search.

### Handler

This function is called whenever a new ad appears.
It must accept two parameters:

* the `Ad` object
* the name (label) of the search (e.g. **"Porsche 944"**)

```python
def handle(ad: lbc.Ad, search_name: str) -> None:
    ...
```
You can find example handlers in the [examples](examples/) folder.

### Proxy

You can configure a proxy, here is an example:

```python
from lbc import Proxy
from model import Search

proxy = Proxy(
    host="127.0.0.1",
    port=9444,
    username="etienne",
    password="123456"
)

Search(
    name=...,
    parameters=...,
    delay=...,
    handler=...,
    proxy=proxy
)
```

## Usage
To run **lbc-finder**, simply start the `main.py` file:
```bash
python main.py
```

## License

This project is licensed under the MIT License.

## Support

<a href="https://www.buymeacoffee.com/etienneh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

You can reach out to me on [Telegram](https://t.me/etienne_hd) or [Discord](https://discord.com/users/1153975318990827552) if you're looking for custom scraping services.