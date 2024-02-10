import dash
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import psycopg

layout = html.Div([
    html.H1("Gift Card App", style={"textAlign": "center"}),
    dbc.Card([dbc.CardBody([
       html.H4("Add a new card"), 
    ])])
    # html.Div([
    #     html.H2("Add a new user"),
    #     dbc.Input(id="username", placeholder="Enter username", type="text"),
    #     dbc.Input(id="email", placeholder="Enter email", type="email"),
    #     dbc.Input(id="password", placeholder="Enter password", type="password"),
    #     dbc.Button("Add user", id="add_user", color="primary", className="mr-1"),
    #     html.Div(id="user_added")
])
