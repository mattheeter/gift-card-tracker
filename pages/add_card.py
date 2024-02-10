import dash
from dash import Dash, html, callback, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import psycopg
import json

with open("./db_credentials.json", "r") as file:
    credentials = json.load(file)

# Connecting to the database
connection = psycopg.connect(dbname=credentials["dbname"], user=credentials["username"], password=credentials["password"])
cursor = connection.cursor()

# Registering this page within the app
dash.register_page(__name__)

def layout():
    return html.Div([
        html.H1("Gift Card App", style={"textAlign": "center"}),
        dbc.Card(children=[
            dbc.CardBody([ # Card for adding a new gift card
                html.H4("Add a new card"), 
                html.Form(id="add_card_form", children=[
                    dbc.Input(id="card_provider", placeholder="Enter card provider", type="text"),
                    dbc.Input(id="card_number", placeholder="Enter card number", pattern=r'^[0-9]{12,24}$', type="text"),
                    dbc.Input(id="card_pin", placeholder="Enter card pin", pattern=r'^[0-9]{4,10}$', type="text"),
                    dbc.Input(id="card_balance", placeholder="Enter card balance", pattern=r'^[0-9]+(?:\.[0-9]{1,2})?$', type="text"),
                    dbc.Button("Add card", id="add_card_button", type="submit", color="primary", className="mr-1")
                ])
            ])
        ])
    ])

# @callback(    
#     Output("add_card_form", "children"),
#     Input("add_card_button", "n_clicks"),
#     Input("card_provider", "value"),
#     Input("card_balance", "value"),
#     Input("card_pin", "value")
# )
# def add_card(_, card_provider, card_number, card_pin):
#    """Add a new card to the database."""
#    pass 

cursor.close()
connection.close()