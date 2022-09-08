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

def layout():
    return html.Div([
        dbc.Row([
        html.Div([
            html.Header([
                html.H4("Time Series of Annual Maximum Flow Data"),
                html.H5(["This page collates data that can be used for flood frequency analysis. Flood frequency analysis focusses on measuring peak flows. There are two ways a peak flow can be defined.",html.Sup("1"), html.Ol(" "), html.Ol("1. The single maximum peak recorded within a year (annual maximum flow)"), html.Ol("2. Any flow measurement above a certain threshold value (peaks over threshold flow)"), "Both data types are plotted on this page. It is important to monitor peak flows for biodiversity reasons. Peak flows and flows that exceed a river’s flow capacity may overflow and wash away fertile topsoil in which plant life grows. ", html.Sup("2") ])
            ])
        ], style={ "margin-top": "3rem", "margin-right": "0.5rem",  "margin-left": "1.5rem"})
    ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                             dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                    html.P("Select one station:")
                        ])
                ]),
                        dbc.CardGroup([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        dcc.Dropdown(
                                            options = [
                                            {'label': 'West Allen at Hindley Wrae', 'value': '23013'},
                                {'label':'East Allen at Wide Eals', 'value': '23012'},
                                {'label': 'Balder at Balderhead Reservoir', 'value': '25022'},
                                {'label': 'Bog Hill at Moor House', 'value': '25809'},
                                {'label': 'Burnt Hill at Moor House', 'value': '25808'},
                                {'label': 'Bedburn Beck at Bedburn', 'value': '24004'},
                                {'label': 'Browney at Burnhall', 'value': '24005'},
                                {'label':'Browney at Lanchester', 'value': '24007'},
                                {'label': 'Burnt Hill at Moor House', 'value': '25808'},
                                {'label': 'Coal Burn at Coalburn', 'value': '76011'},
                                {'label': 'Clow Beck at Croft', 'value': '25007'},
                                {'label': 'Dacre Beck at Dacre Bridge', 'value': '76023'},
                                {'label': 'Derwent at Eddys Bridge', 'value': '23002'},
                                {'label': 'Derwent at Rowlands Gill', 'value': '23007'},
                                {'label': 'Eamont at Pooley Bridge', 'value': '76015'},
                                {'label': 'Eden at Great Musgrave Bridge', 'value': '76021'},
                                {'label': 'Eden at Kirkby Stephen', 'value': '76014'},
                                {'label': 'Gaunless at Bishop Auckland', 'value': '24002'},
                                {'label': 'Greta at Rutherford Bridge', 'value': '25006'},
                                {'label': 'Harwood Beck at Harwood', 'value': '25012'},
                                {'label': 'Kielder Burn at Kielder', 'value': '23011'},
                                {'label': 'Langdon Beck', 'value': '25011'},
                                {'label':'Leven at Leven Bridge', 'value': '25005'},
                                {'label': 'Leven at Easby', 'value': '25019'},
                                {'label': 'Lowther at Eamont Bridge', 'value': '76004'},
                                {'label': 'Lune at Lunes Bridge', 'value': '72015'},
                                {'label': 'North Tyne at Barrasford', 'value': '23015'},
                                {'label': 'North Tyne at Kielder temporary', 'value': '23014'},
                                {'label': 'North Tyne at Tarset', 'value': '23005'},
                                {'label': 'North Tyne at Reaverhill', 'value': '23003'},
                                {'label': 'Ouse Burn at Woolsington', 'value': '23018'},
                                {'label': 'Rede at Rede Bridge', 'value': '23008'},
                                {'label': 'Rede at Rede Bridge', 'value': '23033'},
                                {'label': 'Rookhope Burn at Eastgate', 'value': '24006'},
                                {'label': 'Skerne at Bradbury', 'value': '24006'},
                                {'label': 'Skerne at Darlington South Park', 'value': '25004'},
                                {'label': 'Skerne at Preston le Skerne', 'value': '25020'},
                                {'label': 'Sike Hill at Moor House', 'value': '25810'},
                                {'label': 'South Tyne at Alston', 'value': '23009'},
                                {'label': 'South Tyne at Featherstone', 'value': '23006'},
                                {'label': 'South Tyne at Haydon Bridge', 'value': '23004'},
                                {'label': 'Tarset Burn at Greenhaugh', 'value': '23010'},
                                {'label': 'Team at Team Valley', 'value': '23017'},
                                {'label': 'Tees at Barnard Castle', 'value': '23006'},
                                {'label': 'Trout Beck at Moor House', 'value': '23004'},
                                {'label': 'Tees at Cow Green Reservoir', 'value': '23010'},
                                {'label': 'Team at Team Valley', 'value': '23017'},
                                {'label': 'Tees at Barnard Castle', 'value': '25008'},
                                {'label': 'Trout Beck at Moor House', 'value': '25003'},
                                {'label': 'Tees at Cow Green Reservoir', 'value': '25023'},
                                {'label': 'Tees at Darlington Broken Scar', 'value': '25001'},
                                {'label': 'Tees at Dent Bank', 'value': '25002'},
                                {'label': 'Tees at Low Moo', 'value': '25009'},
                                {'label': 'Tees at Middleton in Teesdale', 'value': '25018'},
                                {'label': 'Tyne at Bywell', 'value': '23001'},
                                {'label': 'Wansbeck at Mitford', 'value': '22007'},
                                {'label': 'Wear at Burnhope Reservoir', 'value': '24011'},
                                {'label': 'Wear at Chester le Street', 'value': '24009'},
                                {'label': 'Wear at Stanhope', 'value': '24003'},
                                {'label': 'Wear at Sunderland Bridge', 'value': '24001'},
                                {'label': 'Wear at Witton Park', 'value': '24008'},  
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
                                                        id="alert-noData1"),
                                    ]),
                                ])
                                ]),
                                ]),
                            ]),
                        #end row 1 with the station select box
                        html.Br(),
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                    html.P("Map of the North Pennines AONB and the selected location. Hover over the map to see station level in metres above ordnance datum."),
                                    html.Br(),
                                        dcc.Graph(id = 'altitudeMapAMAX')
                                    ])
                                    
                                ])
                            ]),

                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        dbc.Alert(
                                            "There is no bankfull data availble for this station.",
                                                color="warning",
                                                    dismissable=True,
                                                        is_open=False,
                                                            id="alert-noBankfullData1"),
                                    ]),
                                    html.Div([
                                        html.P(["Time series graph of annual maximum data with bank full discharge level. The annual maximum flow data shows the single maximum peak, or flow in (m3 s-1) recorded within a year. Bank full discharge is the amount of water flowing when a river is full to the top of its banks.", html.Sup("3") ]),
                                        html.Br(),
                                        dcc.Graph(id='BankfullAMAXPlot1'),
                                    ])
                                ])
                            ]),
                            
                        
                        html.Br(),
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        dcc.Graph(id='GringortenReturn'),
                                    ]),
                                ])

                            ]),
                        html.Br(),
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        dcc.Graph(id='Gringorten'),
                                    ]),
                                ])

                            ]),
                        #end second row with amax flow plot
                        html.Br(),
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        html.P("Histogram of the annual maximum flow values. The histogram shows the frequency or count for a given annual maximum flow value."),
                                        html.Br(),
                                        dcc.Graph(id='Histogram'),
                                    ]),
                                ])

                            ]),
                        html.Br(),

                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        html.P(["Time series of peaks over threshold. The peaks over threshold data contains all peak flows that are greater than a given threshold flow. The threshold is generally set to include an average of 5 events per year. Where multiple peak flows occur in a single event, the largest is used for the peaks over threshold data.", html.Sup("4")]),
                                        html.Br(),
                                        dcc.Graph(id='PeaksOverThreshold'),
                                    ]),
                                ])

                            ]),

                    ],style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "0.5rem",  "margin-left": "1rem"})

                ]),
                #second column
                dbc.Col([
                    dbc.Card([
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("Select one station:")
                                ])
                            ])
                        ]),
                        dbc.CardGroup([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        dcc.Dropdown(
                                            options = [
                                            {'label': 'West Allen at Hindley Wrae', 'value': '23013'},
                                {'label':'East Allen at Wide Eals', 'value': '23012'},
                                {'label': 'Balder at Balderhead Reservoir', 'value': '25022'},
                                {'label': 'Bog Hill at Moor House', 'value': '25809'},
                                {'label': 'Burnt Hill at Moor House', 'value': '25808'},
                                {'label': 'Bedburn Beck at Bedburn', 'value': '24004'},
                                {'label': 'Browney at Burnhall', 'value': '24005'},
                                {'label':'Browney at Lanchester', 'value': '24007'},
                                {'label': 'Burnt Hill at Moor House', 'value': '25808'},
                                {'label': 'Coal Burn at Coalburn', 'value': '76011'},
                                {'label': 'Clow Beck at Croft', 'value': '25007'},
                                {'label': 'Dacre Beck at Dacre Bridge', 'value': '76023'},
                                {'label': 'Derwent at Eddys Bridge', 'value': '23002'},
                                {'label': 'Derwent at Rowlands Gill', 'value': '23007'},
                                {'label': 'Eamont at Pooley Bridge', 'value': '76015'},
                                {'label': 'Eden at Great Musgrave Bridge', 'value': '76021'},
                                {'label': 'Eden at Kirkby Stephen', 'value': '76014'},
                                {'label': 'Gaunless at Bishop Auckland', 'value': '24002'},
                                {'label': 'Greta at Rutherford Bridge', 'value': '25006'},
                                {'label': 'Harwood Beck at Harwood', 'value': '25012'},
                                {'label': 'Kielder Burn at Kielder', 'value': '23011'},
                                {'label': 'Langdon Beck', 'value': '25011'},
                                {'label':'Leven at Leven Bridge', 'value': '25005'},
                                {'label': 'Leven at Easby', 'value': '25019'},
                                {'label': 'Lowther at Eamont Bridge', 'value': '76004'},
                                {'label': 'Lune at Lunes Bridge', 'value': '72015'},
                                {'label': 'North Tyne at Barrasford', 'value': '23015'},
                                {'label': 'North Tyne at Kielder temporary', 'value': '23014'},
                                {'label': 'North Tyne at Tarset', 'value': '23005'},
                                {'label': 'North Tyne at Reaverhill', 'value': '23003'},
                                {'label': 'Ouse Burn at Woolsington', 'value': '23018'},
                                {'label': 'Rede at Rede Bridge', 'value': '23008'},
                                {'label': 'Rede at Rede Bridge', 'value': '23033'},
                                {'label': 'Rookhope Burn at Eastgate', 'value': '24006'},
                                {'label': 'Skerne at Bradbury', 'value': '24006'},
                                {'label': 'Skerne at Darlington South Park', 'value': '25004'},
                                {'label': 'Skerne at Preston le Skerne', 'value': '25020'},
                                {'label': 'Sike Hill at Moor House', 'value': '25810'},
                                {'label': 'South Tyne at Alston', 'value': '23009'},
                                {'label': 'South Tyne at Featherstone', 'value': '23006'},
                                {'label': 'South Tyne at Haydon Bridge', 'value': '23004'},
                                {'label': 'Tarset Burn at Greenhaugh', 'value': '23010'},
                                {'label': 'Team at Team Valley', 'value': '23017'},
                                {'label': 'Tees at Barnard Castle', 'value': '23006'},
                                {'label': 'Trout Beck at Moor House', 'value': '23004'},
                                {'label': 'Tees at Cow Green Reservoir', 'value': '23010'},
                                {'label': 'Team at Team Valley', 'value': '23017'},
                                {'label': 'Tees at Barnard Castle', 'value': '25008'},
                                {'label': 'Trout Beck at Moor House', 'value': '25003'},
                                {'label': 'Tees at Cow Green Reservoir', 'value': '25023'},
                                {'label': 'Tees at Darlington Broken Scar', 'value': '25001'},
                                {'label': 'Tees at Dent Bank', 'value': '25002'},
                                {'label': 'Tees at Low Moo', 'value': '25009'},
                                {'label': 'Tees at Middleton in Teesdale', 'value': '25018'},
                                {'label': 'Tyne at Bywell', 'value': '23001'},
                                {'label': 'Wansbeck at Mitford', 'value': '22007'},
                                {'label': 'Wear at Burnhope Reservoir', 'value': '24011'},
                                {'label': 'Wear at Chester le Street', 'value': '24009'},
                                {'label': 'Wear at Stanhope', 'value': '24003'},
                                {'label': 'Wear at Sunderland Bridge', 'value': '24001'},
                                {'label': 'Wear at Witton Park', 'value': '24008'}, 
                                            ],
                                                placeholder="Select a station",
                                                    id='stationDropDown2',)
                                            #end of html div for station drop down
                                        ]),
                                    html.Div([
                                        dbc.Alert(
                                        "There is no data availble for this station. please select another station.",
                                            color="warning",
                                                dismissable=True,
                                                    is_open=False,
                                                        id="alert-noData2"),
                                    ]),
                                ])
                                 ])
                            ]),
                        #end row 1 with the station select box
                        html.Br(),
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                    html.P("Map of the North Pennines AONB and the selected location. Hover over the map to see station level in metres above ordnance datum."),
                                    html.Br(),
                                        dcc.Graph(id = 'altitudeMapAMAX2')
                                    ])
                                    
                                ])
                            ]),

                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        dbc.Alert(
                                            "There is no bankfull data availble for this station.",
                                                color="warning",
                                                    dismissable=True,
                                                        is_open=False,
                                                            id="alert-noBankfullData2"),
                                    ]),
                                    html.Div([
                                        html.P(["Time series graph of annual maximum data with bank full discharge level. The annual maximum flow data shows the single maximum peak, or flow in (m3 s-1) recorded within a year. Bank full discharge is the amount of water flowing when a river is full to the top of its banks.", html.Sup("3") ]),
                                        html.Br(),
                                        dcc.Graph(id='BankfullAMAXPlot2'),
                                    ])
                                ])
                            ]),
                            
                        
                        html.Br(),
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        dcc.Graph(id='GringortenReturn2'),
                                    ]),
                                ])

                            ]),
                        html.Br(),
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        dcc.Graph(id='Gringorten2'),
                                    ]),
                                ])

                            ]),
                        #end second row with amax flow plot
                        html.Br(),
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        html.P("Histogram of the annual maximum flow values. The histogram shows the frequency or count for a given annual maximum flow value."),
                                        html.Br(),
                                        dcc.Graph(id='Histogram2'),
                                    ]),
                                ])

                            ]),
                        html.Br(),

                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        html.P(["Time series of peaks over threshold. The peaks over threshold data contains all peak flows that are greater than a given threshold flow. The threshold is generally set to include an average of 5 events per year. Where multiple peak flows occur in a single event, the largest is used for the peaks over threshold data.", html.Sup("4")]),
                                        html.Br(),
                                        dcc.Graph(id='PeaksOverThreshold2'),
                                    ]),
                                ])

                            ]),

                    ], style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "1rem",  "margin-left": "0.5rem"})

                ]),
                        #end of row
                dbc.Row([
                    html.Div([
                        html.Footer([
                            html.P("References:"),
                            html.Br(),
                            html.P([html.Sup(1)," Davie, T (2008) Fundamentals of Hydrology, Routledge. p.107"], style={"padding-bottom": "0.5rem"}),
                            html.P([html.Sup(2)," Wilson, E (1974) Engineering Hydrology, The Macmillan Press. p.91"], style={"padding-bottom": "0.5rem"}),
                            html.P([html.Sup(3)," Davie, T (2008) Fundamentals of Hydrology, Routledge. p.108"], style={"padding-bottom": "0.5rem"}),
                            html.P([html.Sup(4), html.A(" National River Flow Archive Website: Peaks Over Threshold", href= "https://nrfa.ceh.ac.uk/peaks-over-threshold#:~:text=Definition,FEH%20Volume%203%2C%20section%2023.5.", id="linkInText") ,], style={"padding-bottom": "0.5rem"}),
                        ])
                    ], style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "0.5rem",  "margin-left": "1.5rem"})
                ]),
    ])
    ])

@app.callback(
    Output('alert-noData1', 'is_open'),
    Output('altitudeMapAMAX', 'figure'),
    Output('alert-noBankfullData1', 'is_open'),
    Output('BankfullAMAXPlot1', 'figure'),
    Output('GringortenReturn', 'figure'),
    Output('Gringorten', 'figure'),
    Output('Histogram', 'figure'),
    Output('PeaksOverThreshold', 'figure'),
    Input('stationDropDown1', 'value')
    )
def getAMAXMIN1 (stationNumber):
    element_id = ctx.triggered_id if not None else 'No clicks yet'
    global AmaxTimeDatadf
    global Gringortendf
    global GringortenReturnPerioddf
    annualmaixmum = "amax-flow"
    #potFlow = "gauging-flow"
    #annualminimum = 
    if element_id == 'stationDropDown1':
        if stationNumber != None:
            AmaxTimeData = getTimeSeriesAmax(annualmaixmum, stationNumber)
            if AmaxTimeData == []:
                #no annual data for bankfull
                return True, dash.no_update, False, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
            AmaxTimeDatadf = pd.DataFrame(data=AmaxTimeData)
            #get bankfull and annual maxima data
            bankfulldf = getBankfullData(stationNumber)
            bankfulltempdf = pd.DataFrame(data=bankfulldf).drop(index=0)
            bankfull = bankfulltempdf['Value'].iloc[0]
            ###########################################################
            potFlowTimeData = getTimeSeriesAmax( 'pot-flow', stationNumber)
            potTimedf = pd.DataFrame(data=potFlowTimeData)
            ################################################
            # Gringorten Formula
            GringortenData = pd.DataFrame(data=AmaxTimeData)
            GringortenData['RankedFlow'] = sorted(GringortenData['Value'], reverse =True)
            # make an empty list for the rank position
            rank = []
            rank.extend(range(1, len(GringortenData['RankedFlow'])+1))
            # add the rank positions into the data frame
            GringortenData['Rank'] = rank
            #create an empty dataframe to plot
            Gringortendf = pd.DataFrame(columns = ["RankedFlow", "Rank", "P(X)"])
            N = GringortenData.Rank.unique()
            n = len(N)
            #return period, rank descending, highest flow is rank 1
            for i in N:
                Px =  GringortenData['Rank']-0.44 / n +0.12
            Gringortendf = Gringortendf.append(pd.DataFrame({'RankedFlow': GringortenData['RankedFlow'], 'Rank': GringortenData['Rank'], 'P(X)': Px}))
            #########################################################
            #Gringorten Reurn Period
            GringortenReturnPerioddf = pd.DataFrame(columns = ["RankedFlow", "Rank", "multiplied", "ReturnPeriod", "plottedreturnPeriod"])
            for i in N:
                multiply = Gringortendf["P(X)"] *100
                returnPeriod = np.reciprocal(multiply)
                returnMultiplied = returnPeriod *10000
            GringortenReturnPerioddf = GringortenReturnPerioddf.append(pd.DataFrame({'RankedFlow': Gringortendf['RankedFlow'], 'Rank': Gringortendf['Rank'], 'multiplied': multiply, 'ReturnPeriod': returnPeriod, 'plottedreturnPeriod': returnMultiplied}))
            ##################################################
            #########################################
            #Title information
            #########################################
            titleData = getgdfStatData(stationNumber)
            titleinfo = pd.DataFrame(data=titleData)
            location = titleinfo['Value'].iloc[1]
            river = titleinfo['Value'].iloc[2]
            #plot figures
            #Time Series
            Amaxfig = px.line(AmaxTimeDatadf, x = "Year", y = "Value",  template="ggplot2",)
            Amaxfig.update_layout(title=f"Annual maximimum flow data over time <br> {location} at {river}")
            Amaxfig.update_xaxes(title='Time (years)')
            Amaxfig.update_yaxes(title='Flow (m3/s-1)')
            #Gringorten Return Period
            GringortenRfig = px.line(GringortenReturnPerioddf, x = GringortenReturnPerioddf['RankedFlow'], y = "plottedreturnPeriod", template="ggplot2",)
            GringortenRfig.update_xaxes(title='Annual maximum flow (m3/s-1)')
            GringortenRfig.update_yaxes(title='Return period in years')
            GringortenRfig.update_layout(title=f"Gringorten probaility function <br> {location} at {river}")
            #Gringorten
            Gringortenfig = px.line(Gringortendf, x = Gringortendf['RankedFlow'], y = "P(X)", template="ggplot2",)
            Gringortenfig.update_xaxes(title='Annual maximum flow (m3/s-1)')
            Gringortenfig.update_yaxes(title='Probabilty as a percentage')
            Gringortenfig.update_layout(title=f"Gringorten probaility function <br> {location} at {river}")
            #Histogram
            histfig = px.histogram(AmaxTimeDatadf, x="Value", template="ggplot2",)
            histfig.update_layout(bargap=0.1)
            histfig.update_xaxes(title='Annual maximum flow (m3/s-1)')
            histfig.update_yaxes(title='Count')
            histfig.update_layout(title=f"Annual maximimum flow frequency <br> {location} at {river}")
            #Peaks over threshold
            potFig = px.scatter(potTimedf, x ="Year", y = "Value", template="ggplot2",)
            potFig.update_traces(marker=dict(size=7, symbol = 133),)
            potFig.update_xaxes(title='Time (years)')
            potFig.update_yaxes(title='Flow (m3/s-1)')
            potFig.update_layout(title=f"Peaks over a threshold value plotted against years<br> {location} at {river}")
            #########################################
            #map
            #########################################
            Location = getMapLocation(stationNumber)
            Locationdf = pd.DataFrame(data=Location)
            indexCol = []
            for value in Locationdf["Value"]:
                indexCol.append(0)
            Locationdf["Index"] = indexCol
            Locationdf = Locationdf.pivot(index="Index", columns="Key", values="Value")
            altitude = Locationdf['station-level'].iloc[0]
            if altitude != 'N/A':
                if altitude < 50:
                    colourdf = pd.DataFrame(["#F8766D"], columns=["color"])
                elif altitude > 50 and altitude < 100:
                    colourdf = pd.DataFrame(["#00BFC4"], columns=["color"])
                elif altitude > 100 and altitude < 200:
                    colourdf = pd.DataFrame(["#4DE0D5"], columns=["color"])
                elif altitude > 200:
                    colourdf = pd.DataFrame(['#C77CFF'], columns=["color"])
                AltitudeLocationData = Locationdf.join(colourdf)
                altmap = px.scatter_mapbox(AltitudeLocationData, lat=AltitudeLocationData['latitude'], lon=AltitudeLocationData['longitude'], 
                                size=AltitudeLocationData['latitude'].astype(float),
                                color_discrete_sequence=[AltitudeLocationData.color],
                                custom_data=['river', 'name', 'station-level'],
                                center=dict(lat=54.776496, lon=-1.976193), zoom=7.3,
                                mapbox_style="open-street-map", height=300)
                altmap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                altmap.update_traces(hovertemplate="River: %{customdata[0]} <br> Location: %{customdata[1]} <br> Station level: %{customdata[2]} m AOD (above ordnance datum)")
            else:
                altmap = px.scatter_mapbox(Locationdf, lat=Locationdf['latitude'], lon=Locationdf['longitude'], 
                size=Locationdf['latitude'].astype(float),
                custom_data=['river', 'name',],
                center=dict(lat=54.776496, lon=-1.976193), zoom=7.3,
                mapbox_style="open-street-map", height=300)
                altmap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                altmap.update_traces(hovertemplate="River: %{customdata[0]} <br> Location: %{customdata[1]}")
            #bankfull 
            if bankfull == 'N/A':
                #no bankful result data for bankful
                return False, altmap, True, Amaxfig, GringortenRfig, Gringortenfig, histfig, potFig
            else:
                Amaxfig.add_hline(y=bankfull, line_width=3, line_dash="dot", line_color="#6A76FC", 
                    annotation_text="Bankfull",
                    annotation_position="bottom left",
                    annotation_font_size=20,
                    annotation_font_color="#6A76FC" )
            return False, altmap, False, Amaxfig, GringortenRfig, Gringortenfig,  histfig, potFig
        else:
            return False, go.Figure(), False, go.Figure(),go.Figure(),  go.Figure(), go.Figure(), go.Figure(), 
    else:
        return False, dash.no_update,  False, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, 

#second app callback
@app.callback(
    Output('alert-noData2', 'is_open'),
    Output('altitudeMapAMAX2', 'figure'),
    Output('alert-noBankfullData2', 'is_open'),
    Output('BankfullAMAXPlot2', 'figure'),
    Output('GringortenReturn2', 'figure'),
    Output('Gringorten2', 'figure'),
    Output('Histogram2', 'figure'),
    Output('PeaksOverThreshold2', 'figure'),
    Input('stationDropDown2', 'value')
    )
def getAMAXMIN1 (stationNumber2):
    element_id = ctx.triggered_id if not None else 'No clicks yet'
    global AmaxTimeDatadf2
    global Gringortendf2
    global GringortenReturnPerioddf2
    annualmaixmum = "amax-flow"
    #potFlow = "gauging-flow"
    #annualminimum = 
    if element_id == 'stationDropDown2':
        if stationNumber2 != None:
            AmaxTimeData2 = getTimeSeriesAmax(annualmaixmum, stationNumber2)
            if AmaxTimeData2 == []:
                #no annual data for bankfull
                return True, dash.no_update, False, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
            AmaxTimeDatadf2 = pd.DataFrame(data=AmaxTimeData2)
            #get bankfull and annual maxima data
            bankfulldf2 = getBankfullData(stationNumber2)
            bankfulltempdf2 = pd.DataFrame(data=bankfulldf2).drop(index=0)
            bankfull2 = bankfulltempdf2['Value'].iloc[0]
            ###########################################################
            potFlowTimeData2 = getTimeSeriesAmax( 'pot-flow', stationNumber2)
            potTimedf2 = pd.DataFrame(data=potFlowTimeData2)
            ################################################
            # Gringorten Formula
            GringortenData2 = pd.DataFrame(data=AmaxTimeData2)
            GringortenData2['RankedFlow'] = sorted(GringortenData2['Value'], reverse =True)
            # make an empty list for the rank position
            rank = []
            rank.extend(range(1, len(GringortenData2['RankedFlow'])+1))
            # add the rank positions into the data frame
            GringortenData2['Rank'] = rank
            #create an empty dataframe to plot
            Gringortendf2 = pd.DataFrame(columns = ["RankedFlow", "Rank", "P(X)"])
            N = GringortenData2.Rank.unique()
            n = len(N)
            #return period, rank descending, highest flow is rank 1
            for i in N:
                Px =  GringortenData2['Rank']-0.44 / n +0.12
            Gringortendf2 = Gringortendf2.append(pd.DataFrame({'RankedFlow': GringortenData2['RankedFlow'], 'Rank': GringortenData2['Rank'], 'P(X)': Px}))
            #########################################################
            #Gringorten Reurn Period
            GringortenReturnPerioddf2 = pd.DataFrame(columns = ["RankedFlow", "Rank", "multiplied", "ReturnPeriod", "plottedreturnPeriod"])
            for i in N:
                multiply = Gringortendf2["P(X)"] *100
                returnPeriod = np.reciprocal(multiply)
                returnMultiplied = returnPeriod *10000
            GringortenReturnPerioddf2 = GringortenReturnPerioddf2.append(pd.DataFrame({'RankedFlow': Gringortendf2['RankedFlow'], 'Rank': Gringortendf2['Rank'], 'multiplied': multiply, 'ReturnPeriod': returnPeriod, 'plottedreturnPeriod': returnMultiplied}))
            ##################################################
            #########################################
            #Title information
            #########################################
            titleData2 = getgdfStatData(stationNumber2)
            titleinfo2 = pd.DataFrame(data=titleData2)
            location2 = titleinfo2['Value'].iloc[1]
            river2 = titleinfo2['Value'].iloc[2]
            #plot figures
            #Time Series
            Amaxfig2 = px.line(AmaxTimeDatadf2, x = "Year", y = "Value",  template="ggplot2",)
            Amaxfig2.update_layout(title=f"Annual maximimum flow data over time <br> {location2} at {river2}")
            Amaxfig2.update_xaxes(title='Time (years)')
            Amaxfig2.update_yaxes(title='Flow (m3/s-1)')
            #Gringorten Return Period
            GringortenRfig2 = px.line(GringortenReturnPerioddf2, x = GringortenReturnPerioddf2['RankedFlow'], y = "plottedreturnPeriod", template="ggplot2",)
            GringortenRfig2.update_xaxes(title='Annual maximum flow (m3/s-1)')
            GringortenRfig2.update_yaxes(title='Return period in years')
            GringortenRfig2.update_layout(title=f"Gringorten probaility function <br> {location2} at {river2}")
            #Gringorten
            Gringortenfig2 = px.line(Gringortendf2, x = Gringortendf2['RankedFlow'], y = "P(X)", template="ggplot2",)
            Gringortenfig2.update_xaxes(title='Annual maximum flow (m3/s-1)')
            Gringortenfig2.update_yaxes(title='Probabilty as a percentage')
            Gringortenfig2.update_layout(title=f"Gringorten probaility function <br> {location2} at {river2}")
            #Histogram
            histfig2 = px.histogram(AmaxTimeDatadf2, x="Value", template="ggplot2",)
            histfig2.update_layout(bargap=0.1)
            histfig2.update_xaxes(title='Annual maximum flow (m3/s-1)')
            histfig2.update_yaxes(title='Count')
            histfig2.update_layout(title=f"Annual maximimum flow frequency <br> {location2} at {river2}")
            #Peaks over threshold
            potFig2 = px.scatter(potTimedf2, x ="Year", y = "Value", template="ggplot2",)
            potFig2.update_traces(marker=dict(size=7, symbol = 133),)
            potFig2.update_xaxes(title='Time (years)')
            potFig2.update_yaxes(title='Flow (m3/s-1)')
            potFig2.update_layout(title=f"Peaks over a threshold value plotted against years<br> {location2} at {river2}")
            #########################################
            #map
            #########################################
            Location2 = getMapLocation(stationNumber2)
            Locationdf2 = pd.DataFrame(data=Location2)
            indexCol = []
            for value in Locationdf2["Value"]:
                indexCol.append(0)
            Locationdf2["Index"] = indexCol
            Locationdf2 = Locationdf2.pivot(index="Index", columns="Key", values="Value")
            altitude = Locationdf2['station-level'].iloc[0]
            if altitude != 'N/A':
                if altitude < 50:
                    colourdf = pd.DataFrame(["#F8766D"], columns=["color"])
                elif altitude > 50 and altitude < 100:
                    colourdf = pd.DataFrame(["#00BFC4"], columns=["color"])
                elif altitude > 100 and altitude < 200:
                    colourdf = pd.DataFrame(["#4DE0D5"], columns=["color"])
                elif altitude > 200:
                    colourdf = pd.DataFrame(['#C77CFF'], columns=["color"])
                AltitudeLocationData2 = Locationdf2.join(colourdf)
                altmap2 = px.scatter_mapbox(AltitudeLocationData2, lat=AltitudeLocationData2['latitude'], lon=AltitudeLocationData2['longitude'], 
                                size=AltitudeLocationData2['latitude'].astype(float),
                                color_discrete_sequence=[AltitudeLocationData2.color],
                                custom_data=['river', 'name', 'station-level'],
                                center=dict(lat=54.776496, lon=-1.976193), zoom=7.3,
                                mapbox_style="open-street-map", height=300)
                altmap2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                altmap2.update_traces(hovertemplate="River: %{customdata[0]} <br> Location: %{customdata[1]} <br> Station level: %{customdata[2]} m AOD (above ordnance datum)")
            else:
                altmap2 = px.scatter_mapbox(Locationdf2, lat=Locationdf2['latitude'], lon=Locationdf2['longitude'], 
                size=Locationdf2['latitude'].astype(float),
                custom_data=['river', 'name',],
                center=dict(lat=54.776496, lon=-1.976193), zoom=7.3,
                mapbox_style="open-street-map", height=300)
                altmap2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                altmap2.update_traces(hovertemplate="River: %{customdata[0]} <br> Location: %{customdata[1]}")
            #bankfull 
            if bankfull2 == 'N/A':
                #no bankful result data for bankful
                return False, altmap2, True, Amaxfig2, GringortenRfig2, Gringortenfig2, histfig2, potFig2
            else:
                Amaxfig2.add_hline(y=bankfull2, line_width=3, line_dash="dot", line_color="#6A76FC", 
                    annotation_text="Bankfull",
                    annotation_position="bottom left",
                    annotation_font_size=20,
                    annotation_font_color="#6A76FC" )
            return False, altmap2, False, Amaxfig2, GringortenRfig2, Gringortenfig2,  histfig2, potFig2
        else:
            return False, go.Figure(), False, go.Figure(),go.Figure(),  go.Figure(), go.Figure(), go.Figure(), 
    else:
        return False, dash.no_update,  False, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, 


"""
            #bankfull 
            if bankfull == 'N/A':
                #no bankful result data for bankful
                return False, dash.no_update, True, dash.no_update,dash.no_update, dash.no_update, dash.no_update, dash.no_update
            Amaxfig.add_hline(y=bankfull, line_width=3, line_dash="dot", line_color="#6A76FC", 
                annotation_text="Bankfull",
                annotation_position="bottom left",
                annotation_font_size=20,
                annotation_font_color="#6A76FC" )
"""