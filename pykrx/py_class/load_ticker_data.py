import pandas as pd 

import sys,os
sys.path.append(os.pardir)
from py_class.date_convert import StockDay, DateConverter


# from pykrx import stock
# from pykrx import bond


from py_lib.krx_lib import *
# from py_class.load_ticker_data import load_ticker_list
# old= load_ticker_list()
# old_ticker = old.df_ticker

logging.basicConfig(filename='./log/'+StockDay.get_now_date()+'.log', level=logging.INFO)

ticker_dir = './data/ticker_list.csv'


class load_ticker_list:
    def __init__(self) -> None:
        if os.path.isfile(ticker_dir) :
            self.df_ticker = pd.read_csv(ticker_dir,index_col=0 )
        else:
            tickers = stock.get_market_ticker_list(market='KOSPI')
            # print(tickers)
            # tickers = np.array(tickers)
            data = { 
                "ticker" : tickers
            }
            df_tickers = pd.DataFrame(data)
            # tickers_len = tickers.shape[0]
            ticker_name = []
            insert_dt = []
            comment = []
            append_dt = DateConverter.convert_to_dash_format(StockDay.get_now_date())
            for i in range(len(data["ticker"])):
                ticker_name.append(stock.get_market_ticker_name(data["ticker"][i]))
                insert_dt.append(append_dt)
                comment.append('-')
    
            df_tickers.insert(1,"ticker_name",ticker_name,True)
            df_tickers.insert(2,"comment",comment,True)
            df_tickers.insert(3,"insert_dt",insert_dt,True)
            df_tickers.insert(4,"update_dt",insert_dt,True)
            df_tickers.to_csv(ticker_dir)
 
            self.df_ticker = df_tickers

    def batch_ticker_list(self):
        old_ticker = self.df_ticker
        tickers = stock.get_market_ticker_list(market='KOSPI')
        # print(tickers)
        # tickers = np.array(tickers)
        data = { 
            "ticker" : tickers
        }
        new_tickers = pd.DataFrame(data)
        # tickers_len = tickers.shape[0]
        ticker_name = []

        for i in range(len(data["ticker"])):
            ticker_name.append(stock.get_market_ticker_name(data["ticker"][i]))

        new_tickers.insert(1,"ticker_name",ticker_name,True)
        # new_tickers.to_csv(ticker_dir)
        changes  = new_tickers[new_tickers['ticker'].isin(old_ticker['ticker'])]
        changes = changes[changes['ticker_name'] != old_ticker['ticker_name']]

        # old_ticker[old_ticker['ticker']=='001045',ticker_name] = 'CJ대한통운'
        old_ticker.loc[old_ticker['ticker'].isin(changes['ticker']),'comment'] = old_ticker['ticker_name']+' -> '+changes['ticker_name']
        old_ticker.loc[old_ticker['ticker'].isin(changes['ticker']),'ticker_name'] = changes['ticker_name']
        old_ticker.loc[old_ticker['ticker'].isin(changes['ticker']),'update_dt'] = DateConverter.convert_to_dash_format(StockDay.get_now_date())

        ticker_dir = './data/ticker_list.csv'
        logging.info('batch_ticker_list 함수가 실행되었습니다.')
        old_ticker.to_csv(ticker_dir)
        self.df_ticker = old_ticker


    


def get_market_ohlcv_to_csv(sdt,edt,ticker): 
    if os.path.isfile("./data/"+ticker+".csv"):
        # 기존에 있는 파일 
        if get_last_ticker_date(edt,ticker):
            print("종료")
        else:
            df = stock.get_market_ohlcv(edt,edt,ticker)
            df.to_csv("./data/"+ticker+".csv",mode='a', header=False)
    else: #신규
        df = stock.get_market_ohlcv(sdt,edt,ticker)
        df.to_csv("./data/"+ticker+".csv", header=True)
    
def get_last_ticker_date(edt,ticker):
    df_asis = pd.read_csv("./data/"+ticker+".csv")
    if df_asis.iloc[-1]['날짜'].replace('-','') == edt:
        return True
    else : 
        return False
    del df_asis

# df = stock.get_market_ohlcv("19000101", "20240314", "079980")