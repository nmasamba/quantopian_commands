# In Quantopian, a trading algorithm is a Python program that defines two special functions: initialize() and handle_data().

# initialize() is called once at the start of the program
# performs startup logic setting
def initialize(context):
	# Reference to Apple
	context.aapl = sid(24)


# handle_data() is called once per minute during the runtime of the program in events that are referred to as 'bars'
# decides what orders to place (if any) every minute
def handle_data(context, data):
	# 100% of portfolio to be long in AAPL
	order_target_percent(context.aapl, 1.00)


# before_trading_start() is called once per day before the market opens and requires context and data as input
# typically used to select which securities to order