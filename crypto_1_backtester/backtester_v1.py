import pandas as pd
import sys
import talib as ta
from talib import MA_Type 
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector as mysql
import itertools
from itertools import combinations
from itertools import permutations
import re
import candlestick
import parametro
import strategia



def AvvioBacktester():
    
    exchange = sys.argv[1] #example: poloniex
    moneta = sys.argv[2]#example: 'BTC/ETH'

    risultato = []
    parametri = parametro.Parametro()
   
    strat = strategia.StrategiaTrendFollowing()
        
    strat.CalcolaStrategiaTrendFollowing(exchange,moneta,parametri,risultato)

    a = sorted(risultato, key=lambda a_entry: a_entry[2]) 

   

    
    
    print(a)
 
AvvioBacktester()


