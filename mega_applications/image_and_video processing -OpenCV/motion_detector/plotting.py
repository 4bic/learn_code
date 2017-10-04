from motion_detector import df #import data
from bokeh.plotting import figure, output_file, show

# create figure object
p=figure(x_axis_type='datetime', height=100, width=500, responsive=True, title="Motion Graph")
# plot a quadrant chart
q = p.quad(left=df["Start"], right=df["End"],bottom=0, top=1, color="orange")

output_file("graph.html",mode='inline')

show(p)
