import pandas as pd
from processor import Processor
from fetcher import Dal

class Manager:
    def __init__(self):
        self.dal = Dal()
        self.processor = Processor()
        self.df = None

    def get_data(self):
        self.df = pd.DataFrame(self.dal.get_tweets())
        return self.processor.process(self.df)

m = Manager()
print(m.get_data())