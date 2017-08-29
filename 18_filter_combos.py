
# Combining filters is done using the & (and) and | (or) operators
# This filter will evaluate to True for securities where both high_dollar_volume and above_20 are True
# If we want to use this filter as a screen in our pipeline, we can set the screen to be is_tradeable
def make_pipeline():

    mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)
    mean_close_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30)

    percent_difference = (mean_close_10 - mean_close_30) / mean_close_30

    dollar_volume = AverageDollarVolume(window_length=30)
    # Note: percentile_between is a Factor method returning a Filter
    high_dollar_volume = dollar_volume.percentile_between(90, 100)

    latest_close = USEquityPricing.close.latest
    above_20 = latest_close > 20

    is_tradeable = high_dollar_volume & above_20

    return Pipeline(
        columns={
            'percent_difference': percent_difference
        },
        screen=is_tradeable
    )
# This screened filter outputs about 737 securities
result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
print 'Number of securities that passed the filter: %d' % len(result)

