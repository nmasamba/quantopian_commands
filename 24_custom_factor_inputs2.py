
# Let's take another example where we build a momentum custom factor and use it to create a filter.
# We will then use that filter as a screen on our pipeline.


# Let's start by defining a Momentum factor to be the division of the most recent close price by the close price from n days ago where n is the window_length.
from quantopian.pipeline import CustomFactor, Pipeline
import numpy

class Momentum(CustomFactor):
    # Default inputs
    inputs = [USEquityPricing.close]

    # Compute momentum
    def compute(self, today, assets, out, close):
        out[:] = close[-1] / close[0]

# instantiate the filter twice to create a 10-day and 20-day momentum filter
# also create a filter to return True for securities with both a positive 10-day momentum and a positive 20-day momentum.
ten_day_momentum = Momentum(window_length=10)
twenty_day_momentum = Momentum(window_length=20)
positive_momentum = ((ten_day_momentum > 1) & (twenty_day_momentum > 1))

# Add custom momentum factors to make_pipeline. 
# Set positive_momentum to be the screen of the pipeline
def make_pipeline():

    ten_day_momentum = Momentum(window_length=10)
    twenty_day_momentum = Momentum(window_length=20)

    positive_momentum = ((ten_day_momentum > 1) & (twenty_day_momentum > 1))

    std_dev = StdDev(inputs=[USEquityPricing.close], window_length=5)

    return Pipeline(
        columns={
            'std_dev': std_dev,
            'ten_day_momentum': ten_day_momentum,
            'twenty_day_momentum': twenty_day_momentum
        },
        screen=positive_momentum
    )
result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
result.head() # Running this pipeline outputs the standard deviation and each of our momentum computations for securities with positive 10-day and 20-day momentum.
