import vectorbt as vbt

price = vbt.YFData.download('BTC-USD').get('Close')

pf = vbt.Portfolio.from_holding(price, init_cash=100)
print(pf.total_profit())

fast_ma = vbt.MA.run(price, 10)
slow_ma = vbt.MA.run(price, 50)
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

pf = vbt.Portfolio.from_signals(price, entries, exits, init_cash=100)
print(pf.total_profit())