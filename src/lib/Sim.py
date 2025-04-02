import pandas as pd
"""
    Steps to run a Sim
    
"""
class Sim:

    def __init__(self,path,hist_offset = 0,):
        self.df = []
        self._parse_data(self,path)
        pass

    def _parse_data(self,path):
        pass

    def step(self, time):
        pass