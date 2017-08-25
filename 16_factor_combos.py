
# Factors can be combined, both with other Factors and with scalar values
# For example, constructing a Factor that computes the average of two other Factors is simply:
f1 = SomeFactor(...)
f2 = SomeOtherFactor(...)
average = (f1 + f2) / 2.0


# Let's create a pipeline that creates a percent_difference factor by combining a 10-day average price factor and a 30-day one
# Step 1: make the 2 factors (after importing their libs):
mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)
mean_close_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30)

# Step 2: create a percent difference factor by combining our mean_close_30 factor with our mean_close_10 factor
percent_difference = (mean_close_10 - mean_close_30) / mean_close_30

# percent_difference is still a Factor even though it's composed as a combination of more primitive factors so we can add percent_difference as a column in our pipeline
# Step 3: define make_pipeline() to create a pipeline with percent_difference as a column
def make_pipeline():

    mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)
    mean_close_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30)

    percent_difference = (mean_close_10 - mean_close_30) / mean_close_30

    return Pipeline(
        columns={
            'percent_difference': percent_difference
        }
    )
result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
result.head()