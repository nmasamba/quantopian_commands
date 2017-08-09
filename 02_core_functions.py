
# A Quantopian algorithm has 3 core functions: initialize(), handle_data() and before_trading_start().

# initialize() is called exactly once when the algorithm starts and requires context as input
# context is an augmented Python dict used for maintaining state during trading, and can be referenced in different parts of the algo
# context should be used instead of global variables in the algorithm
# properties can be accessed using dot notation (context.some_property)
def initialize(context):
	context.message = 'hello'


# before_trading_start() is called before the market opens
# typically used to dynamically select which stocks to trade
def before_trading_start():
	pass


# handle_data() is called once at the END of each minute and requires context and data as input
# context is as above
# data is an object that stores several API functions
def handle_data(context, data):
	print context.message