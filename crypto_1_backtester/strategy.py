import candlestick
import talib as ta
from talib import MA_Type
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import draw
import json, requests
import logging
import qtpylib as qt
from datetime import datetime, timedelta


class Strategy:
    def __init__(self):

        raise NotImplementedError("There is a problem...!")

    def __str__(self):

        return self.nome


class StrategyTrendFollowing(Strategy):
    def __init__(self):

        logging.basicConfig(format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            filename='./log/strategyTF.log',
                            level=logging.INFO)

        # create file handler which logs even debug messages

        self.nome = "Test "  #default
        self.descrizione = "Strategy TrendFollowing"  #default
        self.quantita = 1
        self.tipostrategia = "TrendFollowing"  #default
        self.stoplossprezzo = 0
        self.totalecommissioni = 0  #inizializzazione delle commissioni
        self.lastbuy = 0
        self.stoploss = 0
        self.buy = 0
        self.sell = 0
        self.valorestrategia = 0
        self.condizioni_sell = ""
        self.condizioni_buy = ""
        self.df1 = ""
        self.qt = qt

    def setNome(self, nome):

        self.nome = nome

    def setDescrizione(self, descrizione):

        self.descrizione = descrizione

    def setQuantita(self, quantita):

        self.quantita = quantita

    def stoplossprezzo(self, numero):

        self.stoplossprezzo = numero

    def ExecuteTrendFollowing(self, exchange, moneta, tool, risultato):

        #Attention: static stoploss and dynamic stoploss cannot be activated simultaneously

        tool.attivazione_stoploss_statico = 0  #with zero not activated, with 1 activated
        tool.attivazione_stoploss_dinamico = 1  # with zero not activated, with 1 activated
        tool.profitto = 0.7  #minimum percentage of profit
        tool.stoploss_1 = 0.8  #percentage of stoploss
        tool.stoploss_2 = 2.0  #second level stoploss percentage (not active for now)
        tool.commissioni = 0.25  #percentage of fees in buy and sell
        tool.nrtransizioni = 2000  #do not use
        tool.stoploss_dinamico_moltiplicatore = 0.994  #multiplier of the trailing stop
        tool.stoploss_dinamico_formula = "row.close * tool.stoploss_dinamico_moltiplicatore"  #formula per il calcolo dello stoploss dinamico (trailing stop)
        tool.attivazione_stoploss_dinamico_limiti = 1  #with zero not activated, with 1 activated. It works if dynamic stoploss is activated
        tool.stoploss_dinamico_min_profitto = 0.8  #minimum profit compared to lastbuy if activated stoploss_dinamico_limiti
        tool.stoploss_dinamico_max_perdita = 2  #max loss in percentage compared to lastbuy if activated stoploss_dinamico_limiti
        tool.hours = 36  #timedelta from now

        self.nome = "Test Strategy Trend Following "

        candle = candlestick.Candlestick()

        self.df1 = candle.getCandle(exchange, moneta, tool.hours, tool.periodo)

        moneta = moneta

        exchange = exchange

        self.df1 = self.df1.apply(pd.to_numeric)

        #-------------Indicators and oscillators of the Ta-lib library
        self.df1['rsi'] = ta.RSI(self.df1.close.values, timeperiod=14)
        self.df1['adx'] = ta.ADX(self.df1['high'].values,
                                 self.df1['low'].values,
                                 self.df1['close'].values,
                                 timeperiod=14)
        self.df1['upper'], self.df1['middle'], self.df1['lower'] = ta.BBANDS(
            self.df1['close'].values, matype=1)  #Calcolo di Bollinger Bands
        self.df1['upper2'], self.df1['middle2'], self.df1[
            'lower2'] = ta.BBANDS(self.df1['close'].values, matype=2)
        self.df1['upper3'], self.df1['middle3'], self.df1[
            'lower3'] = ta.BBANDS(self.df1['close'].values, matype=3)
        self.df1['PrezzoMed'] = self.df1['close'].mean()
        self.df1['STDDEV'] = ta.STDDEV(self.df1['close'].values,
                                       timeperiod=15,
                                       nbdev=1)
        self.df1['macd'], self.df1['macdsignal'], self.df1[
            'macdhist'] = ta.MACD(self.df1.close.values,
                                  fastperiod=12,
                                  slowperiod=26,
                                  signalperiod=9)
        self.df1['minus_di'] = ta.MINUS_DI(self.df1['high'].values,
                                           self.df1['low'].values,
                                           self.df1['close'].values,
                                           timeperiod=25)
        self.df1['plus_di'] = ta.PLUS_DI(self.df1['high'].values,
                                         self.df1['low'].values,
                                         self.df1['close'].values,
                                         timeperiod=25)
        self.df1['sar'] = ta.SAR(self.df1['high'].values,
                                 self.df1['low'].values,
                                 acceleration=0,
                                 maximum=0)
        self.df1['mom'] = ta.MOM(self.df1['close'].values, timeperiod=14)
        self.df1['atr'] = ta.ATR(self.df1['high'].values,
                                 self.df1['low'].values,
                                 self.df1['close'].values,
                                 timeperiod=14)
        self.df1['ema'] = ta.EMA(self.df1['close'].values, timeperiod=20)
        self.df1['ema1'] = ta.EMA(self.df1['close'].values, timeperiod=28)
        self.df1['ema2'] = ta.EMA(self.df1['close'].values, timeperiod=35)
        self.df1['ema3'] = ta.EMA(self.df1['close'].values, timeperiod=48)
        self.df1['cci'] = ta.CCI(self.df1['high'].values,
                                 self.df1['low'].values,
                                 self.df1['close'].values,
                                 timeperiod=14)

        self.df1['Sellsignal'] = 0
        self.df1['Buysignal'] = 0

        #---------------------example 1 buy and sell ----------------------------------------
        #-------------Buy conditions----------------------------------------------------------
        #(self.df1['macd'] > self.df1['macdsignal']) &"
        #(self.df1['cci'] <= -50.0)"

        #-------------Sell conditions----------------------------------------------------------
        #(self.df1['macd'] < self.df1['macdsignal']) &"
        #(self.df1['cci'] >= 100.0)"

        #------------------------example 2 buy and sell---------------------------------------
        #-------------Buy conditions----------------------------------------------------------
        #(self.df1['adx'] > 25) &"
        #(self.df1['mom'] < 0) &"
        #(self.df1['minus_di'] > 25) &"
        #(self.df1['plus_di'] < self.df1['minus_di'])"

        #-------------Sell conditions----------------------------------------------------------
        #(self.df1['adx'] > 25) &"
        #(self.df1['mom'] > 0) &"
        #(self.df1['minus_di'] > 25) &"
        #(self.df1['plus_di'] > self.df1['minus_di'])"
        # --------------------------------------------------------------------------

        self.df1.loc[(((
            self.qt.crossed_above(self.df1['rsi'], 70)))), 'Sellsignal'] = -1

        self.df1.loc[(((
            self.qt.crossed_below(self.df1['rsi'], 35)))), 'Buysignal'] = 1

        #---------------------------trailing stoploss---------------------------
        #example 1

        #tool.stoploss_dinamico_formula = "row.close * tool.stoploss_dinamico_moltiplicatore" #formula for calculating dynamic stoploss (trailing stop)

        #example 2

        tool.stoploss_dinamico_formula = "row.ema3"

        x = []
        y = []
        balance = []
        close_vect = []
        buysignal_vect = []
        sellsignal_vect = []
        prezzmed_vect = []
        stdev_vect = []
        stoplosssignal_vect = []
        stoplossprezzo_vect = []
        ema_vect = []
        date = []

        rsi_vect = []

        i = 0

        for row in self.df1.itertuples():
            a = row.Index / 1000.0
            b = datetime.fromtimestamp(a)

            self.stoploss = self.getStoploss(row, i, tool)

            logging.info("-----------Loop line processing " + str(i))
            logging.info("1) self.stoploss value = " + str(self.stoploss))

            if (i > 0):

                stoplossprezzo_vect.append(self.stoplossprezzo)

                logging.info(
                    "2) Value of i greater than zero not first loop for i =" +
                    str(i))

                logging.info("2.1) Value of self.stoplossprezzo = " +
                             str(self.stoplossprezzo))

            else:

                self.stoplossprezzo = row.close * 0.99

                logging.info(
                    "2) Value of i equal to zero first loop for i = " + str(i))

                stoplossprezzo_vect.append(self.stoplossprezzo)

                logging.info("2.1) Value of self.stoplossprezzo = " +
                             str(self.stoplossprezzo))

            if (self.stoploss == 1):

                logging.info(
                    "3) self.stoploss value = 1 after getstoploss method ")

            x.append(i)
            y.append(row.close)

            if (row.Sellsignal == 0
                    and self.stoploss == 0) or (row.Sellsignal == 1
                                                and self.stoploss == 1):

                logging.info("4) Value of self.stoploss before If for sell " +
                             str(self.stoploss))
                logging.info("4.1) Value of row.Sellsignal " +
                             str(row.Sellsignal))

                sellsignal_vect.append(np.nan)

                stoplosssignal_vect.append(np.nan)

            else:

                if (self.stoploss == 1):

                    logging.info("5) self.stoploss value = 1 else before if ")
                    logging.info(
                        "5.1) Indication of sell in presence of self.stoploss = 1"
                    )

                    if (self.sell == 0) and (self.buy == 1):

                        logging.info(
                            "5.2) Sell with self.stoploss = 1 self.stoploss = "
                            + str(self.stoploss))
                        logging.info(
                            "5.2.1) Sell with self.stoploss = 1 self.sell = " +
                            str(self.sell))
                        logging.info(
                            "5.2.2) Sell with self.stoploss = 1  self.buy = " +
                            str(self.buy))

                        sellsignal_vect.append(row.close)

                        stoplosssignal_vect.append(row.close)

                        percentualecommissioni = (
                            float(row.close) / 100) * float(tool.commissioni)

                        logging.info(
                            "5.3) Percentage of fees in presence of self.stoploss = 1"
                            + str(percentualecommissioni))

                        balance.append(
                            [row.close - (percentualecommissioni), 1])

                        self.totalecommissioni = self.totalecommissioni + percentualecommissioni

                        logging.info(
                            "5.4) Total fees in presence of self.stoploss = 1 "
                            + str(self.totalecommissioni))

                        self.sell = 1

                        self.buy = 0

                        self.stoploss = 0

                        logging.info(
                            "5.5) Assign value zero to self.stoploss = " +
                            str(self.stoploss))
                        logging.info("5.6) Assign value 1 to self.sell = " +
                                     str(self.sell))
                        logging.info("5.7) Assign value zero to self.buy = " +
                                     str(self.buy))

                    else:

                        sellsignal_vect.append(np.nan)

                        stoplosssignal_vect.append(np.nan)

                        self.stoploss = 0

                else:

                    stoplosssignal_vect.append(np.nan)

                    if ((self.sell == 0) and (self.buy == 1)
                            and (tool.attivazione_stoploss_dinamico == 0)):

                        logging.info(
                            "6.0) Sell ​​normal not in the presence of dynamic stoploss"
                        )
                        logging.info("6.1) Value of self.sell: " +
                                     str(self.sell))
                        logging.info("6.2) Value of self.buy: " +
                                     str(self.buy))
                        logging.info(
                            "6.3) Dynamic stoploss activation parameter value: "
                            + str(tool.attivazione_stoploss_dinamico))

                        price1 = float(self.lastbuy) + (
                            (float(self.lastbuy)) / 100) * float(tool.profitto)
                        logging.info("6.4) Value of self.lastbuy: " +
                                     str(self.lastbuy))
                        logging.info("6.5) Price1 price of sell: " +
                                     str(price1))
                        logging.info("6.6) Profit parameters: " +
                                     str(tool.profitto))

                        if (float(row.close) > float(price1)):

                            logging.info(
                                "6.7) Sell in presence of row.close greater than value of price1"
                            )
                            logging.info("6.8) Value of row.close: " +
                                         str(row.close))
                            logging.info("6.9) Value of sell price: " +
                                         str(price1))

                            sellsignal_vect.append(row.close)

                            percentualecommissioni = (float(
                                row.close) / 100) * float(tool.commissioni)

                            logging.info(
                                "6.9.1) Percentage of fees in presence of self.stoploss = 1 "
                                + str(percentualecommissioni))

                            balance.append(
                                [row.close - (percentualecommissioni), 1])

                            self.totalecommissioni = self.totalecommissioni + percentualecommissioni

                            logging.info(
                                "6.9.2) Total of fees in presence of self.stoploss = 1"
                                + str(self.totalecommissioni))

                            self.sell = 1
                            self.buy = 0
                            self.stoploss = 0

                            logging.info(
                                "6.9.3) Assign value zero to self.stoploss = "
                                + str(self.stoploss))
                            logging.info(
                                "6.9.4) Assign value 1 to self.sell = " +
                                str(self.sell))
                            logging.info(
                                "6.9.5) Assign value 0 to self.buy = " +
                                str(self.buy))

                        else:

                            sellsignal_vect.append(np.nan)

                    else:

                        sellsignal_vect.append(np.nan)

            if ((row.Buysignal == 0 or row.Buysignal == '0')):

                logging.info(
                    "7) Value of self.stoploss in if row.BuySignal = 0 " +
                    str(self.stoploss))
                logging.info("7.1) Value of row.Buysignal " +
                             str(row.Buysignal))

                buysignal_vect.append(np.nan)

            else:

                if ((row.Buysignal == 1 or row.Buysignal == '1')):

                    logging.info("8) Value of row.Buysignal " +
                                 str(row.Buysignal))

                    if (self.buy == '0' or self.buy == 0):

                        logging.info(
                            "8.1) Buy in presence of self.stoploss =  " +
                            str(self.stoploss))
                        logging.info("8.2) Value of self.sell = " +
                                     str(self.sell))
                        logging.info("8.3) Value of self.buy = " +
                                     str(self.buy))

                        buysignal_vect.append(row.close)

                        percentualecommissioni = (
                            float(row.close) / 100) * float(tool.commissioni)

                        logging.info(
                            "8.4) Percentage of fees in presence of self.stoploss = 1 "
                            + str(percentualecommissioni))

                        self.totalecommissioni = self.totalecommissioni + percentualecommissioni

                        logging.info(
                            "8.5) Total of fees in presence of stoploss = 1" +
                            str(self.totalecommissioni))

                        balance.append([(-row.close - percentualecommissioni),
                                        0])

                        self.buy = 1

                        self.sell = 0

                        logging.info(
                            "8.5.1) Assign value zero to self.stoploss = " +
                            str(self.stoploss))
                        logging.info(
                            "8.5.2) Assign value zero to self.sell = " +
                            str(self.sell))
                        logging.info("8.5.3) Assign value 1 to self.buy = " +
                                     str(self.buy))

                        if (tool.attivazione_stoploss_dinamico == 1):

                            logging.info(
                                "8.6) Value of tool.attivazione_stoploss_dinamico equal to : "
                                + str(tool.attivazione_stoploss_dinamico))

                            self.stoplossprezzo = eval(
                                tool.stoploss_dinamico_formula)

                            logging.info(
                                "8.6.1) Value of self.stoplossprezzo " +
                                str(self.stoplossprezzo))

                        else:

                            self.stoplossprezzo = (row.close - (
                                (row.close / 100) * tool.stoploss_1))

                            logging.info(
                                "8.7) Value of self.stoplossprezzo with tool.attivazione_stoploss_dinamico equal to 1 = "
                                + str(self.stoplossprezzo))

                        self.lastbuy = row.close

                        logging.info("8.8) Value of self.lastbuy" +
                                     str(self.lastbuy))
                        logging.info("8.9.0) Value of self.stoploss = " +
                                     str(self.stoploss))
                        logging.info("8.9.1) Value of self.sell = " +
                                     str(self.sell))
                        logging.info("8.9.2) Value of self.buy = " +
                                     str(self.buy))
                        logging.info("8.9.3) Value of self.stoplossprezzo = " +
                                     str(self.stoplossprezzo))
                        logging.info("8.9.4) Value of self.lastbuy = " +
                                     str(self.lastbuy))
                        logging.info(
                            "8.9.5) Value of  tool.attivazione_stoploss_dinamico = "
                            + str(tool.attivazione_stoploss_dinamico))
                        logging.info(
                            "8.9.6) Value of tool.attivazione_stoploss_statico = "
                            + str(tool.attivazione_stoploss_statico))

                    else:
                        buysignal_vect.append(np.nan)

                else:
                    buysignal_vect.append(np.nan)

            prezzmed_vect.append(row.PrezzoMed)
            stdev_vect.append(row.STDDEV)
            ema_vect.append(row.ema3)
            date.append(b)

            rsi_vect.append(row.rsi)

            i = i + 1

        self.valorestrategia = self.getValoreStrategia(balance)

        tool.setVisualizzaGrafico(1)

        if (tool.visualizzagrafico == 1 or tool.visualizzagrafico == '1'):

            ds = draw.Draw()

            ds.setNrGrafici(3)

            ds.draw_graphic(moneta, x, y, buysignal_vect, sellsignal_vect,
                            prezzmed_vect, stoplossprezzo_vect, stdev_vect,
                            self.nome, self.valorestrategia, date, ema_vect,
                            rsi_vect)

    def getStoploss(self, row, i, tool):

        stoploss = 0

        if ((tool.attivazione_stoploss_dinamico == 1) and (i > 0)):

            if (row.close > self.df1.iloc[i - 1, 3]):

                logging.info(
                    "10.0.0) Value of tool.attivazione_stoploss_statico = " +
                    str(tool.attivazione_stoploss_statico))
                logging.info(
                    "10.0.1) Value of tool.attivazione_stoploss_dinamico = " +
                    str(tool.attivazione_stoploss_dinamico))
                logging.info("10.0.2) Value of  row.close = " + str(row.close))
                logging.info("10.0.3) Value of price -1 = " +
                             str(self.df1.iloc[i - 1, 3]))

                self.stoplossprezzo = eval(tool.stoploss_dinamico_formula)

                logging.info("10.0.4) Value of self.stoplossprezzo = " +
                             str(self.stoplossprezzo))
                logging.info("10.0.5) Value of self.stoploss = " +
                             str(stoploss))

            if (self.df1.iloc[i - 2, 3] > self.stoplossprezzo
                    and row.close < self.stoplossprezzo and self.sell == 0):

                logging.info(
                    "10.0.5.1) Entry with exceeding the stoploss indicated by the formula = "
                    + str(stoploss))

                if (tool.attivazione_stoploss_dinamico_limiti == 1):

                    prezzo_max_perdita = (self.lastbuy -
                                          ((self.lastbuy / 100) *
                                           tool.stoploss_dinamico_max_perdita))
                    prezzo_min_profitto = (
                        self.lastbuy + ((self.lastbuy / 100) *
                                        tool.stoploss_dinamico_min_profitto))

                    logging.info("10.0.6) Value of prezzo_max_perdita = " +
                                 str(prezzo_max_perdita))
                    logging.info("10.0.7) Value of prezzo_min_profitto = " +
                                 str(prezzo_min_profitto))

                    if (row.close < prezzo_max_perdita):

                        stoploss = 1
                        logging.info(
                            "10.0.8) Value row.close less than value of prezzo_max_perdita = "
                            + str(prezzo_max_perdita))
                        logging.info("10.0.9) Value of stoploss = " +
                                     str(stoploss))

                    else:

                        stoploss = 0
                        logging.info(
                            "10.0.9.1) Value of prezzo_max_perdita = " +
                            str(prezzo_max_perdita))

                    if (row.close > prezzo_min_profitto):

                        stoploss = 1
                        logging.info(
                            "10.0.8) Value row.close greater than value of prezzo_min_profitto = "
                            + str(prezzo_min_profitto))
                        logging.info("10.0.9) Value of stoploss = " +
                                     str(stoploss))

                    else:
                        stoploss = 0
                        logging.info(
                            "10.0.9.1) Value row.close less than value of prezzo_min_profitto = "
                            + str(prezzo_min_profitto))

                else:
                    stoploss = 1

                logging.info("11.0.0) Value of stoploss =" + str(stoploss))

        if ((row.close < self.stoplossprezzo) and (i > 0)
                and (tool.attivazione_stoploss_statico == 1)
                and (tool.attivazione_stoploss_dinamico == 0)):

            stoploss = 1
            logging.info(
                "12.0.0) Value of tool.attivazione_stoploss_statico = 1 = " +
                str(tool.attivazione_stoploss_statico))
            logging.info("12.0.1) Value of row.close = " + str(row.close))
            logging.info("12.0.2) Value of self.stoplossprezzo = " +
                         str(self.stoplossprezzo))
            logging.info("12.0.3) Value of stoploss = 1 =" + str(stoploss))

        return stoploss

    def getValoreStrategia(self, balance):

        for i in range(len(balance)):

            if (i == len(balance) - 1):

                if (balance[i][1] == '1' or balance[i][1] == 1):

                    self.valorestrategia = self.valorestrategia + float(
                        balance[i][0])

                else:

                    self.valorestrategia = self.valorestrategia + 0
            else:

                self.valorestrategia = self.valorestrategia + float(
                    balance[i][0])

            i = i + 1

        return self.valorestrategia
