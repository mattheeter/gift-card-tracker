from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import psycopg
import json

with open("./credentials.json", "r") as file:
    credentials = json.load(file)

connection = psycopg.connect(dbname=credentials["dbname"], user=credentials["username"], password=credentials["password"])
cursor = connection.cursor()

# print(cursor.execute("SELECT * FROM users").fetchall())
# cursor.execute(f"INSERT INTO test_table(col_1) VALUES (%s);", (i,))
# connection.commit()
cursor.close()
connection.close()

app = Dash(__name__)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

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
    

if __name__ == '__main__':
    app.run_server(debug=True)
