
# The data object enables lookup of historical, current pricing and volume data for any security
# data is available in handle_data() as well as before_trading_start()

# data.current() can be used to retrieve the most recent value of a given field(s) for a given asset(s)
# data.current() requires two arguments: the asset or list of assets, and the field or list of fields being queried
# Possible query fields include 'price', 'open', 'high', 'low', 'close', and 'volume'
# output type will depend on the input types. To get the most recent price of AAPL, we can use:


data.current(sid(24), 'price')

# get the most recent price of AAPL and SPY (returned as a pandas Series indexed by asset):

data.current([sid(24), sid(8554)], ['low', 'high'])


# dta.can_trade() is used to determine if an asset(s) is currently listed on a supported exchange and can be ordered
# If data.can_trade() returns True for a particular asset in a given minute bar, we are able to place an order for that asset in that minute
# This is an important guard to have in our algorithm if we hand-pick the securities that we want to trade
# data,can_trade() requires a single argument: an asset or a list of assets. The following example checks if AAPL is currently listed on a major exchange:

data.can_trade(sid(24))
