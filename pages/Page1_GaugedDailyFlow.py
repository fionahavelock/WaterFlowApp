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
    return html.Div([
    #need to have a row for the header
    dbc.Row([
        html.Div([
            html.Header([
                html.H4("Time Series of Gauged Daily Flow Data"),
                html.H5(["This page collates gauged daily flow data from the", html.A(" National River Flow Archive", href ="https://nrfa.ceh.ac.uk/", id="linkInText")," and produces hydropgraphs for data anaylsis. Gauged daily flow is the mean river flow in cubic metres per second (m3/s-1) recorded each day. The river flow process refers to the flow of water down a river in a channelised form. River flow is expressed as discharge or runoff: the volumne of water over a defined time period.", html.Sup("1")])
            ])
        ], style={ "margin-top": "3rem", "margin-right": "0.5rem",  "margin-left": "1.5rem"})
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.P("Select one station and year. Select one or more months:")
                        ])
                    ])
                ]),
                dbc.CardGroup([
                    dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                dcc.Dropdown(options = [
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
                                placeholder="Select a location",
                                id='placeDropdown1',)
                            ]),
                            html.Div([
                                dbc.Alert(
                                "There is no data availble for this station. Please select a different station.",
                                    color="warning",
                                        id="alert_noData1",
                                            dismissable=True,
                                                is_open=False,
                                )
                        ])
                        ])
                    ]),
                    ], md=5), #end of card with station number
                    dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                dcc.Dropdown(
                                placeholder="Select a year",
                                id='yearDropdown1gdf',)
                            ]),
                            html.Div([
                                dbc.Alert(
                                "Please select a year.",
                                    color="warning",
                                        id="alert_noyear1",
                                            dismissable=True,
                                                is_open=False,
                                                    
                                )
                            ])
                        ])
                    ]), #end of card with year selection
                    ], md=3),
                    dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                dcc.Dropdown(
                                    multi=True,
                                        placeholder="Select a month",
                                            id='monthDropdown1')
                            ]),
                        ])
                    ])
                    ], md=4),
                ]),
                html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("Map of the North Pennines AONB and the selected location. Hover over the map to see station level in metres above ordnance datum."),
                                    html.Br(),
                                    dcc.Graph(id = 'altitudeMapGdf')
                                ])
                            ])
                        ]),
                html.Br(),
                dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.P("Time series graph of gauged daily flow. Plotting the discharge or flow of a river over time yeilds a hydrograph."),
                            html.Br(),
                            dcc.Graph(id='dailytimeseries1'),
                        ])
                    ])
                ]),
                html.Br(),
                        dbc.Card([ 
                            dbc.CardBody([
                                dbc.Col([
                                html.Div([
                                    html.P("Data frame containing statistical information availible for the selected station."),
                                    html.Br(),
                                    dash_table.DataTable(
                                        id='gdfStatTable1',
                                            columns=[], 
                                                #style_as_list_view=True,
                                                    style_cell={'backgroundColor': 'white', 
                                                                'color': 'black',
                                                                'textAlign': 'left'
                                                                },
                                                        style_header={
                                                        'backgroundColor': '#658B8F',
                                                        'color': '#F2F3F5'
                                                                        },
                                                        style_data={
                                                        'whiteSpace': 'normal',
                                                        'height': 'auto',
                                                        },)
                                ]),
                                ], width={ "offset": 0.5},),
                            ]),
                                ]),

                #end of first card inside column
                 ], style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "0.5rem",  "margin-left": "1rem"} )
            #column size
    ], md=6),
    #second section
        dbc.Col([
            dbc.Card([
                dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.P("Select one station and year. Select one or more months:")
                        ])
                    ])
                ]),
                dbc.CardGroup([
                    dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                dcc.Dropdown(options = [
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
                                placeholder="Select a location",
                                id='placeDropdown2',)
                            ]),
                            html.Div([
                                dbc.Alert(
                                "There is no data availble for this station. Please select a different station.",
                                color="warning",
                                id="alert_noData2",
                                dismissable=True,
                                is_open=False,
                                )
                        ])
                        ])
                    ]),
                    ], md=5), #end of card with station number
                    dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                dcc.Dropdown(
                                placeholder="Select a year",
                                id='yearDropdown2',)
                            ]),
                            html.Div([
                                dbc.Alert(
                                "Please select a year.",
                                    color="warning",
                                        id="alert_noyear2",
                                            dismissable=True,
                                                is_open=False,                
                                )
                            ])
                        ])
                    ]),
                    ], md=3),
                     #end of card with year selection
                    dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                dcc.Dropdown(
                                multi=True,
                                placeholder="Select a month",
                                id='monthDropdown2',)

                            ])
                        ])
                    ])
                    ], md=4),
                ]),
                html.Br(),
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                html.P("Map of the North Pennines AONB and the selected location. Hover over the map to see station level in metres above ordnance datum."),
                                html.Br(),
                                dcc.Graph(id = 'altitudeMapGdf2')
                            ])
                        ])
                    ]),
                html.Br(),
                dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.P("Time series graph of gauged daily flow. Plotting the discharge or flow of a river over time yeilds a hydrograph."),
                            html.Br(),
                            dcc.Graph(id='dailytimeseries2'),
                        ])
                    ])
                ]),
                html.Br(),
                        dbc.Card([ 
                            dbc.CardBody([
                                dbc.Col([
                                html.Div([
                                    html.P("Data frame containing statistical information availible for the selected station."),
                                    html.Br(),
                                    dash_table.DataTable(
                                        id='gdfStatTable2',
                                            columns=[], 
                                                #style_as_list_view=True,
                                                    style_cell={'backgroundColor': 'white', 
                                                                'color': 'black',
                                                                'textAlign': 'left'
                                                                },
                                                        style_header={
                                                        'backgroundColor': '#658B8F',
                                                        'color': '#F2F3F5'
                                                                        },
                                                        style_data={
                                                        'whiteSpace': 'normal',
                                                        'height': 'auto',
                                                        },)
                                ]),
                                ],width={ "offset": 0.5}),
                            ]),
                                ]),
            #column size
            ], style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "1rem",  "margin-left": "0.5rem"})
    ], md=6),
            dbc.Row([
                    html.Div([
                        html.Footer([
                            html.P("References:"),
                            html.Br(),
                            html.P([html.Sup(1)," Davie, T (2008) Fundamentals of Hydrology, Routledge. p.78"], style={"padding-bottom": "0.5rem"}),
                        ])
                    ], style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "0.5rem",  "margin-left": "1.5rem"})
                ]),
    ]),
])


##########################
#Callback for page
##########################

@app.callback(
    Output('alert_noData1', 'is_open'),
    Output('yearDropdown1gdf', 'options'),
    Output('alert_noyear1', 'is_open'),
    Output('monthDropdown1', 'options'),
    Output('altitudeMapGdf', 'figure'),
    Output('dailytimeseries1', 'figure'),
    Output('gdfStatTable1', 'data'),
    Output('gdfStatTable1', 'columns'),
    Input('placeDropdown1', 'value'),
    Input('yearDropdown1gdf', 'value'),
    Input('monthDropdown1', 'value'),
)
def getUserOptions(stationNumber1, yearControl, monthControl):
    element_id = ctx.triggered_id if not None else 'No clicks yet'
    global dfControl
    global tempdfControl
    global tmpdf2Control
    
    ### for the first control graph
    if element_id == 'placeDropdown1':
        if stationNumber1 != None:
            DailyTimeSeriesControl = getDailyTimeSeries(stationNumber1)
            if DailyTimeSeriesControl == []:
                return True, dash.no_update, False, dash.no_update,dash.no_update, dash.no_update, dash.no_update,  dash.no_update,
            dfControl = pd.DataFrame(data=DailyTimeSeriesControl)
            allYearsControl = dfControl.Year.unique()
            return False, allYearsControl,False, dash.no_update,dash.no_update, dash.no_update, dash.no_update,  dash.no_update,
        else: 
            empty_years1 = []
            empty_months1 = []
            emptyKey = []
            emptyValue = []
            return False, empty_years1, False, empty_months1,go.Figure(), go.Figure(), emptyKey, emptyValue,
    elif element_id == 'yearDropdown1gdf':
        #need to put months in after years dataframe is created.
        if yearControl != None:
            tempdfControl = pd.DataFrame(columns = ["Year", "Month", "Day", "Value"])
            dfYearSubsetControl = dfControl[dfControl['Year'] == yearControl]
            tempdfControl = tempdfControl.append(dfYearSubsetControl)
            #convert the months to a value the user understands, while still keeping the int value (the function needs an int to work)
            month_labels = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
                9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
            tempdfControl['Month'] = tempdfControl['Month'].apply(lambda x: month_labels[x])
            allMonthsControl = tempdfControl.Month.unique()
            return False, dash.no_update, False, allMonthsControl,dash.no_update,  dash.no_update,  dash.no_update, dash.no_update, 
        else:
            empty_months1 = []
            emptyKey = []
            emptyValue = []
            return False, dash.no_update, True, empty_months1, dash.no_update, go.Figure(), emptyKey, emptyValue, 
    elif element_id == 'monthDropdown1':
        tmpdf2Control = pd.DataFrame(columns = ["Year", "Month", "Day", "Value"])
        if monthControl != None:
            for i in monthControl:
                dfMonthsubsetControl = tempdfControl[tempdfControl['Month'] == i]
                tmpdf2Control = tmpdf2Control.append(dfMonthsubsetControl)
        else:
            return False, dash.no_update, False, dash.no_update, dash.no_update, go.Figure(), dash.no_update, dash.no_update, 
        #time series
        figControl = px.line(tmpdf2Control, x="Day", y="Value", color='Month',color_discrete_sequence=px.colors.qualitative.Light24,  template="ggplot2")
        figControl.update_xaxes(title='Time (days)')
        figControl.update_yaxes(title='Flow (m3/s-1)')
        figControl.update_traces(mode="markers+lines", hovertemplate=None)
        figControl.update_layout(hovermode="x unified")
        ###########################################
        #for stat data frame
        ###########################################
        StatDataFrame = getgdfStatData(stationNumber1)
        StatKey = StatDataFrame.to_dict('records')
        StatValue = [{"name": i, "id": i} for i in StatDataFrame.columns]
        titleinfo = pd.DataFrame(data=StatDataFrame)
        location = titleinfo['Value'].iloc[1]
        river = titleinfo['Value'].iloc[2]
        figControl.update_layout(title=f"Gauged daily flow<br>{location} at {river} {yearControl}")
        #########################################
        #map
        #########################################
        Location = getMapLocation(stationNumber1)
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
            altmap.update_traces(hovertemplate=" River: %{customdata[0]} <br> Location: %{customdata[1]} <br> Station level: %{customdata[2]} m AOD (above ordnance datum)")
        else:
            altmap = px.scatter_mapbox(Locationdf, lat=Locationdf['latitude'], lon=Locationdf['longitude'], 
            size=Locationdf['latitude'].astype(float),
            custom_data=['river', 'name',],
            center=dict(lat=54.776496, lon=-1.976193), zoom=7.3,
            mapbox_style="open-street-map", height=300)
            altmap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            altmap.update_traces(hovertemplate="River: %{customdata[0]} <br> Location: %{customdata[1]}")
        return False, dash.no_update, False, dash.no_update, altmap,  figControl, StatKey, StatValue, 
    else:
        return False, dash.no_update, False, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, 
        #figControl.update_layout(transition_duration=500)
    return False, dash.no_update, False, dash.no_update, altmap, figControl, StatKey, StatValue, 
################################################################

#second graph
@app.callback(
    Output('alert_noData2', 'is_open'),
    Output('yearDropdown2', 'options'),
    Output('alert_noyear2', 'is_open'),
    Output('monthDropdown2', 'options'),
    Output('altitudeMapGdf2', 'figure'),
    Output('dailytimeseries2', 'figure'),
    Output('gdfStatTable2', 'data'),
    Output('gdfStatTable2', 'columns'),
    Input('placeDropdown2', 'value'),
    Input('yearDropdown2', 'value'),
    Input('monthDropdown2', 'value'),

)
def getUserOptions2(stationNumber, year, month):
    element_id = ctx.triggered_id if not None else 'No clicks yet'
    global dfTwo
    global tempdf
    global tmpdf2
    if element_id == 'placeDropdown2':
        if stationNumber != None:
            DailyTimeSeries = getDailyTimeSeries(stationNumber)
            if DailyTimeSeries == []:
                return True, dash.no_update, False, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
            dfTwo = pd.DataFrame(data=DailyTimeSeries)
            allYears = dfTwo.Year.unique()
            return False, allYears, False, dash.no_update , dash.no_update, dash.no_update, dash.no_update, dash.no_update
        else:
            empty_years = []
            empty_months = []
            emptyKey2 = []
            emptyValue2 = []
            return False, empty_years, False, empty_months,go.Figure(), go.Figure(), emptyKey2, emptyValue2,
    elif element_id == 'yearDropdown2':
        if year != None:
            tempdf = pd.DataFrame(columns = ["Year", "Month", "Day", "Value"])
            dfYearSubset = dfTwo[dfTwo['Year'] == year]
            tempdf = tempdf.append(dfYearSubset)
            #convert the months to a value the user understands, while still keeping the int value (the function needs an int to work)
            month_labels = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
                9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
            tempdf['Month'] = tempdf['Month'].apply(lambda x: month_labels[x])
            allMonths = tempdf.Month.unique()
            return False, dash.no_update, False, allMonths,dash.no_update, dash.no_update, dash.no_update, dash.no_update
        else:
            empty_months = []
            emptyKey2 = []
            emptyValue2 = []
            return False, dash.no_update, True, empty_months, dash.no_update, go.Figure(), emptyKey2, emptyValue2,
    elif element_id == 'monthDropdown2':
        tmpdf2 = pd.DataFrame(columns = ["Year", "Month", "Day", "Value"])
        if month != None:
            for i in month:
                dfMonthsubset = tempdf[tempdf['Month'] == i]
                tmpdf2 = tmpdf2.append(dfMonthsubset)
        else:
            return False, dash.no_update, False, dash.no_update, dash.no_update, go.Figure(), dash.no_update, dash.no_update, 
        fig = px.line(tmpdf2, x="Day", y="Value", color='Month', template="ggplot2", color_discrete_sequence=px.colors.qualitative.Light24)
        fig.update_xaxes(title='Time (days)')
        fig.update_yaxes(title='Flow (m3/s-1)')
        fig.update_traces(mode="markers+lines", hovertemplate=None)
        fig.update_layout(hovermode="x unified")
        ########################################
        #for stat data frame
        ########################################
        StatDataFrame2 = getgdfStatData(stationNumber)
        titleinfo = pd.DataFrame(data=StatDataFrame2)
        StatKey2 = StatDataFrame2.to_dict('records')
        StatValue2 = [{"name": i, "id": i} for i in StatDataFrame2.columns]
        location = titleinfo['Value'].iloc[1]
        river = titleinfo['Value'].iloc[2]
        fig.update_layout(title=f"Gauged daily flow <br> {location} at {river}  {year}")
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
            altmap2 = px.scatter_mapbox(AltitudeLocationData, lat=AltitudeLocationData['latitude'], lon=AltitudeLocationData['longitude'], 
                            size=AltitudeLocationData['latitude'].astype(float),
                            color_discrete_sequence=[AltitudeLocationData.color],
                            custom_data=['river', 'name', 'station-level'],
                            center=dict(lat=54.776496, lon=-1.976193), zoom=7.3,
                            mapbox_style="open-street-map", height=300)
            altmap2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            altmap2.update_traces(hovertemplate=" River: %{customdata[0]} <br> Location: %{customdata[1]} <br> Station level: %{customdata[2]} m AOD (above ordnance datum)")
        else:
            altmap2 = px.scatter_mapbox(Locationdf, lat=Locationdf['latitude'], lon=Locationdf['longitude'], 
            size=Locationdf['latitude'].astype(float),
            custom_data=['river', 'name',],
            center=dict(lat=54.776496, lon=-1.976193), zoom=7.3,
            mapbox_style="open-street-map", height=300)
            altmap2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            altmap2.update_traces(hovertemplate="River: %{customdata[0]} <br> Location: %{customdata[1]}")
        return False, dash.no_update, False, dash.no_update, altmap2, fig, StatKey2, StatValue2
    else:
        return False, dash.no_update, False, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    return False, dash.no_update, False, dash.no_update, altmap2, fig, StatKey2, StatValue2
