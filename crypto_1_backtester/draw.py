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

    def draw_graphic(self, moneta, x, y, buysignal_vect, sellsignal_vect,
                     prezzmed_vect, stoplosssignal_vect, stddev_vect,
                     titolostrategia, valorestrategia, date, ema_vect,
                     rsi_vect):

        self.moneta = moneta
        self.x = date
        self.y = y
        self.buysignal_vect = buysignal_vect
        self.sellsignal_vect = sellsignal_vect
        self.prezzmed_vect = prezzmed_vect
        self.stoplosssignal_vect = stoplosssignal_vect
        self.stdev_vect = stddev_vect
        self.ema_vect = ema_vect
        self.rsi_vect = rsi_vect

        self.titolostrategia = titolostrategia
        self.valorestrategia = valorestrategia

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

    def draw_graphic_2(self):

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

        plt.xlabel('Time of ' + self.moneta)
        plt.ylabel('Price')
        plt.title(self.titolostrategia + ' Value of strategy: ' +
                  str(self.valorestrategia))
        plt.grid(True)
        plt.legend()

        plt.subplot(312)

        plt.plot(self.x, self.y, color="blue", linewidth=1, label="Close")
        plt.plot(self.x,
                 self.stoplosssignal_vect,
                 color="brown",
                 linewidth=1,
                 label="Stoploss Signal")
        plt.plot(self.x,
                 self.sellsignal_vect,
                 color="red",
                 label="SellSignal",
                 marker='v')

        plt.xlabel('Time of  ' + self.moneta)
        plt.ylabel('Price')

        plt.grid(True)
        plt.legend()

        plt.subplot(313)

        plt.plot(self.x, self.y, color="blue", linewidth=1, label="Close")
        plt.plot(self.x,
                 self.stoplosssignal_vect,
                 color="brown",
                 linewidth=1,
                 label="Stoploss Signal")
        plt.plot(self.x,
                 self.buysignal_vect,
                 color="green",
                 label="BuySignal",
                 marker='v')

        plt.xlabel('Time of ' + self.moneta)
        plt.ylabel('Price')

        plt.grid(True)
        plt.legend()

        plt.show()

    def draw_graphic_4(self):

        print("The matplolib display has not been configured")
