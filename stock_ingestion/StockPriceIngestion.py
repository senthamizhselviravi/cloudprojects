import json
import boto3
import sys
import yfinance as yf

import time
import random
import datetime


# Your goal is to get per-hour stock price data for a time range for the ten stocks specified in the doc. 
# Further, you should call the static info api for the stocks to get their current 52WeekHigh and 52WeekLow values.
# You should craft individual data records with information about the stockid, price, price timestamp, 52WeekHigh and 52WeekLow values and push them individually on the Kinesis stream

# kinesis = boto3.client('kinesis', region_name = "us-east-2") #Modify this line of code according to your requirement.

today = datetime.date.today() - datetime.timedelta(5)
yesterday = datetime.date.today() - datetime.timedelta(6)

# Example of pulling the data between 2 dates from yfinance API
#data = yf.download("MSFT", start= yesterday, end= today, interval = '1h' )

## Add code to pull the data for the stocks specified in the doc
def stock_to_kinesis(stock, start_date, end_date):
    # Download stock data from Yahoo Finance
    data = yf.download(stock, start=start_date, end=end_date, interval = '1h')
    tickers = yf.Tickers(stock)
    req1=tickers.tickers[stock].info
    stream_name='kdssen'
    # Initializing Kinesis Data Streams client
    kinesis = boto3.client('kinesis', region_name = "us-east-2")
    
    # Code to send data to  Kinesis
    for index, row in data.iterrows():
        record = {
            'Timestamp': str(index),
            'stock':stock,
            'Close': row['Close'],
            'fiftyTwoWeekLow':req1['fiftyTwoWeekLow'],
            'fiftyTwoWeekHigh':req1['fiftyTwoWeekHigh']
        }
        print(record)
        json_data = json.dumps(record)
        #print(json_data)
        ## Add your code here to push data records to Kinesis stream.
        response = kinesis.put_record(
            StreamName=stream_name,
            Data=json_data,
            PartitionKey=str(index)
        )
        
        print(f"Record sent to kinesis is : {response}")
    
    print("All records sent to Kinesis.")


## Add additional code to call 'info' API to get 52WeekHigh and 52WeekLow refering this this link - https://pypi.org/project/yfinance/



stocklist=['MSFT', 'MVIS', 'GOOG', 'SPOT', 'INO', 'OCGN', 'ABML', 'RLLCF', 'JNJ', 'PSFE']

for stk in stocklist:
    stock_to_kinesis(stk, yesterday,today)

