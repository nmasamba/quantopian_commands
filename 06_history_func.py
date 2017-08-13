

# The data object has a history() function that allows us to get trailing windows of historical pricing or volume data
# requires 4 arguments: an asset or list of assets, a field or list of fields, an integer lookback window length, and a lookback frequency
# possible fields: fields include 'price', 'open', 'high', 'low', 'close', and 'volume'
# possible frequencies: '1d' for daily and '1m' for minutely


# Get the 10-day trailing price history of AAPL in the form of a Series.
hist = data.history(sid(24), 'price', 10, '1d')
# Mean price over the last 10 days.
mean_price = hist.mean()


# avoid partial data, e.g. To get the past 10 complete days of data, we can get an extra day of data, and drop the most recent row
data.history(sid(8554), 'volume', 11, '1d')[:-1].mean()


# Get the last 5 minutes of volume data for each security in our list.
hist = data.history([sid(24), sid(8554), sid(5061)], 'volume', 5, '1m')
# Calculate the mean volume for each security in our DataFrame.
mean_volumes = hist.mean(axis=0)


# Low and high minute bar history for each of our securities.
hist = data.history([sid(24), sid(8554), sid(5061)], ['low', 'high'], 5, '1m')
# Calculate the mean low and high over the last 5 minutes
means = hist.mean()
mean_lows = means['low']
mean_highs = means['high']


# The following example is clonable and can be backtested in the IDE. It prints the mean trading volume of a list of securities over the last 10 minutes:
def initialize(context):
    # AAPL, MSFT, SPY
    context.security_list = [sid(24), sid(8554), sid(5061)]

def handle_data(context, data):
    hist = data.history(context.security_list, 'volume', 10, '1m').mean()
    print hist.mean()