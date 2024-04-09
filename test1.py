import numpy as np
import pandas as pd
from datetime import datetime

import vectorbt as vbt

# Prepare data
start = '2019-01-01 UTC'  # crypto is in UTC
end = '2020-01-01 UTC'
btc_price = vbt.YFData.download('BTC-USD', start=start, end=end).get('Close')

print(btc_price.shape)


fast_ma = vbt.MA.run(btc_price, 10, short_name='fast')
slow_ma = vbt.MA.run(btc_price, 20, short_name='slow')

entries = fast_ma.ma_crossed_above(slow_ma)
print(entries)

exits = fast_ma.ma_crossed_below(slow_ma)
print(exits)

pf = vbt.Portfolio.from_signals(btc_price, entries, exits)
print(pf.total_return())