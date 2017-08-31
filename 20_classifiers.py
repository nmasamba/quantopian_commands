
# A classifier is a function from an asset and a moment in time to a categorical output such as a string or integer label
# f(asset, timestamp) --> category


# An example of a classifier producing a string output is the exchange ID of a security
# First we'll have to import morningstar.share_class_reference.exchange_id and use the latest attribute to instantiate our classifier
from quantopian.pipeline.data import morningstar
# Since the underlying data of morningstar.share_class_reference.exchange_id
# is of type string, .latest returns a Classifier
exchange = morningstar.share_class_reference.exchange_id.latest


# Classifiers can also be used to produce filters with methods like isnull, eq, and startswith
# e.g. to select securities trading on the New York Stock Exchange, we can use the eq method of our exchange classifier
nyse_filter = exchange.eq('NYS')


# Classifiers can also be produced from various Factor methods
# The most general of these is the quantiles method, which accepts a bin count as an argument
# The quantiles classifier assigns a label from 0 to (bins - 1) to every non-NaN data point in the factor output
# NaNs are labeled with -1. Aliases are available for quartiles (quantiles(4)), quintiles (quantiles(5)), and deciles (quantiles(10)).
# As an example, this is what a filter for the top decile of a factor might look like:
dollar_volume_decile = AverageDollarVolume(window_length=10).deciles()
top_decile = (dollar_volume_decile.eq(9))

def make_pipeline():

    exchange = morningstar.share_class_reference.exchange_id.latest
    nyse_filter = exchange.eq('NYS')

    morningstar_sector = Sector()

    dollar_volume_decile = AverageDollarVolume(window_length=10).deciles()
    top_decile = (dollar_volume_decile.eq(9))

    return Pipeline(
        columns={
            'exchange': exchange,
            'sector_code': morningstar_sector,
            'dollar_volume_decile': dollar_volume_decile
        },
        screen=(nyse_filter & top_decile)
    )
result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
print 'Number of securities that passed the filter: %d' % len(result)
result.head()

# Classifiers are also useful for describing grouping keys for complex transformations on Factor outputs




