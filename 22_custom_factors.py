
# Frequently, a desired computation isn't included as a built-in factor
# Pipeline API allows us to define our own custom factors
# Let's take an example of a computation that doesn't exist as a built-in: standard deviation


from quantopian.pipeline import CustomFactor, Pipeline
import numpy

# Custom factor to calculate the standard deviation over a trailing window using numpy.nanstd
# An instance of CustomFactor that’s been added to a pipeline will have its compute method called every day
class StdDev(CustomFactor):
    def compute(self, today, asset_ids, out, values):
    	# *inputs are M x N numpy arrays, where M is the window_length and N is the number of securities
    	# out is an empty array of length N. out will be the output of our custom factor each day. The job of compute is to write output values into out.
    	# asset_ids will be an integer array of length N containing security ids corresponding to the columns in our *inputs arrays.
    	# today will be a pandas Timestamp representing the day for which compute is being called.
        # Calculates the column-wise standard deviation, ignoring NaNs
        out[:] = numpy.nanstd(values, axis=0)

# instantiate custom factor in make_pipeline()
def make_pipeline():
    std_dev = StdDev(inputs=[USEquityPricing.close], window_length=5)

    return Pipeline(
        columns={
            'std_dev': std_dev
        }
    )
result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
result.head()