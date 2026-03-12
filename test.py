import requests
from requests import Response
from warnings import warn


def main():
    quote: str = input("Sitat: ")

    if not quote:
        warn("Sitat er tom. Default: Test")

    test_data: dict[str, str] = {
        "quote": quote or "Test"
    }

    url: str = "https://192.168.20.181:8000/sitat"
    # res: Response = requests.get(url)
    res: Response = requests.post(url, json=test_data)
    data = res.json()

    return data

if __name__ == "__main__":
    print(main())