import requests
import json
import pandas as pd
import yfinance as yf
import os

def main():
    with open("nasdaqstocks.txt",mode="r") as f:
        x = list(f)
        y = [b.split("\t")[1:3] for b in x]
        rankedbymarketcap = dict()
        for z in y:
            rankedbymarketcap[z[0]] = z[1]


    #This is the code to download the data from yfinance
    # for x in rankedbymarketcap:
    #     print(x)
    #     if os.path.exists(f"./NASDAQ/{x}.txt"):
    #         continue
    #     try:
    #         ticker = yf.Ticker(x)
    #         df = ticker.history(period='200y')
    #         df.to_csv(f"./NASDAQ/{x}.txt")
    #     except:
    #         continue



if __name__ == "__main__":
    main()
