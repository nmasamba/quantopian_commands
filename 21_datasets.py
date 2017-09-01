
# When building a pipeline, we need a way to identify the inputs to our computations
# The input to a pipeline computation is specified using DataSets and BoundColumns


# DataSets are simply collections of objects that tell the Pipeline API where and how to find the inputs to computations
# An example of a DataSet that we have already seen is 
USEquityPricing


# A BoundColumn is a column of data that is concretely bound to a DataSet. Inputs to pipeline computations must be of type BoundColumn.
# An example of a BoundColumn that we have already seen is 
USEquityPricing.close 
# BoundColumns are most commonly used in CustomFactors
# The dtype of a BoundColumn tells a computation what the type of the data will be when the pipeline is run
# e.g. USEquityPricing has a float dtype


# Pricing data:
# US equity pricing data is stored in the USEquityPricing dataset which has the bound columns open, high, low, close, volume


# Fundamental data:
# Morningstar fundamental datasets are namespaced under the 
quantopian.pipeline.data.morningstar module
# morningstar datasets include balance_sheet, operation_ratios, valuation_ratios and earnings_report


# Partner data:
# These include corporate fundamental data, news sentiment, macroeconomic indicators, and more
# All datasets are namespaced under quantopian.pipeline.data e.g. 
quantopian.pipeline.data.psychsignal 
quantopian.pipeline.data.quandl 
# Similar to USEquityPricing, each of these datasets have columns (BoundColumns) that can be used in pipeline computations




