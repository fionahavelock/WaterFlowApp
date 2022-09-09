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
from sklearn.linear_model import LinearRegression

#File Imports
from app import app
from APInrfa import *

def layout():
    return html.Div([
        dbc.Row([
        html.Div([
            html.Header([
                html.H4("Catchment Daily Rainfall"),
                html.H5(["This page provides catchment daily rainfall information. The catchment daily rainfall data records the total rainfall averaged over the catchment in millimetres for each day.", html.Sup("1"), " Catchment daily rainfall is not directly related to streamflow; however, it is a factor that can influence the flow regime of a river.", html.Sup("2"), " For this reason, this visualisations on this page aim to support the analysis of stream flow."])
            ])
        ], style={ "margin-top": "3rem", "margin-right": "0.5rem",  "margin-left": "1.5rem"})
    ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.P("Select one station. Select one or more years:")
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
                                {'label': 'Bedburn Beck at Bedburn', 'value': '24004'},
                                {'label': 'Browney at Burnhall', 'value': '24005'},
                                {'label': 'Browney at Lanchester', 'value': '24007'},
                                {'label': 'Burnt Hill at Moor House', 'value': '25808'},
                                {'label': 'Coal Burn at Coalburn', 'value': '76011'},
                                {'label': 'Derwent at Eddys Bridge', 'value': '23002'},
                                {'label': 'Derwent at Rowlands Gill', 'value': '23007'},
                                {'label': 'Eden at Great Musgrave Bridge', 'value': '76021'},
                                {'label': 'Eden at Kirkby Stephen', 'value': '76014'},
                                {'label': 'Gaunless at Bishop Auckland', 'value': '24002'},
                                {'label': 'Greta at Rutherford Bridge', 'value': '25006'},
                                {'label': 'Harwood Beck at Harwood', 'value': '25012'},
                                {'label': 'Langdon Beck', 'value': '25011'},
                                {'label': 'North Tyne at Barrasford', 'value': '23015'},
                                {'label': 'North Tyne at Kielder temporary', 'value': '23014'},
                                {'label': 'North Tyne at Tarset', 'value': '23005'},
                                {'label': 'North Tyne at Reaverhill', 'value': '23003'},
                                {'label': 'Ouse Burn at Woolsington', 'value': '23018'},
                                {'label': 'Rookhope Burn at Eastgate', 'value': '24006'},
                                {'label': 'Skerne at Bradbury', 'value': '25021'},
                                {'label': 'Skerne at Darlington South Park', 'value': '25004'},
                                {'label': 'Skerne at Preston le Skerne', 'value': '25020'},
                                {'label': 'Sike Hill at Moor House', 'value': '25810'},
                                {'label': 'South Tyne at Alston', 'value': '23009'},
                                {'label': 'South Tyne at Featherstone', 'value': '23006'},
                                {'label': 'South Tyne at Haydon Bridge', 'value': '23004'},
                                {'label': 'Team at Team Valley', 'value': '23017'},
                                {'label': 'Tees at Barnard Castle', 'value': '25008'},
                                {'label': 'Tees at Cow Green Reservoir', 'value': '25023'},
                                {'label': 'Trout Beck at Moor House', 'value': '25003'},
                                {'label': 'Tees at Darlington Broken Scar', 'value': '25001'},
                                {'label': 'Tees at Dent Bank', 'value': '25002'},
                                {'label': 'Tees at Low Moor', 'value': '25009'},
                                {'label': 'Tees at Middleton in Teesdale', 'value': '25018'},
                                {'label': 'Tyne at Bywell', 'value': '23001'},
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
                                            "There is no runoff data availble for this station. Please select a different station.",
                                                color="warning",
                                                    id="alert_noRunoffData",
                                                        dismissable=True,
                                                            is_open=False,
                                            )
                                        ]),
                                        html.Div([
                                            dbc.Alert(
                                            "There is no rainfall data availble for this station. Please select a different station.",
                                                color="warning",
                                                    id="alert_noRainfallData",
                                                        dismissable=True,
                                                            is_open=False,
                                            )
                                        ])
                                ])
                            ]),
                            dbc.Card([
                                dbc.CardBody([
                                            html.Div([
                                            dcc.Dropdown(
                                            multi=True,
                                            id='yearDropdown',
                                            placeholder="Select a year",    
                                            ),
                                        ]),
                                        html.Div([
                                            dbc.Alert(
                                            "Please select a year.",
                                                color="warning",
                                                    id="alert_noYearData",
                                                        dismissable=True,
                                                            is_open=False,
                                            )
                                        ]),
                                        html.Div([
                                            dbc.Alert(
                                            "This year does not contain data.",
                                                color="warning",
                                                    id="alert_noYearRunoffData",
                                                        dismissable=True,
                                                            is_open=False,
                                            )
                                        ]),
                                ])
                            ])
                        ]),
                    #end row 1
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("Map of the North Pennines AONB and the selected location. Hover over the map to see station level in metres above ordnance datum."),
                                    html.Br(),
                                    dcc.Graph(id = 'altitudeMap')
                                ])
                            ])
                        ]),
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P(["Catchment daily rainfall data plotted against gauged daily flow data shows the relationship between rainfall and runoff.", html.Sup("3"), " A linear regression fit is plotted to show the overall trend of this data. Plotting many data points tends to show the best results."]),
                                    html.Br(),
                                    dcc.Graph(id ='rainfallRunoff')
                                ]),
                            ])
                    ]),
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("Time series of the total rainfall averaged over the catchment in millimetres for each day."),
                                    html.Br(),
                                    dcc.Graph(id = 'rainfall')
                                ])
                            ])
                        ]),
                ],style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "0.5rem",  "margin-left": "1rem"})
            ]),
        #Section 2
        dbc.Col([ 
            dbc.Card([
                    dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.P("Select one station. Select one or more years:")
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
                                {'label': 'Bedburn Beck at Bedburn', 'value': '24004'},
                                {'label': 'Browney at Burnhall', 'value': '24005'},
                                {'label': 'Browney at Lanchester', 'value': '24007'},
                                {'label': 'Burnt Hill at Moor House', 'value': '25808'},
                                {'label': 'Coal Burn at Coalburn', 'value': '76011'},
                                {'label': 'Derwent at Eddys Bridge', 'value': '23002'},
                                {'label': 'Derwent at Rowlands Gill', 'value': '23007'},
                                {'label': 'Eden at Great Musgrave Bridge', 'value': '76021'},
                                {'label': 'Eden at Kirkby Stephen', 'value': '76014'},
                                {'label': 'Gaunless at Bishop Auckland', 'value': '24002'},
                                {'label': 'Greta at Rutherford Bridge', 'value': '25006'},
                                {'label': 'Harwood Beck at Harwood', 'value': '25012'},
                                {'label': 'Langdon Beck', 'value': '25011'},
                                {'label': 'North Tyne at Barrasford', 'value': '23015'},
                                {'label': 'North Tyne at Kielder temporary', 'value': '23014'},
                                {'label': 'North Tyne at Tarset', 'value': '23005'},
                                {'label': 'North Tyne at Reaverhill', 'value': '23003'},
                                {'label': 'Ouse Burn at Woolsington', 'value': '23018'},
                                {'label': 'Rookhope Burn at Eastgate', 'value': '24006'},
                                {'label': 'Skerne at Bradbury', 'value': '25021'},
                                {'label': 'Skerne at Darlington South Park', 'value': '25004'},
                                {'label': 'Skerne at Preston le Skerne', 'value': '25020'},
                                {'label': 'Sike Hill at Moor House', 'value': '25810'},
                                {'label': 'South Tyne at Alston', 'value': '23009'},
                                {'label': 'South Tyne at Featherstone', 'value': '23006'},
                                {'label': 'South Tyne at Haydon Bridge', 'value': '23004'},
                                {'label': 'Tees at Barnard Castle', 'value': '25008'},
                                {'label': 'Tees at Cow Green Reservoir', 'value': '25023'},
                                {'label': 'Team at Team Valley', 'value': '23017'},
                                {'label': 'Trout Beck at Moor House', 'value': '25003'},
                                {'label': 'Tees at Darlington Broken Scar', 'value': '25001'},
                                {'label': 'Tees at Dent Bank', 'value': '25002'},
                                {'label': 'Tees at Low Moor', 'value': '25009'},
                                {'label': 'Tees at Middleton in Teesdale', 'value': '25018'},
                                {'label': 'Tyne at Bywell', 'value': '23001'},
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
                                            "There is no runoff data availble for this station. Please select a different station.",
                                                color="warning",
                                                    id="alert_noRunoffData2",
                                                        dismissable=True,
                                                            is_open=False,
                                            )
                                        ]),
                                        html.Div([
                                            dbc.Alert(
                                            "There is no rainfall data availble for this station. Please select a different station.",
                                                color="warning",
                                                    id="alert_noRainfallData2",
                                                        dismissable=True,
                                                            is_open=False,
                                            )
                                        ])
                                ])
                            ]),
                            dbc.Card([
                                dbc.CardBody([
                                            html.Div([
                                            dcc.Dropdown(
                                            multi=True,
                                            id='yearDropdownRainfall2',
                                            placeholder="Select a year",    
                                            ),
                                        ]),
                                        html.Div([
                                            dbc.Alert(
                                            "Please select a year.",
                                                color="warning",
                                                    id="alert_noYearData2",
                                                        dismissable=True,
                                                            is_open=False,
                                            )
                                        ]),
                                        html.Div([
                                            dbc.Alert(
                                            "This year does not contain data.",
                                                color="warning",
                                                    id="alert_noYearRunoffData2",
                                                        dismissable=True,
                                                            is_open=False,
                                            )
                                        ]),
                                ])
                            ])
                        ]),
                    #end row 1
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("Map of the North Pennines AONB and the selected location. Hover over the map to see station level in metres above ordnance datum."),
                                    html.Br(),
                                    dcc.Graph(id = 'altitudeMap2')
                                ])
                            ])
                        ]),
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P(["Catchment daily rainfall data plotted against gauged daily flow data shows the relationship between rainfall and runoff.", html.Sup("3"), " A linear regression fit is plotted to show the overall trend of this data. Plotting many data points tends to show the best results."]),
                                    html.Br(),
                                    dcc.Graph(id ='rainfallRunoff2')
                                ]),
                            ])
                    ]),
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("Time series of the total rainfall averaged over the catchment in millimetres for each day."),
                                    html.Br(),
                                    dcc.Graph(id = 'rainfall2')
                                ])
                            ])
                        ]),
                ],style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "1rem",  "margin-left": "0.5rem"})

        ]),
        dbc.Row([
                    html.Div([
                        html.Footer([
                            html.P("References:"),
                            html.Br(),
                            html.P([html.Sup(1), html.A(" National River Flow Archive Website: Catchment daily rainfall", href= "https://nrfa.ceh.ac.uk/catchment-rainfall", id="linkInText") ,], style={"padding-bottom": "0.5rem"}),
                            html.P([html.Sup(2)," Davie, T (2008) Fundamentals of Hydrology, Routledge. p.108"], style={"padding-bottom": "0.5rem"}),
                            html.P([html.Sup(3)," Davie, T (2008) Fundamentals of Hydrology, Routledge. p.116"], style={"padding-bottom": "0.5rem"}),
                        ])
                    ], style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "0.5rem",  "margin-left": "1.5rem"})
                ]),
        ])
    ])

#first callback
@app.callback(
    Output('alert_noRunoffData', 'is_open'),
    Output('alert_noRainfallData', 'is_open'),
    Output('yearDropdown', 'options'),
    Output('alert_noYearData', 'is_open'),
    Output('alert_noYearRunoffData', 'is_open'),
    Output('altitudeMap', 'figure'),
    Output('rainfallRunoff', 'figure'),
    Output('rainfall', 'figure'),
    Input('stationDropDown1', 'value'),
    Input('yearDropdown', 'value')
)

def callbackStats(stationNumber, selected_years):
    global dfrunoff1
    global dfrain1
    global Runoffdf
    global Rainfalldf
    global RainfalldfBar
    element_id = ctx.triggered_id if not None else 'No clicks yet'
    if element_id == 'stationDropDown1':
        if stationNumber != None:
            #get runoff data
            runoffData1 = getDailyTimeSeriesRunoff(stationNumber)
            if runoffData1 == []:
                return True, False, dash.no_update, False, False, dash.no_update, dash.no_update, dash.no_update
            #get rainfall data
            rainfallData = getDailyTimeSeriescdr(stationNumber)
            if rainfallData == []:
                return False, True, dash.no_update,False, False, dash.no_update, dash.no_update, dash.no_update
            ####################
            #get all years availible and make dataframes
            dfrunoff1 = pd.DataFrame(data=runoffData1)
            dfrain1 = pd.DataFrame(data=rainfallData)
            allYearsControl = dfrain1.Year.unique()
            return False, False, allYearsControl, False, False, dash.no_update, dash.no_update, dash.no_update
        else: 
            empty_years1 = []
            return False, False, empty_years1, False, False, go.Figure(), go.Figure(), go.Figure()
    elif element_id == 'yearDropdown':
        if selected_years != None:
            Runoffdf = pd.DataFrame(columns = ["Year", "Month", "Day", "Runoff", "sumRunoff" ])
            Rainfalldf = pd.DataFrame(columns = ["Year", "Month", "Day", "Rainfall" "sumRain"])
            RainfalldfBar = pd.DataFrame(columns = ["Year", "Month", "Day", "Rainfall"])
            for i in selected_years:
                dfsubsetrunoffSum = dfrunoff1[dfrunoff1['Year'] == i]
                if dfsubsetrunoffSum.empty == True:
                    return False, False, dash.no_update, False, True, dash.no_update, dash.no_update, dash.no_update
                dfsubsetrunoffSum['sumRunoff'] = dfsubsetrunoffSum.Runoff.sum()
                #dfsubsetrunoffSum = dfsubsetrunoffSum.assign(sumRunoff=dfsubsetrunoffSum.Runoff.sum())
                Runoffdf = Runoffdf.append(dfsubsetrunoffSum)
                ############################
                #rainfall data correlation
                ############################
                dfsubsetrainSum = dfrain1[dfrain1['Year'] == i ]
                dfsubsetrainSum['sumRain'] = dfsubsetrainSum.Rainfall.sum()
                #dfsubsetrainSum = dfsubsetrainSum.assign(sumRain=dfsubsetrainSum.Rainfall.sum())
                Rainfalldf = Rainfalldf.append(dfsubsetrainSum)
                ###########################
                #rainfall data bar chart
                ############################
                dfsubsetrainfall = dfrain1[dfrain1['Year'] == i]
                RainfalldfBar = RainfalldfBar.append(dfsubsetrainfall)
        else:
            return False, False, dash.no_update, True, False, dash.no_update,  go.Figure(), go.Figure()
        #########################################
        #Title information
        #########################################
        titleData = getgdfStatData(stationNumber)
        titleinfo = pd.DataFrame(data=titleData)
        location = titleinfo['Value'].iloc[1]
        river = titleinfo['Value'].iloc[2]
        #merge dataframes
        #mergeRainRunoff = ([Runoffdf,Rainfalldf ])
        #mergeRainRunoff = Runoffdf.merge(Rainfalldf, how='inner')
        mergeRainRunoff= Runoffdf.merge(Rainfalldf, left_on= ['Year', 'Month', 'Day'], right_on=['Year', 'Month', 'Day'])
        # plot rainfall runoff correlation 
        #color='Year',
        if mergeRainRunoff.empty == True:
            return False, False, dash.no_update, True, False, dash.no_update,  go.Figure(), go.Figure()
        else:
            X = mergeRainRunoff.sumRain.values.reshape(-1, 1)
            model = LinearRegression()
            model.fit(X, mergeRainRunoff.sumRunoff)
            x_range = np.linspace(X.min(), X.max(), 100)
            y_range = model.predict(x_range.reshape(-1, 1))
            figRunoffRainCor = px.scatter(mergeRainRunoff, x='sumRain', y='sumRunoff', color="Year", template="ggplot2", color_discrete_sequence=px.colors.qualitative.Light24)
            figRunoffRainCor.add_traces(go.Scatter(x=x_range, y=y_range, name='Regression Fit', ))
            #for least squares trendline
            #figRunoffRainCor = px.scatter(mergeRainRunoff, x="sumRain", y="sumRunoff", color="Year", trendline="ols", trendline_scope="overall", trendline_color_override="#8E9293",
                #template="ggplot2")
            figRunoffRainCor.update_xaxes(title='Total precipitation (mm)')
            figRunoffRainCor.update_yaxes(title='Total runoff (m3s-1)')
            figRunoffRainCor.update_traces(marker=dict(size=12, symbol = 103),)
            figRunoffRainCor.update_layout(title=f"Runoff Rainfall Correlation<br> {location} at {river}")
            ##selector=dict(mode='markers')
            #rainfall figure
            Rainfig = px.bar(RainfalldfBar, x="Month", y="Rainfall", color='Year', barmode="group", 
            template="ggplot2", color_discrete_sequence=px.colors.qualitative.Light24)
            Rainfig.update_xaxes(title='Time (months)')
            Rainfig.update_yaxes(title='Monthly sum of catchment daily rainfall in mm')
            Rainfig.update_layout(title=f"Catchement daily rainfall by Month<br> {location} at {river}")
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
                #need to plot legend
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
        return False, False, dash.no_update, False, False, altmap, figRunoffRainCor, Rainfig
    else:
        return False, False, dash.no_update, False, False, dash.no_update, dash.no_update, dash.no_update
    return False, False, dash.no_update, False, False, altmap, figRunoffRainCor, Rainfig

#Second callback
@app.callback(
    Output('alert_noRunoffData2', 'is_open'),
    Output('alert_noRainfallData2', 'is_open'),
    Output('yearDropdownRainfall2', 'options'),
    Output('alert_noYearData2', 'is_open'),
    Output('alert_noYearRunoffData2', 'is_open'),
    Output('altitudeMap2', 'figure'),
    Output('rainfallRunoff2', 'figure'),
    Output('rainfall2', 'figure'),
    Input('stationDropDown2', 'value'),
    Input('yearDropdownRainfall2', 'value')
)

def callbackStats2(stationNumber2, selected_years2):
    global dfrunoff2
    global dfrain2
    global Runoffdf2
    global Rainfalldf2
    global RainfalldfBar2
    element_id = ctx.triggered_id if not None else 'No clicks yet'
    if element_id == 'stationDropDown2':
        if stationNumber2 != None:
            #get runoff data
            runoffData2 = getDailyTimeSeriesRunoff(stationNumber2)
            if runoffData2 == []:
                return True, False, dash.no_update, False, False, dash.no_update, dash.no_update, dash.no_update
            #get rainfall data
            rainfallData2 = getDailyTimeSeriescdr(stationNumber2)
            if rainfallData2 == []:
                return False, True, dash.no_update,False, False, dash.no_update, dash.no_update, dash.no_update
            ####################
            #get all years availible and make dataframes
            dfrunoff2 = pd.DataFrame(data=runoffData2)
            dfrain2 = pd.DataFrame(data=rainfallData2)
            allYears2 = dfrain2.Year.unique()
            return False, False, allYears2, False, False, dash.no_update, dash.no_update, dash.no_update
        else: 
            empty_years2 = []
            return False, False, empty_years2, False, False, go.Figure(), go.Figure(), go.Figure()
    elif element_id == 'yearDropdownRainfall2':
        if selected_years2 != None:
            Runoffdf2 = pd.DataFrame(columns = ["Year", "Month", "Day", "Runoff", "sumRunoff" ])
            Rainfalldf2 = pd.DataFrame(columns = ["Year", "Month", "Day", "Rainfall" "sumRain"])
            RainfalldfBar2 = pd.DataFrame(columns = ["Year", "Month", "Day", "Rainfall"])
            for i in selected_years2:
                dfsubsetrunoffSum2 = dfrunoff2[dfrunoff2['Year'] == i]
                if dfsubsetrunoffSum2.empty == True:
                    return False, False, dash.no_update, False, True, dash.no_update, dash.no_update, dash.no_update
                dfsubsetrunoffSum2['sumRunoff'] = dfsubsetrunoffSum2.Runoff.sum()
                #dfsubsetrunoffSum = dfsubsetrunoffSum.assign(sumRunoff=dfsubsetrunoffSum.Runoff.sum())
                Runoffdf2 = Runoffdf2.append(dfsubsetrunoffSum2)
                ############################
                #rainfall data correlation
                ############################
                dfsubsetrainSum2 = dfrain2[dfrain2['Year'] == i ]
                dfsubsetrainSum2['sumRain'] = dfsubsetrainSum2.Rainfall.sum()
                #dfsubsetrainSum = dfsubsetrainSum.assign(sumRain=dfsubsetrainSum.Rainfall.sum())
                Rainfalldf2 = Rainfalldf2.append(dfsubsetrainSum2)
                ###########################
                #rainfall data bar chart
                ############################
                dfsubsetrainfall2 = dfrain2[dfrain2['Year'] == i]
                RainfalldfBar2 = RainfalldfBar2.append(dfsubsetrainfall2)
        else:
            return False, False, dash.no_update, True, False, dash.no_update,  go.Figure(), go.Figure()
        #########################################
        #Title information
        #########################################
        titleData2 = getgdfStatData(stationNumber2)
        titleinfo2 = pd.DataFrame(data=titleData2)
        location2 = titleinfo2['Value'].iloc[1]
        river2 = titleinfo2['Value'].iloc[2]
        #merge dataframes
        #mergeRainRunoff = ([Runoffdf,Rainfalldf ])
        #mergeRainRunoff = Runoffdf.merge(Rainfalldf, how='inner')
        mergeRainRunoff2= Runoffdf2.merge(Rainfalldf2, left_on= ['Year', 'Month', 'Day'], right_on=['Year', 'Month', 'Day'])
        # plot rainfall runoff correlation 
        #color='Year',
        if mergeRainRunoff2.empty == True:
            return False, False, dash.no_update, True, False, dash.no_update,  go.Figure(), go.Figure()
        else:
            X = mergeRainRunoff2.sumRain.values.reshape(-1, 1)
            model = LinearRegression()
            model.fit(X, mergeRainRunoff2.sumRunoff)
            x_range = np.linspace(X.min(), X.max(), 100)
            y_range = model.predict(x_range.reshape(-1, 1))
            figRunoffRainCor2 = px.scatter(mergeRainRunoff2, x='sumRain', y='sumRunoff', color="Year", template="ggplot2", color_discrete_sequence=px.colors.qualitative.Light24)
            figRunoffRainCor2.add_traces(go.Scatter(x=x_range, y=y_range, name='Regression Fit', ))
            #for least squares trendline
            #figRunoffRainCor = px.scatter(mergeRainRunoff, x="sumRain", y="sumRunoff", color="Year", trendline="ols", trendline_scope="overall", trendline_color_override="#8E9293",
                #template="ggplot2")
            figRunoffRainCor2.update_xaxes(title='Total precipitation (mm)')
            figRunoffRainCor2.update_yaxes(title='Total runoff (m3s-1)')
            figRunoffRainCor2.update_traces(marker=dict(size=12, symbol = 103),)
            figRunoffRainCor2.update_layout(title=f"Runoff Rainfall Correlation<br> {location2} at {river2}")
            ##selector=dict(mode='markers')
            #rainfall figure
            Rainfig2 = px.bar(RainfalldfBar2, x="Month", y="Rainfall", color='Year', barmode="group", 
            template="ggplot2", color_discrete_sequence=px.colors.qualitative.Light24)
            Rainfig2.update_xaxes(title='Time (months)')
            Rainfig2.update_yaxes(title='Monthly sum of catchment daily rainfall in mm')
            Rainfig2.update_layout(title=f"Catchement daily rainfall by Month<br> {location2} at {river2}")
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
                #need to plot legend
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
        return False, False, dash.no_update, False, False, altmap2, figRunoffRainCor2, Rainfig2
    else:
        return False, False, dash.no_update, False, False, dash.no_update, dash.no_update, dash.no_update
    return False, False, dash.no_update, False, False, altmap2, figRunoffRainCor2, Rainfig2

