import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from main_calc import main_calc

df = main_calc()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

available_indicators = df.columns.unique()

app.layout = html.Div([
    html.Div([
        html.Label('Annual Gross Salary (USD)'),
        dcc.Input(id='salary-input', value='0', type='text'),

        html.Label('Salary Growth'),
        dcc.Input(id='salary-growth', value='0', type='text'),

        html.Label('Market Return'),
        dcc.Input(id='market-return', value='0', type='text'),

        html.Label('Inflation'),
        dcc.Input(id='inflation', value='0', type='text'),

        html.Label('Savings Account APY'),
        dcc.Input(id='savings-apy', value='0', type='text'),

    ]),

    html.Div([
        dcc.Graph(id='net-worth-chart',
                  figure=dict(
                      data=[
                          dict(x=df['date'], y=df['Assets'], type='line', name='Assets'),
                          dict(x=df['date'], y=df['Liabilities'], type='line', name='Liabilities'),
                          dict(x=df['date'], y=df['Net Worth'], type='line', name='Net Worth')
                      ],
                      layout=dict(title='Net Worth', xaxis_title='Date'),
                  )
                  )
    ])
])

# @app.callback(
#     Output('indicator-graphic', 'figure'),
#     [Input('salary-input', 'value'),
#      Input('salary-growth', 'value'),
#      Input('market-return', 'value'),
#      Input('inflation', 'value'),
#      Input('savings-apy', 'value')])
# def update_graph(xaxis_column_name, yaxis_column_name):
#     return {
#         'data': [dict(
#             x=df[df['Churn'] == i][xaxis_column_name],
#             y=df[df['Churn'] == i][yaxis_column_name],
#             text=df['Churn'],
#             mode='markers',
#             marker={
#                 'size': 15,
#                 'opacity': 0.5,
#                 'line': {'width': 0.5, 'color': 'white'}
#             },
#             name=churn_trace_text[i]
#         ) for i in df.Churn.unique()],
#         'layout': dict(
#             xaxis={
#                 'title': xaxis_column_name
#             },
#             yaxis={
#                 'title': yaxis_column_name
#             },
#             margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
#             hovermode='closest'
#         )
#     }


if __name__ == '__main__':
    app.run_server(debug=True)