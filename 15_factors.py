
# A factor is a function from an asset and a moment in time to a number, i.e. f(asset, timestamp) --> numerical value
# In Pipeline, Factors are the most commonly-used term, representing the result of any computation producing a numerical result
# Factors require a column of data as well as a window length as input.


# The simplest factors in Pipeline are built-in Factors
# let's make a factor that computes the average close price of each asset over a trailing 10-day window
# we need to import our built-in SimpleMovingAverage factor and the USEquityPricing dataset.
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import SimpleMovingAverage


# create s factor for computing the 10-day mean close price of securities.
mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)

# add the factor to a pipeline (which you first need to make)
# you need to pass in the factor as column data for the computation
def make_pipeline():

  mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)

  return Pipeline(
    columns={
      '10_day_mean_close': mean_close_10
    }
  )

# to see what this looks like
result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
result.head()

# factors can also be added to an existing Pipeline instance using the Pipeline.add method
my_pipe = Pipeline()
f1 = SomeFactor(...)
my_pipe.add(f1)



# The most commonly used built-in Factor is Latest
# Latest factor gets the most recent value of a given data column
def make_pipeline():

    mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)
    latest_close = USEquityPricing.close.latest

    return Pipeline(
        columns={
            '10_day_mean_close': mean_close_10,
            'latest_close_price': latest_close
        }
    )
result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
result.head()
# NB: .latest can sometimes return things other than Factors. We'll see examples of other possible return types in later lessons


# Some factors have default inputs that should never be changed. 
# For example the VWAP built-in factor is always calculated from USEquityPricing.close and USEquityPricing.volume, so no need to specify these default BoundColumns
from quantopian.pipeline.factors import VWAP
vwap = VWAP(window_length=10)




