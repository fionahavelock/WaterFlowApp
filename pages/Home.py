
#Dash Imports
from dash import Dash, dcc, html, Input, Output, ctx, State, dash_table, callback
import dash_bootstrap_components as dbc
import dash

#File Imports
from app import app
from APInrfa import *

def layout():
    return html.Div([
        dbc.Row([
        html.Div([
            html.Header([
                html.H4("North Pennines AONB Dashboard App Project"),
                html.H5(["This thesis is part of an ongoing project to develop a dashboard app that collates and visualizes water flow data from the North Pennines. The North Pennines is an area of outstanding natural beauty and ecological importance. The dashboard presented here can be seen as an initial developed concept for the project. This design demonstrates what the app is capable of, and helps envisage the path for future works.",
                html.Br(), html.Br(), "All the data used for this project is publicly available at the", html.A(" National River Flow Archive.", href ="https://nrfa.ceh.ac.uk/", id="linkInText")]),

            ])
        ], style={ "margin-top": "3rem", "margin-right": "0.5rem",  "margin-left": "1.5rem"})
    ]),
        dbc.Row([
            dbc.Col([
                html.Div([html.Hr()], id = "horizontalLine"),
                html.Div([
                    html.P("References:"),
                    html.Br(),
                    html.P("As this project is applied data science, some readings which provided fundamental knowledge needed to begin this project were not relevant to the final thesis. For this reason, I have provided an additional list of references here. These references helped towards understanding important concepts in hydrology and programming."),
                    html.Br(),
                    html.P(["European Centre for River Restoration. Website. ‘Development of a strategy to manage sediment in an appropriate way’. [last accessed: 01/07/2022]"], style={"padding-bottom": "0.5rem"}),
                    html.P(["McCuen, R. (1998) Hydrologic Analysis and Design, (2nd ed.) Pearson Education, New Jersey."], style={"padding-bottom": "0.5rem"}),
                    html.P(["Maity, R. (2018) Statistical Methods in Hydrology and Hydroclimatology, Springer. "], style={"padding-bottom": "0.5rem"}),
                    html.P(["Ward, R.C. (2000) Principles of Hydrology. (4th ed. ) McGraw-Hill International Publishing Company, London."], style={"padding-bottom": "0.5rem"}),
                    html.P(["VanderPlas, J. (2016) Python Data Science Handbook: Essential tools for working with Data, O’Reily."], style={"padding-bottom": "0.5rem"}),
                    html.Br(),
                    html.Br(),
                    html.Img(src="https://raw.githubusercontent.com/fionahavelock/WaterFlowApp/main/Durham_University_Logo.png", id="Image")

                ])
                
            ], width={"size": 9, "offset": 1},)
        ])
    ])
