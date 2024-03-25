import sys, os 
sys.path.append(os.pardir)
from py_class.load_ticker_data import load_ticker_list
list_ticker = load_ticker_list()
list_ticker.arange_ticker_list()
list_ticker.batch_ticker_list()