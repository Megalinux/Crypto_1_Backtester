import pandas as pd
import requests, json
import ccxt
import arrow
from datetime import datetime,timedelta

class Candlestick:
    
    def __init__(self):
        
        
        self.tick_interval = '5m' #default value
        self.exchange = 'binance' #default exchange
        self.pair = "ETH/BTC" #default pair
        self.hours = 7 #default timedelta
          
        
            

    def getCandle(self,exchange,pair,hours,tick_interval):
 
        
        self.periodo = tick_interval
        self.exchange = exchange
        self.hours = hours
        self.pair = pair

        from_datetime1 = datetime.now()-timedelta(hours = self.hours)
        from_datetime = from_datetime1.strftime('%Y-%m-%d %H:%M:%S')
        
    
        OHCLV = []

        exchange_class = getattr(ccxt,self.exchange)

        exchange = exchange_class({

            'enableRateLimit': True
        
        })
       
        markets = exchange.load_markets()
        
        

        #open, high, low, close, volume

        if exchange.has['fetchOHLCV']:

                
                
            OHCLV = exchange.fetch_ohlcv(self.pair,self.periodo,exchange.parse8601(from_datetime))

            header = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
            df3 = pd.DataFrame(OHCLV, columns=header).set_index('timestamp')
            



        

        return df3
        

        
        
        
        


