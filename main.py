import requests
import json

def main():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    r = requests.get(url)
    data = [r.content]

    with open("stokcshit", mode = "wb") as f:
        f.writelines(data)

if __name__ is "__main__":
    main()