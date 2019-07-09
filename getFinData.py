import numpy as np
import pandas as pd

listURL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
table = pd.read_html(listURL, header = [0], index_col = 0)[0]
stockTickers = table.index.drop_duplicates().values