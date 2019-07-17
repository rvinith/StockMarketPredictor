import numpy as np
import pandas as pd
from config import Config
from tqdm import tqdm
import requests
import io
from time import sleep
import pickle

list_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
table = pd.read_html(list_url, header = [0], index_col = 0)[0]
stock_tickers = table.index.drop_duplicates().values
ticker_list = dict()

# alphavantage is for retrieving historical financial data
av_url = "https://www.alphavantage.co/query?"
# alphavantage key
key = Config.av_api_key
parameters = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "datatype" : "csv",
    "outputsize" : "full",
    "apikey" : key
}

for ticker in tqdm(stock_tickers):
    parameters["symbol"] = ticker
    data = requests.get(av_url, parameters)
    filepath = io.StringIO(data.content.decode('utf-8'))
    ticker_list[ticker] = pd.read_csv(filepath, parse_dates = True, index_col = [0], error_bad_lines = False)

fin_data = pd.concat(ticker_list)
fin_data.to_pickle("fin_data.pkl")
fin_data.to_csv("fin_data.csv", chunksize = 50)