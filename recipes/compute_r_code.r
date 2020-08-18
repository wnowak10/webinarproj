library(dataiku)

# Recipe inputs
customers_labeled <- dkuReadDataset("customers_labeled", samplingMethod="head", nbRows=100000)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a R dataframe or data table
r_code <- customers_labeled # For this sample code, simply copy input to output


# Recipe outputs
dkuWriteDataset(r_code,"r_code")
