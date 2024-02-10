import dash
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import psycopg
import json

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)

app.layout = html.Div([
    html.H1('Gift Card Tracker'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])
    
if __name__ == '__main__':
    app.run_server(debug=True)
