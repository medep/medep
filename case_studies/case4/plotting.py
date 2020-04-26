import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(go.Scatter(
    x = df['Date'],
    y = df['AAPL.High'],
))

fig.update_layout(
    title = 'Time Series with Custom Date-Time Format',
    xaxis_tickformat = '%d %B (%a)<br>%Y'
)

fig.show()