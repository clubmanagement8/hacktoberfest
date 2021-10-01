from pynse import *
import pandas as pd
import datetime as dt
import csv
nse=Nse()
path = "C:\\Users\\karti\\Downloads\\bhavcopy.csv"
ticker_data=pd.read_csv(path, ",")
ticker_data.columns
Years = list(ticker_data["Year"])
Months = list(ticker_data["Month"])
Days = list(ticker_data["Day"])
data1=list(zip(Years,Months,Days))
l=[]
i=0
for data in data1:
    if i==0:
        df=nse.bhavcopy_fno(dt.date(int(data[0]),int(data[1]),int(data[2])))
    else:
        df=df.append(nse.bhavcopy_fno(dt.date(int(data[0]),int(data[1]),int(data[2]))))
    i=i+1
df.reset_index(inplace=True)
df = df[df['SYMBOL'] == 'WIPRO']
df = df[df['CONTRACTS'] > 1]
df = df[df['INSTRUMENT'] == 'OPTSTK']
df.to_excel(r'C:\Users\karti\Desktop\Backtest.xlsx', index = False)
df1=nse.get_hist('WIPRO',from_date=dt.date(2020, 10, 1),to_date=dt.date(2020, 10, 15))
df1
df1.to_excel(r'C:\Users\karti\Desktop\close.xlsx', index = False)