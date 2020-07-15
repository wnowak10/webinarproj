import numpy as np

# from bokeh.layouts import row, widgetbox
# from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
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
p = figure(plot_height=250)
x = df.age_first_order
y = df.pages_visited_avg
p.scatter(x,y)


from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox

from bokeh.models import HoverTool

hover = HoverTool()

hover.tooltips = [
    ("Sample", "@names"),
    ("Pressure", "@x_values mTorr"),
    ("Roughness", "@y_values nm"),
]

p.tools.append(hover)

text = TextInput(title="title", value='sine wave')

inputs = widgetbox(text)

curdoc().add_root(row(p, inputs))

# Give FIeld to input ID if they know it
# Or simply highlight point using toolip.


# plot = figure(plot_height=400, plot_width=400, title="my sine wave",
#               tools="crosshair,pan,reset,save,wheel_zoom",
#               x=x,y=y)

# from bokeh.models import HoverTool

# hover = HoverTool()

# hover.tooltips = [
#     ("Sample", "@names"),
#     ("Pressure", "@x_values mTorr"),
#     ("Roughness", "@y_values nm"),
# ]

# plot.tools.append(hover)



# # plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)


# # Set up widgets
# text = TextInput(title="title", value='sine wave')
# offset = Slider(title="offset", value=0.0, start=-5.0, end=5.0, step=0.1)
# amplitude = Slider(title="amplitude", value=1.0, start=-5.0, end=5.0)
# phase = Slider(title="phase", value=0.0, start=0.0, end=2*np.pi)
# freq = Slider(title="frequency", value=1.0, start=0.1, end=5.1)


# # Set up callbacks
# def update_title(attrname, old, new):
#     plot.title.text = text.value

# text.on_change('value', update_title)

# def update_data(attrname, old, new):

#     # Get the current slider values
#     a = amplitude.value
#     b = offset.value
#     w = phase.value
#     k = freq.value

#     # Generate the new curve
#     x = np.linspace(0, 4*np.pi, N)
#     y = a*np.sin(k*x + w) + b

#     source.data = dict(x=x, y=y)

# for w in [offset, amplitude, phase, freq]:
#     w.on_change('value', update_data)


# # Set up layouts and add to document
# inputs = widgetbox(text, offset, amplitude, phase, freq)

# curdoc().add_root(row(inputs, plot, width=800))
# curdoc().title = "Sliders"