import requests
from requests import Response


def main():
    test_data: dict[str, str] = {
        "quote": "Test sitat"
    }

    url: str = "localhost:8000/quote"
    # res: Response = requests.get(url)
    res: Response = requests.post(url, json=test_data)
    data = res.json()

    return data

if __name__ == "__main__":
    print(main())