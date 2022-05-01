import dash
#import dash_core_components as dcc
from dash import dcc
#import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/UnemploymentRates.csv')

app = dash.Dash()

# Bar chart data
barchart_df = df1#[df1['Country'] == 'US']
barchart_df = barchart_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
barchart_df = barchart_df.groupby(['year'])['unemployed'].sum().reset_index()
barchart_df = barchart_df.sort_values(by=['unemployed'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=barchart_df['year'], y=barchart_df['unemployed'])]

# Stack bar chart data
stackbarchart_df = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
stackbarchart_df['unemployed'] = stackbarchart_df['population'] - stackbarchart_df['employed_total']
#stackbarchart_df = stackbarchart_df[(stackbarchart_df['Country'] != 'China')]
stackbarchart_df = stackbarchart_df.groupby(['year']).agg(
    {'population': 'sum', 'employed_total': 'sum', 'unemployed': 'sum'}).reset_index()
stackbarchart_df = stackbarchart_df.sort_values(by=['population'], ascending=[False]).head(20).reset_index()
trace1_stackbarchart = go.Bar(x=stackbarchart_df['year'], y=stackbarchart_df['unemployed'], name='Unemployed',
                              marker={'color': '#CD7F32'})
trace3_stackbarchart = go.Bar(x=stackbarchart_df['year'], y=stackbarchart_df['employed_total'], name='Employed',
                              marker={'color': '#FFD700'})
data_stackbarchart = [trace1_stackbarchart, trace3_stackbarchart]

# Line Chart
line_df = df1
#line_df['year'] = pd.to_datetime(line_df['Date'])
data_linechart = [go.Scatter(x=line_df['year'], y=line_df['unemployed'], mode='lines', name='Unemployed')]

# Multi Line Chart
multiline_df = df1
#multiline_df['year'] = pd.to_datetime(multiline_df['Date'])
trace1_multiline = go.Scatter(x=multiline_df['year'], y=multiline_df['unemployed'],
mode='lines', name='Unemployed')
trace2_multiline = go.Scatter(x=multiline_df['year'], y=multiline_df['employed_total'], mode='lines', name='Employed')
trace3_multiline = go.Scatter(x=multiline_df['year'], y=multiline_df['population'], mode='lines', name='Population')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]

# Bubble chart
bubble_df = df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
bubble_df['unemployed'] = bubble_df['population'] - bubble_df['employed_total']
#bubble_df = bubble_df[(bubble_df['Country'] != 'China')]
bubble_df = bubble_df.groupby(['year']).agg(
    {'population': 'sum', 'employed_total': 'sum', 'unemployed': 'sum'}).reset_index()
data_bubblechart = [
    go.Scatter(x=bubble_df['employed_total'],
               y=bubble_df['unemployed'],
               text=bubble_df['year'],
               mode='markers',
               marker=dict(size=bubble_df['population'] / 200, color=bubble_df['population'] / 200, showscale=True))
]

# Heatmap
data_heatmap = [go.Heatmap(x=df1['year'],
                           y=df1['unemployed'],
                           z=df1['unemployed_percent'].values.tolist(),
                           colorscale='Jet')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Cream Frogs',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Final Project for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('US Employment and Unemployment rates since 1940', style={'textAlign': 'center'}),
    html.Br(),
    #html.Br(),
    #html.Hr(style={'color': '#7FDBFF'}),
    #html.H3('Interactive Bar chart', style={'color': '#df1e56'}),
    #html.Div('This bar chart represent the US Employment and Unemployment rates since 1940.'),
    #dcc.Graph(id='graph1'),
    #html.Div('Please select a continent', style={'color': '#ef3e18', 'margin':'10px'}),
    #dcc.Dropdown(
    #    id='select-continent',
    #    options=[
    #        {'label': 'Asia', 'value': 'Asia'},
    #        {'label': 'Africa', 'value': 'Africa'},
    #        {'label': 'Europe', 'value': 'Europe'},
    #        {'label': 'North America', 'value': 'North America'},
    #        {'label': 'Oceania', 'value': 'Oceania'},
    #        {'label': 'South America', 'value': 'South America'}
    #    ],
    #    value='Europe'
    #),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the US Employment and Unemployment rates since 1940.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='US Employment and Unemployment rates since 1940',
                                      xaxis={'title': 'year'}, yaxis={'title': 'Unemployed'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represent the US Employment and Unemployment rates since 1940.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='US Employment and Unemployment rates since 1940',
                                      xaxis={'title': 'year'}, yaxis={'title': 'Percent of Unemployed'},
                                      barmode='stack')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the US Employment and Unemployment rates since 1940.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='US Employment and Unemployment rates since 1940',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Percent of Unemployed'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represent the US Employment and Unemployment rates since 1940.'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='US Employment and Unemployment rates since 1940',
                      xaxis={'title': 'Year'}, yaxis={'title': 'Percent of Unemployed'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
    html.Div(
        'This bubble chart represent the US Employment and Unemployment rates since 1940.'),
    dcc.Graph(id='graph6',
figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title='US Employment and Unemployment rates since 1940',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Percent of Unemployed'},
                                      hovermode='closest')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represent the US Employment and Unemployment rates since 1940.'),
    dcc.Graph(id='graph7',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='US Employment and Unemployment rates since 1940',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Percent of Unemployed'})
              }
              )
])


if __name__ == '__main__':
    app.run_server()