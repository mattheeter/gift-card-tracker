import dash
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import psycopg
import json 

dash.register_page(__name__)

def layout(): 
    return html.Div(["Welcome to the home page!"])