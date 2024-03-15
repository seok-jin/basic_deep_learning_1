from datetime import datetime as dt

class DateConverter:
    @staticmethod
    def convert_to_datetime(date_string):
        # YYYYMMDD 형식인지 확인
        if len(date_string) == 8 and date_string.isdigit():
            year = int(date_string[0:4])
            month = int(date_string[4:6])
            day = int(date_string[6:8])
            return dt(year, month, day)
        
        # YYYY-MM-DD 형식인지 확인
        elif len(date_string) == 10 and date_string[4] == '-' and date_string[7] == '-':
            return dt.strptime(date_string, '%Y-%m-%d')
        
        else:
            raise ValueError("잘못된 날짜 형식입니다.")
    
    @staticmethod
    def convert_to_dash_format(date):
        # datetime 형식인 경우
        if isinstance(date, dt):
            return date.strftime('%Y-%m-%d')
        
        # 'YYYYMMDD' 형식인 경우
        elif isinstance(date, str) and len(date) == 8 and date.isdigit():
            return f"{date[:4]}-{date[4:6]}-{date[6:8]}"
        
        else:
            raise ValueError("잘못된 날짜 형식입니다.")
    
    @staticmethod
    def convert_to_yyyymmdd(date):
        # 'YYYY-MM-DD' 형식인 경우
        if isinstance(date, str) and len(date) == 10 and date[4] == '-' and date[7] == '-':
            return date[:4] + date[5:7] + date[8:10]
        
        # datetime 형식인 경우
        elif isinstance(date, dt):
            return date.strftime('%Y%m%d')
        
        else:
            raise ValueError("잘못된 날짜 형식입니다.")
        

class StockDay :
    def __init__(self) -> None:
        self.market_date

    def get_now_date():
        now_date = dt.now()
        return DateConverter.convert_to_yyyymmdd(now_date)
    
    def get_weekdays(date):
        return True if DateConverter.convert_to_datetime(date).weekday() <= 4 else False