
# portfolio object stores important information about our portfolio
# portfolio object is stored in context
# we'll focus on the positions attribute of the portfolio object in this tutorial


# current positions are stored in context.portfolio.positions. (similar to a Python dictionary with assets as keys, and Position objects as values)
# it can be useful to reference our current positions and iterate over the keys if we want to close out all of our open positions
	for security in context.portfolio.positions:
  		order_target_percent(security, 0)


# The following is a testable example which can be used to print portfolio positions daily at market close.
def initialize(context:
	context.aapl = sid(24)
	context.spy = sid(8554)

	schedule_function(rebalance, date_rules.every_day(), time_rules.market_open())
	schedule_function(print_pos, date_rules.every_day(), time_rules.market_close())

def rebalance(context, data):
	order_target_percent(context.aapl, 0.5)
	order_target_percent(context.spy, -0.5)

def print_pos(context, data):
	positions = context.portfolio.positions

	print positions.keys()





