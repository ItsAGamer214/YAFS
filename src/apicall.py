import requests
from typing import *

type Response = requests.models.Response

class AlphaV:
    
    baseURL = "https://www.alphavantage.co/query?"
    def __init__(self, key: str, params: dict):
        '''
        key is your key (do not push to github)
        params has to be a dict, why? just cuz
        '''
        self.key = key
        self.params = params
        self.response: Response = None

    def get(self,function:str):
        url = self.baseURL
        for x in self.params:
            match x:
                case "TIME_SERIES_INTRADAY":
                    url += "function=TIME_SERIES_INTRADAY"

    def __str__(self):
        if self.response is not None:
            return self.response.text[:30] + "\n..."
        else:
            return "None"
    def __repr__(self):
        return "AlphaV()"


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = [r.content]

with open("stokcshit", mode = "wb") as f:
    f.writelines(data)




