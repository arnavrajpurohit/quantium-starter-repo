import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load and process the data
df = pd.read_csv('output.csv')
df['date'] = pd.to_datetime(df['date'])

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div(
    style={'font-family': 'Arial, sans-serif', 'text-align': 'center'},
    children=[
        html.H1(
            children='Pink Morsel Sales Analysis',
            style={'color': '#5E35B1', 'margin-top': '20px'}
        ),
        html.P(
            children='Select a region to view sales data:',
            style={'font-size': '18px'}
        ),
        dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',  # Default value
            labelStyle={'display': 'inline-block', 'margin-right': '15px'},
            style={'margin-bottom': '20px'}
        ),
        dcc.Graph(id='sales-line-chart')
    ]
)

# Define the callback to update the graph
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-radio', 'value')]
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=f'Daily Sales of Pink Morsels in the {selected_region.capitalize()} Region',
    ).update_layout(
        xaxis_title="Date",
        yaxis_title="Sales"
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)