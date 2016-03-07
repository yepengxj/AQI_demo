import pandas as pd
data = pd.read_csv('./test')
date_lite = ['X2016.02.28','X2016.03.01','X2016.03.02','X2016.03.03','X2016.03.04','X2016.03.05']
data_plot = json.loads(data[date_lite].to_json(orient="values"))
#data[].to_json(orient="values")
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
    title='GitHub commits per day',
    xaxis = dict(ticks='', nticks=36),
    yaxis = dict(ticks='' )
)

fig = go.Figure(data=data, layout=layout)

url = iplot(fig)
