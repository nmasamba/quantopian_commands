
# This is a basic way to manually reference hand-picked securities
# Two ways to manually select securities on Quantopian - sid() and symbol()

# sid() returns a security given a unique Security ID, best way to reference a security (robust to ticker changes)
# the reference is best stored in a context variable
def initialize(context):
	context.aapl = sid(24)


# symbol() returns a security given a ticker symbol, not recommended without setting a reference date
# not robust to ticker changes unless specified with a reference date like "set_symbol_lookup_date('YYYY-MM-DD')"
def initialize(context):
	context.aapl = symbol('AAPL')