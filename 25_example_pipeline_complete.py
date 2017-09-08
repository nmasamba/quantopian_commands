
# This is an example of a full pipeline that can be used in an algorithm

from quantopian.pipeline import CustomFactor, Pipeline, numpy
from quantopian.pipeline.data import morningstar
from quantopian.pipeline.filters.morningstar import IsPrimaryShare
from quantopian.pipeline.factors import AverageDollarVolume, SimpleMovingAverage



# To start, let's first create a filter to narrow down the types of securities coming out of our pipeline.
# Note that when defining our filters, we used several Classifier methods that we haven't yet seen including notnull, startswith, endswith, and matches.
# Filter to select for securities that meet the following criteria:

# Is a primary share
primary_share = IsPrimaryShare()

# Is listed as a common stock
# 'ST00000001' indicates common stock.
common_stock = morningstar.share_class_reference.security_type.latest.eq('ST00000001')

# Is not a depositary receipt (ADR/GDR). Recall that ~ in an inverter.
not_depositary = ~morningstar.share_class_reference.is_depositary_receipt.latest

# Is not trading over-the-counter (OTC)
not_otc = ~morningstar.share_class_reference.exchange_id.latest.startswith('OTC')

# Is not when-issued (WI)
not_wi = ~morningstar.share_class_reference.symbol.latest.endswith('.WI')

# Doesn't have a name indicating it's a limited partnership (LP). The .matches does a match using a regular expression
not_lp_name = ~morningstar.company_reference.standard_name.latest.matches('.* L[. ]?P.?$')

# Doesn't have a company reference entry indicating it's a LP
not_lp_balance_sheet = morningstar.balance_sheet.limited_partnership.latest.isnull()

# Is not an ETF (has Morningstar fundamental data)
have_market_cap = morningstar.valuation.market_cap.latest.notnull()

# Filter for stocks that pass all of our previous filters.
tradeable_stocks = (
    primary_share
    & common_stock
    & not_depositary
    & not_otc
    & not_wi
    & not_lp_name
    & not_lp_balance_sheet
    & have_market_cap
)

# Next, let's create a filter for the top 30% of tradeable stocks by 20-day average dollar volume. We'll call this our base_universe.
base_universe = AverageDollarVolume(window_length=20, mask=tradeable_stocks).percentile_between(70, 100)

# Alternatively, we could use one of Quantopian's built-in base universe filter:
# from quantopian.pipeline.filters.morningstar import Q1500US
# base_universe = Q1500US()


# Now that we have a filter base_universe that we can use to select a subset of securities, let's focus on creating factors for this subset
# In this strategy, we'll look at the 10-day and 30-day moving averages (close price). 
# Let's plan to open equally weighted long positions in the 25 securities with the least (most negative) percent difference and equally weighted short positions in the 25 with the greatest percent difference.
# 10-day close price average.
mean_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10, mask=base_universe)

# 30-day close price average.
mean_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30, mask=base_universe)

percent_difference = (mean_10 - mean_30) / mean_30

# Next, let's create filters for the top 25 and bottom 25 equities by percent_difference.
# Create a filter to select securities to short.
shorts = percent_difference.top(25)

# Create a filter to select securities to long.
longs = percent_difference.bottom(25)

# Let's then combine shorts and longs to create a new filter that we can use as the screen of our pipeline:
securities_to_trade = (shorts | longs)

# Finally we instantiate our pipeline
# the only information that we actually need from our pipeline is which securities we want to trade (the pipeline index) and whether or not to open a long or a short position.
def make_pipeline():

    # Base universe filter.
    base_universe = Q1500US()

    # 10-day close price average.
    mean_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10, mask=base_universe)

    # 30-day close price average.
    mean_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30, mask=base_universe)

    # Percent difference factor.
    percent_difference = (mean_10 - mean_30) / mean_30

    # Create a filter to select securities to short.
    shorts = percent_difference.top(25)

    # Create a filter to select securities to long.
    longs = percent_difference.bottom(25)

    # Filter for the securities that we want to trade.
    securities_to_trade = (shorts | longs)

    return Pipeline(
      columns={
        'longs': longs,
        'shorts': shorts
      },
      screen=securities_to_trade
    )
result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
result.head()    




















