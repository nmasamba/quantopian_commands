

# To set the cost of trades, we can specify a commission model in initialize() using set_commission()
# By default (if a commission model is not specified), the following commission model is used:
set_commission(commission.PerShare(cost=0.0075, min_trade_cost=1))

# The default commission model charges $0.0075 per share, with a minimum trade cost of $1.
# Slippage and commission models can have an impact on the performance of a backtest.

# NB: not relevant to live trading (as this is determined by broker) but they are realistic and recommended for backtesting