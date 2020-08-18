# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
customers_labeled = dataiku.Dataset("customers_labeled")
customers_labeled_df = customers_labeled.get_dataframe()

print('hi, webinar attendees!')

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

pyout_df = customers_labeled_df # For this sample code, simply copy input to output


# Write recipe outputs
pyout = dataiku.Dataset("pyout")
pyout.write_with_schema(pyout_df)
