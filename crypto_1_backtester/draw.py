import matplotlib.pyplot as plt
import pandas as pd


class Draw():
    def __init__(self):

        plt.figure()

        self.vettori1 = []
        self.vettori2 = []
        self.vettori3 = []
        self.vettori4 = []
        self.nrgrafici = 3

    def setNrGrafici(self, nrgrafici):

        self.nrgrafici = nrgrafici

    def draw_graphic(self, moneta, x, y, nr_of_trades, nr_positive_trades,nr_negative_trades,buysignal_vect, sellsignal_vect,
                     prezzmed_vect, stoplosssignal_vect, stddev_vect,
                     titolostrategia, valorestrategia, date, ema_vect,
                     rsi_vect,pattern_vect,volume_vect,lower2_vect,
                     upper2_vect,ema_short_vect,ema_long_vect,lower_vect,upper_vect,macd_vect,macd_signal_vect,macd_hist_vect,atr_vect):

        self.moneta = moneta
        self.x = date
        self.y = y
        self.nr_of_trades = nr_of_trades
        self.nr_positive_trades = nr_positive_trades
        self.nr_negative_trades = nr_negative_trades
        self.buysignal_vect = buysignal_vect
        self.sellsignal_vect = sellsignal_vect
        self.prezzmed_vect = prezzmed_vect
        self.stoplosssignal_vect = stoplosssignal_vect
        self.stdev_vect = stddev_vect
        self.ema_vect = ema_vect
        self.rsi_vect = rsi_vect
        self.pattern_vect = pattern_vect
        self.volume_vect = volume_vect
        self.lower2_vect = lower2_vect
        self.upper2_vect = upper2_vect
        self.lower_vect = lower_vect
        self.upper_vect = upper_vect
        self.ema_short_vect = ema_short_vect
        self.ema_long_vect = ema_long_vect
        self.macd_vect = macd_vect
        self.macd_signal_vect = macd_signal_vect
        self.macd_hist_vect = macd_hist_vect
        self.atr_vect = atr_vect
        #KPI calcolo percentuale positive_trades su trades.
        self.percentage_negative_trades = (100 * self.nr_negative_trades) / self.nr_of_trades
        self.percentage_positive_trades = (100 * self.nr_positive_trades) / self.nr_of_trades
        self.titolostrategia = titolostrategia
        self.valorestrategia = valorestrategia
        self.chart_title = self.titolostrategia + ' Value of strategy: '+ str(self.valorestrategia) +'\n'+ 'Nr. of trades: '+str(nr_of_trades)+' Nr. positive trades: '+str(nr_positive_trades) + ' in %: '+str(self.percentage_positive_trades)

        if (self.nrgrafici == 3):

            self.draw_graphic_3()

        elif (self.nrgrafici == 2):

            self.draw_graphic_2()

        elif (self.nrgrafici == 1):

            self.draw_graphic_1()

        else:

            self.draw_graphic_4()

    def draw_graphic_1(self):

        print("The matplolib display has not been configured")
        plt.subplot(111)

        plt.plot(self.x, self.y, color="blue", linewidth=1, label="Close")
        plt.plot(self.x,
                 self.buysignal_vect,
                 color="green",
                 label="BuySignal",
                 marker='v')
        plt.plot(self.x,
                 self.sellsignal_vect,
                 color="red",
                 label="SellSignal",
                 marker='v')
        plt.plot(self.x,
                 self.stoplosssignal_vect,
                 color="brown",
                 linewidth=1,
                 label="Dinamyc Stoploss / Static Stoploss")  #fisso
        plt.plot(self.x,
                 self.prezzmed_vect,
                 color="purple",
                 label="Average Price")
        plt.plot(self.x,
                 self.ema_vect,
                 color="orange",
                 linewidth=1,
                 label="Ema Signal")
        plt.plot(self.x,
                 self.pattern_vect,
                 color="yellow",
                 label="Pattern Signal",
                 marker='v')
        plt.plot(self.x,
                 self.ema_short_vect,
                 color="black",
                 linewidth=1,
                 label="Ema Signal Short")
        plt.plot(self.x,
                 self.ema_long_vect,
                 color="red",
                 linewidth=1,
                 label="Ema Signal Long")
        plt.plot(self.x,
                self.upper_vect,
                color="black",
                label="BB Upper")
        plt.plot(self.x,
                self.lower_vect,
                color="purple",
                label="BB Lower")
        plt.plot(self.x,
                self.lower2_vect,
                color="green",
                label="BB Lower2")
        plt.plot(self.x,
                self.upper2_vect,
                color="green",
                label="BB Upper2")

        plt.xlabel('Time of ' + self.moneta)
        plt.ylabel('Price')
        plt.title(self.chart_title)
        plt.grid(True)
        plt.legend()
        plt.show()


    def draw_graphic_2(self):
        plt.subplot(211)
        
        plt.plot(self.x, self.y, color="blue", linewidth=1, label="Close")
        plt.plot(self.x,
                 self.buysignal_vect,
                 color="green",
                 label="BuySignal",
                 marker='v')
        plt.plot(self.x,
                 self.sellsignal_vect,
                 color="red",
                 label="SellSignal",
                 marker='v')
        plt.plot(self.x,
                 self.stoplosssignal_vect,
                 color="brown",
                 linewidth=1,
                 label="Dinamyc Stoploss / Static Stoploss")  #fisso
        plt.plot(self.x,
                 self.prezzmed_vect,
                 color="purple",
                 label="Average Price")
        """ plt.plot(self.x,
                 self.ema_vect,
                 color="orange",
                 linewidth=1,
                 label="Ema Signal")
        plt.plot(self.x,
                 self.pattern_vect,
                 color="yellow",
                 label="Pattern Signal",
                 marker='v') """
        """ plt.plot(self.x,
                self.upper2_vect,
                color="black",
                label="BB Upper 2")
        plt.plot(self.x,
                self.lower2_vect,
                color="black",
                label="BB Lower 2") """

        plt.xlabel('Time of ' + self.moneta)
        plt.ylabel('Price')
        plt.title(self.chart_title)
        plt.grid(True)
        plt.legend()
        
        plt.subplot(212)
        
        # plt.plot(self.x,
        #          self.macd_hist_vect,
        #          color="red",
        #          label="Macd_hist")
        plt.plot(self.x,
                 self.atr_vect,
                 color="red",
                 label="Atr")
        

        plt.xlabel('Time of ' + self.moneta)
        plt.ylabel('Values')
        plt.grid(True)
        plt.legend()
        plt.show()
        

        print("The matplolib display has not been configured")

    def draw_graphic_3(self):

        plt.subplot(311)

        plt.plot(self.x, self.y, color="blue", linewidth=1, label="Close")
        plt.plot(self.x,
                 self.buysignal_vect,
                 color="green",
                 label="BuySignal",
                 marker='v')
        plt.plot(self.x,
                 self.sellsignal_vect,
                 color="red",
                 label="SellSignal",
                 marker='v')
        plt.plot(self.x,
                 self.stoplosssignal_vect,
                 color="brown",
                 linewidth=1,
                 label="Dinamyc Stoploss / Static Stoploss")  #fisso
        plt.plot(self.x,
                 self.prezzmed_vect,
                 color="purple",
                 label="Average Price")
        plt.plot(self.x,
                 self.ema_vect,
                 color="orange",
                 linewidth=1,
                 label="Ema Signal")
        plt.plot(self.x,
                 self.pattern_vect,
                 color="yellow",
                 label="Pattern Signal",
                 marker='v')
        plt.plot(self.x,
                 self.ema_short_vect,
                 color="black",
                 linewidth=1,
                 label="Ema Signal Short")
        plt.plot(self.x,
                 self.ema_long_vect,
                 color="red",
                 linewidth=1,
                 label="Ema Signal Long")
        
        """ plt.plot(self.x,
                self.upper2_vect,
                color="black",
                label="BB Upper 2")
        plt.plot(self.x,
                self.lower2_vect,
                color="black",
                label="BB Lower 2") """

        plt.xlabel('Time of ' + self.moneta)
        plt.ylabel('Price')
        plt.title(self.chart_title)
        plt.grid(True)
        plt.legend()

        plt.subplot(312)
        plt.plot(self.x,
                 self.rsi_vect,
                 color="red",
                 label="Rsi")
        

        plt.xlabel('Time of ' + self.moneta)
        plt.ylabel('Values')
        plt.grid(True)
        plt.legend()
        

        plt.subplot(313)
        plt.fill_between(self.x,
                 self.volume_vect,
                 color="green",
                 label="Volume",
                 alpha=0.4)
        

        plt.xlabel('Time of ' + self.moneta)
        plt.ylabel('Values')
        plt.grid(True)
        plt.legend()
        
        

        plt.show()

    def draw_graphic_4(self):

        print("The matplolib display has not been configured")
