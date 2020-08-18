library(dataiku)

# Recipe inputs
customers_orders_joined <- dkuReadDataset("customers_orders_joined", samplingMethod="head", nbRows=100000)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a R dataframe or data table
r_instead_of_prep <- customers_orders_joined # For this sample code, simply copy input to output


# Recipe outputs
dkuWriteDataset(r_instead_of_prep,"r_instead_of_prep")
