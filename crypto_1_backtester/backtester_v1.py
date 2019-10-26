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
import tools
import strategy


def AvvioBacktester():

    exchange = sys.argv[1]  #example: poloniex
    moneta = sys.argv[2]  #example: 'BTC/ETH'

    risultato = []
    tool = tools.Tools()

    strat = strategy.StrategyTrendFollowing()

    strat.ExecuteTrendFollowing(exchange, moneta, tool, risultato)

    a = sorted(risultato, key=lambda a_entry: a_entry[2])

    print(a)


AvvioBacktester()
