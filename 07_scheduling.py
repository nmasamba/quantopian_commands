
# schedule_function() allows us to schedule custom functions at regular intervals and allows us to specify interday frequency as well as intraday timing


# The following example schedules a function called rebalance() to run once per day, one hour after market open (usually 10:30AM ET).
schedule_function(func=rebalance, # rebalance() must be a function requiring context and data as arguments that we can define later in our algorithm.
                  date_rules=date_rules.every_day(),
                  time_rules=time_rules.market_open(hours=1))


# Note: The relative date and time rules that we specify will follow the trading calendar that we selected. 
# For example, date_rules.market_open() will usually run in the 9:30AM ET minute bar if we selected the US equity calendar.
# If you are only trading equities, you will want to use the US Equities Calendar. 
# If you would like to include futures in your algorithm, you will need to use the US Futures Calendar. 


# Another example to run a custom function weekly_trades(), on the last trading day of each week, 30 minutes before market close
schedule_function(weekly_trades, date_rules.week_end(), time_rules.market_close(minutes=30))



# The following clonable example takes a long position in SPY at the start of the week, 
# and closes out the position at 3:30pm on the last day of the week:
def initialize(context):
    context.spy = sid(8554)
    schedule_function(open_positions, date_rules.week_start(), time_rules.market_open())
    schedule_function(close_positions, date_rules.week_end(), time_rules.market_close(minutes=30))
def open_positions(context, data):
    order_target_percent(context.spy, 0.10)
def close_positions(context, data):
    order_target_percent(context.spy, 0)


# NB: schedule_function() uses relative times and dates to account for market holidays. 
# A backtest or live algorithm only ever runs on trading days. Market half-days can be skipped by passing half_days=False as a final keyword argument to schedule_function(). 
# For more information, and a full list of date_rules and time_rules, check out the documentation.

