# Crypto_1_Backtester #

[![Donate with Bitcoin](https://en.cryptobadges.io/badge/small/3EJZiSmqRkoZ48ae2pYbKupMYQqoQvxdxe)](https://en.cryptobadges.io/donate/3EJZiSmqRkoZ48ae2pYbKupMYQqoQvxdxe)

* Backtesting is a process of applying a current strategy to historical data with the objective to determine wich implemented strategy is the best in terms of profit. The profit is determined by sell and buy transactions.

* Crypto_1_Backtester is a backtester tool of trading strategies written by Grando Ruggero. This tool performs a simulation with a single pair of cryptocurrency on a single run and implements a dynamic and static stoploss. The backtester uses an Crypto Asset exchange (among those supported by the [CCXT](https://github.com/ccxt/ccxt) library) like Poloniex, or Bittrex, or Binance and the Pair (asset/currency) like ETH/BTC, or ETC/BTC  present in these exchanges.  
* Version 0.0.1

### Disclaimer ###

This software is for educational purposes only. Do not risk money which you are afraid to lose. USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS.

We strongly recommend you to have coding and Python knowledge. Do not hesitate to read the source code and understand the mechanism of this backtester.

### Features ###

* **Backtesting** of your strategies with Ta-lib and Qtpylib trading libraries
* Use of static and dynamic **stoploss**. Create your dinamyc stoploss formula.
* **Visualization** of the strategy progress and result with matplotblib
* Configuration of a set of **parameters**
* Calculation of a strategy **value**
* Support of CryptoCurrency eXchange Trading Library [CCXT](https://github.com/ccxt/ccxt)

### Creating your Strategy ###

* You can define a strategy by implementing the Strategy Class in strategy.py. Through the configuration of numerous parameters present in the file tools.py there is the possibility of implementing many strategies using the Qtpylib and Ta-lib libraries.
 
### Example 1 of strategy ###

```python

self.df1.loc[
            (            
                (

                    (self.qt.crossed_above(self.df1['rsi'], 70))                    
                )         
            ),
            'Sellsignal'] = -1

        self.df1.loc[
            (
                (  
                    (self.qt.crossed_below(self.df1['rsi'], 35)) 
                ) 
            ),
            'Buysignal'] = 1
```

### Example 2 of strategy ###

```python

self.df1.loc[
            (            
                (
                    (self.df1['macd'] < self.df1['macdsignal']) &
                    (self.df1['cci'] >= 100.0)              
                )         
            ),
            'Sellsignal'] = -1

        self.df1.loc[
            (
                (  

                    (self.df1['macd'] > self.df1['macdsignal']) &
                    (self.df1['cci'] <= -50.0)

                ) 
            ),
            'Buysignal'] = 1
```

### Create your dinamyc stoploss

* Create your dinamyc stoploss formula.

1. Modify the parameter tool.stoploss_dinamico_formula on file strategy.py with text editor as following described.

###example 1 ###

```python

tool.stoploss_dinamico_formula = "row.close * tool.stoploss_dinamico_moltiplicatore" 
        
```

### example 2 ###      

```python  

tool.stoploss_dinamico_formula = "row.ema3"

```

### Run ###

1. Configure strategy and parameters on strategy.py with text editor as already described
2. In terminal/cmd go to Your main Backtester's folder.
3. Run BacktestTool by command: python3 backtester_v1 {exchange} {pair}
    Example of run backtester:

    * `python3 backtester_v1 poloniex 'ATOM/BTC'`
    * `python3 backtester_v1 poloniex 'DOGE/BTC'`
    * `python3 backtester_v1 poloniex 'ETH/BTC'` 
    * `python3 backtester_v1 binance 'ETC/BTC'` 


### Requirements ###

* Python >=3.4
* Talib
* Matplotlib
* Requests
* Numpy
* Pandas
* Json
* Logging
* Ccxt

### Support ###

For any questions not covered by the documentation or for further information about the backtester, we encourage you to send an email to webmaster@megalinux.it

### Bugs / Issues ###

If you discover a bug in the bot, please search [our issue tracker first](https://github.com/Megalinux/Crypto_1_Backtester/issues?q=is%3Aissue) . If it hasn't been reported, please [create a new issue](https://github.com/Megalinux/Crypto_1_Backtester/issues/new) and ensure you follow the template guide so that our team can assist you as quickly as possible.
Feature Requests

Have you a great idea to improve the bot you want to share? Please, first search if this feature was not already discussed. If it hasn't been requested, please create a new request!

### License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2019 © Grando Ruggero.