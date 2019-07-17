from extractFinData import extractFinData
from extractSECFiling import extractSECFiling
from config import Config

quandl_key = Config.quandl_api_key
av_key = Config.av_api_key
sec_extractor = extractSECFiling
fin_extractor = extractFinData(quandl_key, av_key)
