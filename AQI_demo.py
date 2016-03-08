from pymongo import MongoClient
import json
import pandas as pd

uri = 'mongodb://mongo:27017/AQI_DEMO'
client = MongoClient(uri)

data = pd.read_csv('./test')
data_json = json.loads(data.to_json(orient="records"))
posts = client.AQI_DEMO

posts.test.insert_one({'X2016-02-28': 48,
 'X2016-02-29': 53,
 'X2016-03-01': 158,
 'X2016-03-02': 212,
 'X2016-03-03': 333,
 'X2016-03-04': 365,
 'X2016-03-05': 170,
 '\ufeff"city_name"': '北京市'})
data
source_cols = data.columns
[s.replace('.','-') for s in source_cols]
data.columns = [s.replace('.','-') for s in source_cols]
data_list = data.columns[1:]
data_records = data[data_list].to_json(orient="records")
posts.test.insert_many(json.loads(data_records) )

data_value =  data[data_list].to_json(orient="values")
city_name = json.loads(data.T.to_json(orient="values"))[0]


import datetime
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import plotly.graph_objs as go
init_notebook_mode() 


data = [
    go.Heatmap(
        z=data_plot,
        x=date_lite,
        y=city_name,
        colorscale='Viridis',
    )
]

layout = go.Layout(
    title='AQI',
    xaxis = dict(ticks='', nticks=36),
    yaxis = dict(ticks='' )
)

fig = go.Figure(data=data, layout=layout)

url = iplot(fig)
