
# The Quantopian Pipeline API makes it possible to dynamically buy securities based on specific computations
# There are three types of computations that can be expressed in a pipeline: factors, filters, and classifiers.
# Pipeline computations can be performed using pricing (OHLC) and volume data, fundamental data, or partner data


# In this tutorial, we will build up to a pipeline that selects liquid securities with large changes between their 10-day and 30-day average prices.


# import necessary libraries
from quantopian.pipeline import Pipeline
from quantopian.research import run_pipeline

# function to create a pipeline
def make_pipeline():
    return Pipeline()

# instantiate the pipeline and save to my_pipe
my_pipe = make_pipeline()

# run the pipeline for one day and save to result
result = run_pipeline(my_pipe, '2015-05-05', '2015-05-05')

# output the top results of the day's pipeline, these will have no columns as they received an empty pipeline from make_pipeline()
result.head()