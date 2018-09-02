#!/usr/bin/env python3
import plotly.graph_objs as go
import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='khecht', api_key='d7LfPjC5htWFMBOQmgyG')
import numpy as np
import pandas as pd

# Parse command line

DF = pd.read_csv('User Data.csv')

# Dorm Locations on given map
locations = {
		'WF' : [4.25, 7.5],
		'Cavanaugh': [5.4, 14.3],
		'McGlinn':[3.3,8.5],
		'PW':[6.4,15.5],
		'PE':[6.8,15.5],
		'Flaherty':[7.3,14.75],
		'Farley':[5.8,15],
		'Lyons':[3.1,12],
		'Lewis':[4.6,16.2],
		'Walsh':[4.4, 12],
		'Howard':[3.6,12],
		'BP':[5.8,14.2],
		'Badin':[3.8,11.75],
		'Ryan':[4.25, 7.5]
		}

# declare x and y valued lists
L_x = []
L_y = []
# Fill x and y valued lists
for dorm in list(DF['Dorm']):
	L_x.append(locations[dorm][0])
	L_y.append(locations[dorm][1])
# Access trace of the locations 
trace = go.Scatter(
		x = L_x,
		y = L_y,
		mode='markers',
		marker=dict(
			size='16',
			color = np.random.randn(500), #set color equal to a variable
			colorscale='Viridis',
			showscale=True
			)
		)
# Background Image
layout= go.Layout(images= [dict(
	# ND Campus image
	source= 'https://cdn.vox-cdn.com/uploads/chorus_asset/file/9124603/Screen_Shot_2017_08_27_at_4.15.18_PM.png',  
	xref = "x",
	yref= "y",
	x= 1.7,
	y= 30,
	sizex= 30,
	sizey= 30,
	sizing= "fit",
	opacity= 1,
	layer= "below")])
# Plot
fig=go.Figure(data=[trace],layout=layout)
#plot_url = py.iplot(fig, filename='my plot')
py.image.save_as(fig, filename='my-plot.png')
