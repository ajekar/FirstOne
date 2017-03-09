import wget
# wget.download('http://www.bseindia.com/download/BhavCopy/Equity/EQ220217_CSV.ZIP','D:\Stocks\EQ220217_CSV.ZIP')


import pandas as pd
from datetime import date
start_date = date(2010, 1, 1)
end_date = date(2015, 12, 31)
daterange = pd.date_range(start_date, end_date)
for single_date in daterange:
    if single_date.weekday() not in (5, 6):
        file_name = "EQ" + single_date.strftime("%d%m%y") + "_CSV.ZIP"
        print (single_date.strftime("%y-%m-%d"), single_date.weekday())
        try:
            wget.download('http://www.bseindia.com/download/BhavCopy/Equity/' + file_name,'D:\Stocks\\' + file_name)
        except:
            print("Download failed for " + single_date.strftime("%y-%m-%d"))


