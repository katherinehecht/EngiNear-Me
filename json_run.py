#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import pylab as plt
import plotly.graph_objs as go
import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='khecht', api_key='d7LfPjC5htWFMBOQmgyG')
import numpy as np
import pandas as pd
import collections
import requests
import json
from pandas.tools.plotting import table

URL = 'https://getsimpleform.com/messages.json?api_token=9e8867546d012b0953bcaf56ec014b30'

# Fetch Data
response = requests.get(URL)
data = response.json()

dorms = [_['data']['dorm'] for _ in data]
count = collections.Counter()
count.update(dorms)

#values = [_['data'] for _ in data]

#for x in values:
#	print(x['name'])

#raise SystemExit

#print(data[0]['data']['name'])
# Dorm Locations on given map
locations = {
		'Welsh Family Hall' : [4.25, 7.5],
		'Cavanaugh Hall': [5.4, 14.3],
		'McGlinn Hall':[3.3,8.5],
		'Pasquerilla West Hall':[6.4,15.5],
		'Pasquerilla East Hall':[6.8,15.5],
		'Flaherty Hall':[7.3,14.75],
		'Farley Hall':[5.8,15],
		'Lyons Hall':[3.1,12],
		'Lewis Hall':[4.6,16.2],
		'Walsh Hall':[4.4, 12],
		'Howard Hall':[3.6,12],
		'Breen-Phillips Hall':[5.8,14.2],
		'Badin Hall':[3.8,11.75],
		'Ryan Hall':[4.25, 7.5]
		}

# declare x and y valued lists
L_x = []
L_y = []
# Fill x and y valued lists
for dorm in dorms:
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
			colorscale='Jet',
			showscale=True
			colorbar=ColorBar(
				title='Number of Girls'
				),
			mode='markers'
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
	layer= "below",
	xaxis=dict(
		autorange=True,
		showgrid=False,
		zeroline=False,
		showline=False,
		autotick=False,
		ticks='',
		showticklabels=False
		),
	yaxis=dict(
		autorange=True,
		showgrid=False,
		zeroline=False,
		showline=False,
		autotick=False,
		ticks='',
		showticklabels=False
		)
	)])
# Plot
fig=go.Figure(data=[trace],layout=layout)
#plot_url = py.iplot(fig, filename='my plot')
py.image.save_as(fig, filename='my-plot.png')


dorms = [_['data']['dorm'] for _ in data]
names = [_['data']['name'] for _ in data]
years = [_['data']['year'] for _ in data]
majors = [_['data']['major'] for _ in data]
ids = [_['data']['netid'] for _ in data]


table_data = {
		'Name': names,
		'Dorm': dorms,
		'Year': years,
		'Major': majors,
		'NetID': ids
		}

df = pd.DataFrame(table_data)
plt.savefig('all_table.png')
# Table by Year


# Table by Dorm


# Table by Major



