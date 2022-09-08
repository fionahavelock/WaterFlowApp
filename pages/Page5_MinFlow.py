#Dash Imports
from dash import Dash, dcc, html, Input, Output, ctx, State, dash_table, callback
import dash_bootstrap_components as dbc
import dash

#Plotly Imports
import plotly.express as px
import plotly.graph_objects as go

#Data Managing Imports
import pandas as pd
import numpy as np


#File Imports
from app import app
from APInrfa import *

####################



def layout():
    html.Div([
        dbc.Row([
        html.Div([
            html.Header([
                html.H4("Time Series of Annual Minimum Flow Data"),
                html.H5(["This page collates gauged daily flow data from the", html.A(" National River Flow Archive", href ="https://nrfa.ceh.ac.uk/", id="linkInText")," and produces hydropgraphs for data anaylsis. The gauged Daily Flow is the mean river flow in cubic metres per second (m3s-1). Gauged daily flow readings are equivalent to the daily flow or discharge of a river."])
            ])
        ], style={ "margin-top": "3rem", "margin-right": "0.5rem",  "margin-left": "1.5rem"})
    ]),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.Card([
                    html.Div([
                        dcc.Dropdown(
                            options = [
                            {'label': 'Bywell', 'value': '23001'},
                            {'label': 'Reaverhill', 'value': '23003'},
                            {'label': 'Barrasford', 'value': '23015'},
                            {'label': 'Chester le Street', 'value': '24009'},
                            ],
                                placeholder="Select a station",
                                    id='stationDropDown1',)
                            #end of html div for station drop down
                        ]),
                    html.Div([
                        dbc.Alert(
                        "There is no data availble for this station. please select another station.",
                            color="warning",
                                dismissable=True,
                                    is_open=False,
                                        id="alert-noMinData1"),
                    ]),
                ])

                ], style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "1rem",  "margin-left": "1rem"})
            ]),
            dbc.Col([

            ])
        ])

"""
                            html.Br(),
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        html.P("Frequency graph of the annual maximum flow values."),
                                        html.Br(),
                                        dcc.Graph(id='MinimumFlow'),
                                    ]),
                                ])
                            ])


                            ###########################################
                                        ############################################################
            #Minimum flow
            mindata = getDailyTimeSeries(stationNumber)
            mindatadf = pd.DataFrame(data=mindata)
            allYears = mindatadf.Year.unique()
            MinimumFlowdf = pd.DataFrame(columns = ["Year", "Month", "Day", "Value"])
            for i in allYears:
                yearDf = mindatadf[mindatadf['Year'] == i]
                minFlow = yearDf[yearDf['Value'] == yearDf['Value'].min()]
                MinimumFlowdf = MinimumFlowdf.append(minFlow)

            #Minimum Flow Plot
            minfig = px.line(MinimumFlowdf, x ="Year", y = "Value", markers=True, template="ggplot2")
            #minfig.update_traces(marker=dict(size=7, symbol = 133),)
            minfig.update_xaxes(title='Time (years)')
            minfig.update_yaxes(title='Flow x(m3/s)')
            minfig.update_layout(title=f"Minimum flow values plotted against years<br> {location} at {river}")

"""