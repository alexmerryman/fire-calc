import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.DataFrame.from_dict({'date': ['1/1/2020', '2/1/2020', '3/1/2020', '4/1/2020', '6/1/2020', '12/1/2020',
                                      '6/1/2021', '12/1/2021', '6/1/2022', '12/1/2022', '6/1/2023', '12/1/2023',
                                      '6/1/2024', '12/1/2024', '6/1/2025', '12/1/2025', '6/1/2026', '12/1/2026',
                                      '6/1/2027', '12/1/2027', '6/1/2028', '12/1/2028', '6/1/2029', '12/1/2029',
                                      '6/1/2030', '12/1/2030', '6/1/2031', '12/1/2031', '6/1/2032', '12/1/2032',
                                      '6/1/2033', '12/1/2033', '6/1/2034', '12/1/2034', '6/1/2035', '12/1/2035',
                                      '6/1/2036', '12/1/2036', '6/1/2037', '12/1/2037', '6/1/2038', '12/1/2038'],
                             'assets': [8000, 9500, 11000, 13000, 13000, 13000]*7,
                             'liabilities': [-10000, -9000, -7500]*2*7})


# churn_trace_text = {True: 'Churned',
#                     False: "Didn't churn"}


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
                          dict(x=df['date'], y=df['assets'], type='line', name='Assets'),
                          dict(x=df['date'], y=df['liabilities'], type='line', name='Liabilities'),
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