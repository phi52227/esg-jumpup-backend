import requests
import random


def main():
    response = requests.get("http://www.google.com/random-address")
    # print("Status Code: ", response.status_code)
    # print(response.headers.get("Content-Type"))
    print(response.text)
    print(response.url)


if __name__ == "__main__":
    main()
