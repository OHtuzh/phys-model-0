import plotly.graph_objs as go
import numpy as np

# Параметры
####################################

b = 10 # величина магнитного поля (Тл)
s = 8 # площадь поперечного сечения проводника (м^2)
f = 3 # частота вращения (Гц)
r = 19 # сопротивление (Ом)
t = 20 # время (с)

####################################

step = t / 1000
newX = np.arange(0, t, step)
newEmfY = b * s * 2 * np.pi * f * np.sin(2 * np.pi * f * newX)
newIndY = newEmfY / r

min_val = min(np.min(newEmfY), np.min(newIndY))
max_val = max(np.max(newEmfY), np.max(newIndY))
yRange = [min_val - abs(min_val) / 10, max_val + abs(max_val) / 10]

trace1 = go.Scatter(
    x=newX, y=newEmfY, mode='lines+markers',
    marker=dict(color="yellow"),
    line=dict(color='yellow')
)
trace2 = go.Scatter(
    x=newX, y=newIndY, mode='lines+markers',
    marker=dict(color="yellow"),
    line=dict(color='yellow')
)

layout1 = go.Layout(
    title="ЭДС",
    xaxis=dict(title="Время, с"),
    yaxis=dict(title="ЭДС, В", range=yRange),
    plot_bgcolor='black'
)

layout2 = go.Layout(
    title="Индукционный ток",
    xaxis=dict(title="Время, с"),
    yaxis=dict(title="Индукционный ток, А", range=yRange),
    plot_bgcolor='black'
)

fig1 = go.Figure(data=[trace1], layout=layout1)
fig2 = go.Figure(data=[trace2], layout=layout2)

fig1.show()
fig2.show()
