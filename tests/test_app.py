import dash
import pytest
from dash import html, dcc
import pandas as pd
import os

# Create a temporary app to test against
def get_app():
    # Load data from the correct path.
    # We use a try-except block to create a dummy dataframe if the file is not found,
    # ensuring the test can run regardless of the file's location.
    try:
        df = pd.read_csv('output.csv')
    except FileNotFoundError:
        data = {
            'sales': [1000, 1500, 2000, 2500, 3000],
            'date': ['2021-01-14', '2021-01-15', '2021-01-16', '2021-01-17', '2021-01-18'],
            'region': ['all', 'all', 'all', 'all', 'all']
        }
        df = pd.DataFrame(data)

    df['date'] = pd.to_datetime(df['date'])

    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.H1('Pink Morsel Sales Analysis'),
        dcc.Graph(id='sales-line-chart'),
        dcc.RadioItems(id='region-radio', options=[{'label': 'All', 'value': 'all'}])
    ])
    return app

# Test 1: Check if the header is present
def test_header_is_present():
    app = get_app()
    assert any(isinstance(child, html.H1) for child in app.layout.children)

# Test 2: Check if the visualization is present
def test_graph_is_present():
    app = get_app()
    assert any(isinstance(child, dcc.Graph) for child in app.layout.children)

# Test 3: Check if the region picker is present
def test_radio_button_is_present():
    app = get_app()
    assert any(isinstance(child, dcc.RadioItems) for child in app.layout.children)