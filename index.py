############################
#Imports
############################
#Dash Imports
import dash
from dash import Dash, dcc, html, Input, Output, ctx, State, dash_table, callback
import dash_bootstrap_components as dbc

#Plotly Imports
import plotly.express as px
import plotly.graph_objects as go

#Data Managing Imports
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


#File Imports
from APInrfa import *
from pages import Page1_GaugedDailyFlow, Page2_FlowCurve, Page3_AMaxMin, Page4_Stats, Home
# import all pages in the app
from app import app 
############################
# End imports
############################

#Logo URL for the navigation bar
#From my own github so the image is safe from being altered or deleted
LOGO = "https://raw.githubusercontent.com/fionahavelock/WaterFlowApp/main/Asset-4.png"

#################################
#Navigation bar 
#################################
text_color = "#95C5CC"
navbar = dbc.Navbar(
    dbc.Container([
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row([
                dbc.Col(html.Img(src=LOGO, height="60rem")),
                ],align="center", className="g-0",),
            href="index",style={"textDecoration": "none"},),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse([      
                    dbc.NavItem(
                        dbc.NavLink("Home", href="/page-1")),
                            dbc.DropdownMenu(
                                children=[
                                    dbc.DropdownMenuItem("Daily Flow", href="/DailyFlow"),
                                    dbc.DropdownMenuItem("Flow Duration", href="/FlowDuration"),
                                    dbc.DropdownMenuItem("Flood Frequency", href="/amax_min"),
                                ],label="Water Flow", nav=True, style = {"color": "#FAF1EB"}),
                    dbc.NavItem(dbc.NavLink("Catchment Daily Rainfall", href="/stats")),
                    ],id="navbar-collapse", is_open=False, navbar=True, style={"margin-left": "4rem"})
    ]), color = "#345A6B" )
#################################
# End navigation bar 
#################################



#############################
#layout of multipage app
#############################
#app.layout = html.Div([dcc.Location(id="url"), navbar])

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

#region help (navigation bar callback)
###################################
#call back for navigation bar
###################################
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open
#endregion 

###################################
#call back for navigation 
###################################


@app.callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
    )
def render_page_content(pathname):
    if pathname == "/DailyFlow":
        return Page1_GaugedDailyFlow.layout()
    elif pathname == "/FlowDuration":
        return Page2_FlowCurve.layout()
    elif pathname == "/amax_min":
        return Page3_AMaxMin.layout()
    elif pathname == "/stats":
        return Page4_Stats.layout()
    else:
        return Home.layout()
    # If the user tries to reach a different page, return a 404 message
    #return dbc.Jumbotron(
        #[
            #html.H1("404: Not found", className="text-danger"),
            #html.Hr(),
            #html.P(f"The pathname {pathname} was not recognised..."),
        #]
    #)

if __name__ == '__main__':

    app.run_server(host='127.0.0.1', debug=True)


