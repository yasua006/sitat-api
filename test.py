import requests
from requests import Response


def main():
    url: str = "https:localhost:8000/quote"
    res: Response = requests.get(url)
    data = res.json()

    return data

if __name__ == "__main__":
    print(main())