from datetime import datetime as tmdt
from datetime import timedelta as dtmt
import time, sys, os
import pandas as pd 
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정

import logging
# external package
from pykrx import stock
from pykrx import bond

# user package
from py_class.date_convert import DateConverter,StockDay



def logging_text(text):
        logging.basicConfig(filename='./log/'+StockDay.get_now_date()+'.log', level=logging.INFO, encoding='euc-kr')    
        dt = tmdt.now()
        logging.info('time '+dt.strftime("%Y-%m-%dT%H:%M:%S")+' : '+text)

