
# Sometimes we want to ignore certain assets when computing pipeline expresssions
# Maybe we want to compute an expression that's computationally expensive, and we know we only care about results for certain assets
# Or we want to compute an expression that performs comparisons between assets, but we only want those comparisons to be performed against a subset of all assets
# To support these two use-cases, all Factors and many Factor methods can accept a mask argument
# The mask argument must be a Filter indicating which assets to consider when computing


def make_pipeline():

    # Dollar volume factor
    dollar_volume = AverageDollarVolume(window_length=30)

    # High dollar volume filter
    high_dollar_volume = dollar_volume.percentile_between(90,100)

    # Top open securities filter (high dollar volume securities)
    top_open_price = USEquityPricing.open.latest.top(50, mask=high_dollar_volume)

    # Top percentile close price filter (high dollar volume, top 50 open price)
    high_close_price = USEquityPricing.close.latest.percentile_between(90, 100, mask=top_open_price)

    return Pipeline(
        screen=high_close_price
    )
result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
print 'Number of securities that passed the filter: %d' % len(result) # only 5 securities pass this filter

# applying masks in layers as we did above can be thought of as an "asset funnel"