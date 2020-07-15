import numpy as np

from bokeh.io import curdoc
# from bokeh.layouts import row, widgetbox
# from bokeh.models import ColumnDataSource
# from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure


# # Set up data
DATASET_NAME = 'customers_labeled'

# # Get dataset
import dataiku
df = dataiku.Dataset(DATASET_NAME)
df = df.get_dataframe(limit = 10000)
df = df.set_index(df['customerID'], drop = True)

# Run TSNE
# To do -- copy code from notebook
# For now, just do this to make a plot
df = df[['age_first_order','pages_visited_avg']]

# Make plot 
p = figure( plot_height=250)
x = [1,2,3]
y = [1,2,3]
# x = df.age_first_order
# y = df.pages_visited_avg
p.scatter(x,y)
