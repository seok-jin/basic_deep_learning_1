import sys, os 
sys.path.append(os.pardir)
from py_class.load_ticker_data import load_ticker_list

load_ticker_list.arange_ticker_list()
load_ticker_list.batch_ticker_list()