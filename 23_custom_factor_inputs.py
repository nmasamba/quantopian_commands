
# When writing a custom factor, we can set default inputs and window_length in our CustomFactor subclass
# TenDayMeanDifference custom factor to compute the mean difference between two data columns over a trailing window using numpy.nanmean
# Let's set the default inputs to [USEquityPricing.close, USEquityPricing.open] and the default window_length to 10:


from quantopian.pipeline import CustomFactor, Pipeline
import numpy

class TenDayMeanDifference(CustomFactor):
    # Default inputs.
    inputs = [USEquityPricing.close, USEquityPricing.open]
    window_length = 10
    def compute(self, today, asset_ids, out, close, open):
        # Calculates the column-wise mean difference, ignoring NaNs
        out[:] = numpy.nanmean(close - open, axis=0)

# Instantiate in make_pipeline() and call the custom factor
# This call will now use default inputs 10-day mean difference between the daily open and close prices.
close_open_diff = TenDayMeanDifference()

# This call will override defaults to compute the 10-day mean difference between the daily high and low prices (using given arguments).
high_low_diff = TenDayMeanDifference(inputs=[USEquityPricing.high, USEquityPricing.low])



