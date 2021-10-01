import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
import os
import pickle
from pynse import *
import pandas as pd
import datetime as dt
import csv

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# here enter the id of your google sheet
SAMPLE_SPREADSHEET_ID_input = '1cvZswLiDo3LfhnA7RcS8vFqacx73RGor-OZ_FtvyLE8'
SAMPLE_RANGE_NAME = 'A1:AA1000'

def main():
    global values_input, service
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'my_json_file.json', SCOPES) # here enter the name of your downloaded JSON file
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result_input = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                range=SAMPLE_RANGE_NAME).execute()
    values_input = result_input.get('values', [])

    if not values_input and not values_expansion:
        print('No data found.')

main()

df=pd.DataFrame(values_input[1:], columns=values_input[0])
nse=Nse()
path = "C:\\Users\\karti\\Desktop\\prac.csv"
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
df = df[df['SYMBOL'] == 'PNB']
df = df[df['CONTRACTS'] > 1]
df = df[df['INSTRUMENT'] == 'OPTSTK']
df.to_excel(r'C:\Users\karti\Desktop\Backtest.xlsx', index = False)