import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/UnemploymentRates.csv')

app = dash.Dash()

# Bar chart data
fig = px.bar(df1, x='year', y='unemployed_percent', color="unemployed",
             labels={
                 "year": "Year",
                 "unemployed_percent": "Percent Unemployed",
                 "unemployed": "Total Unemployed"
             },
             title="US Unemployment rates since 1940")

# Layout
app.layout = html.Div(children=[
    html.H1(children='Cream Frogs',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Final Project for Data Visualization using Python', style={'textAlign': 'center', 'fontSize': '20px'}),
    html.Br(),
    dcc.Graph(id="graph", figure=fig),
])

# Run layout
app.run_server()