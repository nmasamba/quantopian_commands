
# Large orders, or orders placed for illiquid securities can take some time to fill
# On Quantopian, the time it takes for an order to fill is determined by the slippage model being used
# When placing new orders, it's sometimes necessary to consider open orders
# When placing new orders, it's sometimes necessary to consider open orders, at the end of each trading day, all open orders are cancelled


# get_open_orders() which returns a dictionary of open orders keyed by assets
# use this to ensure that we don't have an open order for a security before we place a new order for it
def initialize(context):
    # Relatively illiquid stock.
    context.xtl = sid(40768)

def handle_data(context, data):
    # Get all open orders.
    open_orders = get_open_orders()

    if context.xtl not in open_orders and data.can_trade(context.xtl):
        order_target_percent(context.xtl, 1.0)