
# Several functions can be used to order securities through the Quantopian API
# This tutorial focuses on the order_target_percent() function

# order_target_percent() allows you to order securities to a target percent of our portfolio value
# requires two arguments - asset to order and target percent of portfolio
# the following takes a long pos in Apple worth 60% of portfolio, and a short pos in SPY ETF worth 40% of portfolio value
def initialize(context):
	context.aapl = sid(24)
	context.spy = sid(8554)

def handle_data(context, data):
	# NB: can_trade() explained in next lesson
	if data.can_trade(context.aapl):
		order_target_percent(context.aapl, 0.6)
	# minus sign to indicate short position
	if data.can_trade(context.spy):
		order_target_percent(context.spy, -0.4)
