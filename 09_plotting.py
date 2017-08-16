

# In the IDE, the record() function allows us to plot time series charts
# updated as frequently as daily in backtesting or as frequently as minutely in live trading
# up to 5 series can be recorded and plotted


# The following example plots the number of long positions in our portfolio as a series called 'num_long', and the number of short positions as 'num_short'.
def initialize(context):
    context.aapl = sid(24)
    context.spy = sid(8554)

    schedule_function(rebalance, date_rules.every_day(), time_rules.market_open())
    schedule_function(record_vars, date_rules.every_day(), time_rules.market_close())

def rebalance(context, data):
    order_target_percent(context.aapl, 0.50)
    order_target_percent(context.spy, -0.50)

def record_vars(context, data):

    long_count = 0
    short_count = 0

    for position in context.portfolio.positions.itervalues():
        if position.amount > 0:
            long_count += 1
        if position.amount < 0:
            short_count += 1

    # Plot the counts
    record(num_long=long_count, num_short=short_count)
