

# Slippage occurs because trade orders do not necessarily fill instantaneously
# Buy orders drive prices up, and sell orders drive prices down; this is generally referred to as the price_impact() of a trade
# Fill rates are dependent on the order size and current trading volume of the ordered security
# The volume_limit determines the fraction of a security's trading volume that can be used by your algorithm

# By default (if a slippage model is not specified in initialize()), the following volume share slippage model is used:
set_slippage(slippage.VolumeShareSlippage(volume_limit=0.025, price_impact=0.1))

# NB: not relevant to live trading (as this is determined by broker) but they are realistic and recommended for backtesting