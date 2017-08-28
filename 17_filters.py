
# A filter is a function from an asset and a moment in time to a boolean
# In Pipeline, Filters are used for narrowing down the set of securities included in a computation or in the final output of a pipeline
# There are two common ways to create a Filter: comparison operators and Factor/Classifier methods


# Comparison operators on Factors and Classifiers produce Filters
# The following example (on a Factor) produces a filter that returns True whenever the latest close price is above $20
last_close_price = USEquityPricing.close.latest
close_price_filter = last_close_price > 20

# this example produces a filter that returns True whenever the 10-day mean is below the 30-day mean
mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)
mean_close_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30)
mean_crossover_filter = mean_close_10 < mean_close_30


# Factor/Classifier Methods also return filters (i.e. no comparison operators)
# Example: The Factor.top(n) method produces a Filter that returns True for the top n securities of a given factor each day
# This filter returns True for exactly 200 securities which were in the top 200 by last close price across all known securities
last_close_price = USEquityPricing.close.latest
top_close_price_filter = last_close_price.top(200)


# The following filter returns True for securities with a 30-day avg dollar volume greater than $10m
from quantopian.pipeline.factors import AverageDollarVolume, SimpleMovingAverage

dollar_volume = AverageDollarVolume(window_length=30)
high_dollar_volume = (dollar_volume > 10000000)

def make_pipeline():

    mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)
    mean_close_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30)

    percent_difference = (mean_close_10 - mean_close_30) / mean_close_30

    dollar_volume = AverageDollarVolume(window_length=30)

    high_dollar_volume = (dollar_volume > 10000000)

    return Pipeline(
        columns={
            'percent_difference': percent_difference,
            'high_dollar_volume': high_dollar_volume
        },
    )
result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
result.head()


# To screen the output for only the values passing as True when filtered, pass the filter as the argument to screen
def make_pipeline():

  mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)
  mean_close_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30)

  percent_difference = (mean_close_10 - mean_close_30) / mean_close_30

  dollar_volume = AverageDollarVolume(window_length=30)
  high_dollar_volume = (dollar_volume > 10000000)

  return Pipeline(
    columns={
      'percent_difference': percent_difference
    },
    screen=high_dollar_volume
  )
# Running this will produce an output only for only the securities that passed the high_dollar_volume
result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
print 'Number of securities that passed the filter: %d' % len(result) # ~2,100 securities on this day


# The ~ operator is used to invert a filter, swapping all True values with Falses and vice-versa
low_dollar_volume = ~high_dollar_volume












