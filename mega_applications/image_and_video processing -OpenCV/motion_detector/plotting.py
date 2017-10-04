from motion_detector import df #import data
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

# convert columns to desired datetime formats
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

# create figure object
p=figure(x_axis_type='datetime', height=100, width=500, responsive=True, title="Motion Graph")
# styling
p.yaxis.minor_tick_line_color=None
# remove ticks on yaxis
p.ygrid[0].ticker.desired_num_ticks=1
# add a hover tool
hover = HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

# plot a quadrant chart
q = p.quad(left="Start", right="End",bottom=0, top=1, color="orange",source=cds)



output_file("graph_2.html",mode='inline')

show(p)
