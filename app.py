from flask import Flask
import dash
from dash import dcc, html
import seaborn as sns
import pandas as pd
import plotly.express as px

server = Flask(__name__)
app = dash.Dash(__name__,
                server=server,
                routes_pathname_prefix='/')

iris = sns.load_dataset('iris')
fig = px.scatter(iris,
                 x='sepal_length',
                 y='sepal_width',
                 color='species',
                 title='Exemplo de Gráfico em Ciencia de Dados')

app.layout = html.Div([
    html.H1('Usando Dash em Flask'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)