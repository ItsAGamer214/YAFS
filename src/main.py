import requests
import json
import pandas as pd
import yfinance as yf
import os

def main():

    with open("allstocks.txt",mode="r") as f:
        x = list(f)
        y = [b.split("\t")[1:3] for b in x]
        dictall = dict()
        for z in y:
            dictall[z[0]] = z[1]
    

    for x in dictall:
        print(x)
        if os.path.exists(f"./NASDAQ/{x}.txt"):
            continue
        try:
            ticker = yf.Ticker(x)
            df = ticker.history(period='200y')
            df.to_csv(f"./NASDAQ/{x}.txt")
        except:
            continue


if __name__ == "__main__":
    main()