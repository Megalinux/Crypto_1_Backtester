class Tools:
    def __init__(self):

        self.profitto = 0.6
        self.profitti_Intervallo = [1]  #inactive
        self.stoploss_1 = 1
        self.hours = 7
        self.periodo = '5m'  #default value
        self.setStoploss_1_Intervallo = [1, 2, 3]  #inactive
        self.stoploss_2 = 4  #inactive
        self.setStoploss_2_Intervallo = [4, 5]  #inactive
        self.nrtransizioni = 500  #inactive
        self.nrtransizioni_Intervallo = [1000]  #inactive
        self.commissioni = 0.25
        self.commissioni_Intervallo = [0.25, 0.35]  #inactive
        self.visualizzagrafico = 0
        self.ricerca_parametri = 0  #inactive
        self.diffbb_price = 0.01  #inactive
        self.diffbb_price_intervallo = [0.01, 0.02]  #inactive
        self.attivazione_stoploss_statico = 0
        self.attivazione_stoploss_dinamico = 0  #trailing_stop
        self.stoploss_dinamico_moltiplicatore = 0.995
        self.stoploss_dinamico_formula = "row.close * parametri.stoploss_dinamico_moltiplicatore"  # formula example of default for calculating dynamic stop loss
        self.attivazione_stoploss_dinamico_limiti = 1  #if activated the minimum profit limits and the maximum loss limits come into operation
        self.stoploss_dinamico_min_profitto = 1.1
        self.stoploss_dinamico_max_perdita = 2

    def setDiffbbprice(self, numero):

        self.diffbb_price = numero

    def setDiffbbprice_Intervallo(self, vect):

        self.diffbb_price_intervallo = vect

    def setAttivazione_Profitto(self, attivazione):

        self.attivazione_profitto = attivazione

    def setAttivazione_Stoploss_Statico(self, attivazione):

        self.attivazione_stoploss_statico = attivazione

    def setProfitto(self, numero):

        self.numero = numero

    def setPeriodo(self, numero):

        self.numero = numero

    def setProfitti(self, vect):

        self.profitti = vect

    def setAttivazioneStoploss_Dinamico(self, abilitazione):

        self.attivazione_stoploss_dinamico = abilitazione

    def getStoploss_dinamico(self):

        return self.stoploss_dinamico

    def setStoploss_1(self, numero):

        self.stoploss_1 = numero

    def setStoploss_1_Intervallo(self, vect):

        self.stoploss_1_intervallo = vect

    def setStoploss_2(self, numero):

        self.stoploss_2 = numero

    def setStoploss_2_Intervallo(self, vect):

        self.stoploss_1_intervallo = vect

    def setTransizioni(self, numero):

        self.nrtransizioni = numero

    def setTransizioni_Intervallo(self, vect):

        self.nrtransizioni_intervallo = vect

    def setTrailing_stop(self, abilitazione):

        self.trailing_stop = abilitazione

    def setCommissioni(self, commissioni):

        self.commissioni = commissioni

    def setCommissioni_Intervallo(self, commissioni):

        self.setCommissioni_Intervallo = commissioni

    def setRicercaparametri(self, abilitazione):

        self.ricerca_parametri = abilitazione

    def setVisualizzaGrafico(self, abilitazione):

        self.visualizzagrafico = abilitazione
