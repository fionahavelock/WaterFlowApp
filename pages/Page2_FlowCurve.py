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
                html.H4("Flow Duration Curve Analysis"),
                html.H5(["Flow-duration curves are cumulative frequency curves that describe the amount of time a certain flow is equaled or exceeded during a given period. The percentage of time is shown against the flow value. The data used to create the flow duration plot is gauged daily flow – the average flow for each day.",html.Sup("1"),"This data is taken from the", html.A(" National River Flow Archive.", href ="https://nrfa.ceh.ac.uk/", id="linkInText")])
            ])
        ], style={ "margin-top": "3rem", "margin-right": "0.5rem",  "margin-left": "1.5rem"})
    ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("Select station. Select one or more years:")
                                ])
                            ])
                            ]),
                            dbc.CardGroup([
                                dbc.Card([
                                    dbc.CardBody([
                                        html.Div([
                                            dcc.Dropdown(options = [
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
                                            id='stationDropDown',)
                                            #end of html div for station drop down
                                        ]),
                                        html.Div([
                                            dbc.Alert(
                                                "There is no data availble for this station. Please select a different station.",
                                                    color="warning",
                                                        id="alert_noCurveData1",
                                                            dismissable=True,
                                                                is_open=False,)
                                    ])
                                    ]),
                                ]),
                                dbc.Card([
                                    dbc.CardBody([
                                        html.Div([
                                            dcc.Dropdown(
                                            multi=True,
                                            id='yearDropdownFlow',
                                            placeholder="Select a year",
                                            
                                            ),
                                        ])
                                    ])
                    #end of card 2 row 1
                    ])
                    ]),
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("Map of the North Pennines AONB and the selected location. Hover over the map to see station level in metres above ordnance datum."),
                                    html.Br(),
                                    dcc.Graph(id = 'altitudeMapCurveFlow')
                                ])
                            ])
                        ]),
                    html.Br(),
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                html.P("Flow duration curve showing a curve for all years by default. ‘All years’ shows the overall flow duration curve for that station. Comparing selected years against the overall flow duration curve provides insight into how exceptional a year is."),
                                html.Br(),
                                dcc.Graph(id ='flowDurationCurvePlot')
                            ]),
                        ])
                    ]),
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("The natural log of the flow duration curve provides more detail of the flow duration curve above."),
                                    html.Br(),
                                    dcc.Graph(id='NaturalLog')
                                    ]),
                            ])
                        ]),
                    html.Br(),
                            dbc.Card([
                                dbc.CardBody([
                                html.Div([
                                    html.P(["This flow duration curve plot shows the 95th, 50th and 10th percentiles. The flow value that is exceeded 95 per cent of the time (Q95) is a useful statistic for low flow analysis. The flow value that is exceeded 50 per cent of the time (Q50) is the median flow value. The flow value that is exceeded 10 per cent of the time (Q10) is a useful statistic for analysis of high flows and flooding.",html.Sup("2")]),
                                    html.Br(),
                                    dcc.Graph(id='percentile')
                                ])
                                ])
                            ]),

                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                            html.Div([
                                html.P(["Mass curves provide a way of determining the storage capacity necessary for specific flow measurements at a given station. The curve shows the cumulative sum of the flow values plotted against time.",html.Sup("3")]),
                                html.Br(),
                                dcc.Graph(id= 'MassCurve')
                            ])
                        ])
                        ])
                    ], style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "1rem",  "margin-left": "1rem"})
                ], md=6),
                ######################################################
                # Second section
                ######################################################
                dbc.Col([
                    dbc.Card([
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("Select station. Select one or more years:")
                                ])
                            ])
                        ]),
                            dbc.CardGroup([
                                dbc.Card([
                                    dbc.CardBody([
                                        html.Div([
                                            dcc.Dropdown(options = [
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
                                                "There is no data availble for this station. Please select a different station.",
                                                    color="warning",
                                                        id="alert_noCurveData2",
                                                            dismissable=True,
                                                                is_open=False,)
                                        ])
                                    ]),
                            ]),
                                dbc.Card([
                                    dbc.CardBody([
                                        html.Div([
                                            dcc.Dropdown(
                                            multi=True,
                                            id='yearDropdownFlow2',
                                            placeholder="Select a year",
                                            
                                            ),
                                        ])
                                    ])
                    #end of card 2 row 1
                    ])

                        ]),
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("Map of the North Pennines AONB and the selected location. Hover over the map to see station level in metres above ordnance datum."),
                                    html.Br(),
                                    dcc.Graph(id = 'altitudeMapCurveFlow2')
                                ])
                            ])
                        ]),
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("Flow duration curve showing a curve for all years by default. ‘All years’ shows the overall flow duration curve for that station. Comparing selected years against the overall flow duration curve provides insight into how exceptional a year is."),
                                    html.Br(),
                                    dcc.Graph(id ='flowDurationCurvePlot2')
                                ]),
                            ])
                        ]),
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.P("The natural log of the flow duration curve provides more detail of the flow duration curve above."),
                                    html.Br(),
                                    dcc.Graph(id='NaturalLog2')
                                    ]),
                            ])
                        ]),
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                            dbc.Card([
                                html.Div([
                                    html.P(["This flow duration curve plot shows the 95th, 50th and 10th percentiles. The flow value that is exceeded 95 per cent of the time (Q95) is a useful statistic for low flow analysis. The flow value that is exceeded 50 per cent of the time (Q50) is the median flow value. The flow value that is exceeded 10 per cent of the time (Q10) is a useful statistic for analysis of high flows and flooding.",html.Sup("2")]),
                                    html.Br(),
                                    dcc.Graph(id='percentile2')
                                ])
                            ])
                            ])
                        ]),
                    html.Br(),
                        dbc.Card([
                            dbc.CardBody([
                            html.Div([
                                html.P(["Mass curves provide a way of determining the storage capacity necessary for specific flow measurements at a given station. The curve shows the cumulative sum of the flow values plotted against time.",html.Sup("3")]),
                                html.Br(),
                                dcc.Graph(id= 'MassCurve2')

                            ])
                            ])
                        ])
                    ], style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "1rem",  "margin-left": "0.5rem"})

                ], md=6),
            #end of row
                dbc.Row([
                    html.Div([
                        html.Footer([
                            html.P("References:"),
                            html.Br(),
                            html.P([html.Sup(1)," Davie, T (2008) Fundamentals of Hydrology, Routledge. p.107",], style={"padding-bottom": "0.5rem"}),
                            html.P([html.Sup(2)," Davie, T (2008) Fundamentals of Hydrology, Routledge. p.108"], style={"padding-bottom": "0.5rem"}),
                            html.P([html.Sup(3)," Wilson, E (1974) Engineering Hydrology, The Macmillan Press. p.106"])
                        ])
                    ], style={ "margin-top": "2rem", "margin-bottom": "2rem", "margin-right": "0.5rem",  "margin-left": "1.5rem"})
                ]),
            ])
        #end of html Div
            ])

###################################
#first callback
@app.callback(
    Output('alert_noCurveData1', 'is_open'),
    Output('yearDropdownFlow', 'options'),
    Output('altitudeMapCurveFlow', 'figure'),
    Output('flowDurationCurvePlot', 'figure'),
    Output('NaturalLog', 'figure'),
    Output('percentile', 'figure'),
    Output('MassCurve', 'figure'),
    Input('stationDropDown', 'value'),
    Input('yearDropdownFlow', 'value'),
)

def callBackFlowAnayltics(stationNumber, selected_years):
    ######################
    #create global dataframes so the dataframes can be accessed
    global CurveFlowDatadf
    global allYears
    global massdf
    global curvedf
    element_id = ctx.triggered_id if not None else 'No clicks yet'
    if element_id == 'stationDropDown':
        if stationNumber != None:
            #########################################
            #curve flow data
            #########################################
            CurveFlowData = getTimeSeries('gdf', stationNumber)
            if CurveFlowData == []:
                return True, dash.no_update, dash.no_update, dash.no_update,dash.no_update,  dash.no_update, dash.no_update
            CurveFlowDatadf = pd.DataFrame(data=CurveFlowData)
            allYears = CurveFlowDatadf.Year.unique()
            return False, allYears, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
        else:
            empty_years = []
            return False, empty_years, go.Figure(), go.Figure(), go.Figure(), go.Figure(), go.Figure()
    elif element_id == 'yearDropdownFlow':
        #################################
        #curve flow
        #################################
        curvedf = pd.DataFrame(columns = ["Year", "Flow", "Exceedence"])
        massdf = pd.DataFrame(columns = ["Year", "Days",  "Value", "Alldays"])
        if selected_years != None:
            ############################
            #curve flow data generation
            ############################
            
            dfsubset = CurveFlowDatadf
            sort = np.sort(dfsubset['Value'])[::-1]
            #it will be one less without the one 
            # M = np.arange(1., len(sort)+1) 
            # n = len(sort)
            # arange creates a range, a rank list 
            exceedence = np.arange(1., len(sort)+1) / (len(sort)+1)
            x = sort
            y = exceedence*100
            curvedf = curvedf.append(pd.DataFrame({'Year': 'All Years', 'Exceedence': y, 'Flow': x}))

            for i in selected_years:
                ############################
                #mass curve
                ############################
                dfsubsetmass = CurveFlowDatadf[CurveFlowDatadf['Year'] == i]
                dfsubsetmass.insert(0, 'Alldays', range(0, len(dfsubsetmass), 1)) 
                massdf = massdf.append(pd.DataFrame({'Year': dfsubsetmass['Year'], 'Alldays': dfsubsetmass['Alldays'],'Value': dfsubsetmass['Value'] }))
                #massdf = massdf[massdf['Alldays'] == range(0, len(massdf), 1)]
                ############################
                #curve flow data generation
                ############################
                dfsubset = CurveFlowDatadf[CurveFlowDatadf['Year'] == i]
                sort = np.sort(dfsubset['Value'])[::-1]
                exceedence = np.arange(1.,len(sort)+1) / (len(sort)+1)
                x = sort
                y = exceedence*100
                curvedf = curvedf.append(pd.DataFrame({'Year': dfsubset['Year'], 'Exceedence': y, 'Flow': x}))
        else:
            return False, dash.no_update, dash.no_update, go.Figure(),  go.Figure(), go.Figure(), go.Figure()

        #########################################
        #Title information
        #########################################
        titleData = getgdfStatData(stationNumber)
        titleinfo = pd.DataFrame(data=titleData)
        location = titleinfo['Value'].iloc[1]
        river = titleinfo['Value'].iloc[2]
        #########################################
        #Mass curve figure
        #########################################
        massCurve1 = massdf.assign(sum=massdf.Value.cumsum())
        #massCurve1.insert(0, 'Alldays', range(0, len(massCurve1), 1))
        figMassControl = px.line(massCurve1, x="Alldays", y="sum", color='Year',
        template="ggplot2", color_discrete_sequence=px.colors.qualitative.Light24)
        figMassControl.update_xaxes(title='Time (days)')
        figMassControl.update_yaxes(title='Runoff')
        figMassControl.update_traces( hovertemplate=None)
        figMassControl.update_layout(hovermode="x unified")
        figMassControl.update_layout(title=f"Cumulative mass curve of runoff <br> {location} at {river}")
        #########################################
        #curve flow figure
        #########################################
        fig = px.line(curvedf, y="Flow", x="Exceedence", color="Year", template="ggplot2", color_discrete_map={"All Years": '#869FA3'},color_discrete_sequence=px.colors.qualitative.Light24)
        fig.update_xaxes(title='% time flow exceeded')
        fig.update_yaxes(title='Flow (m3/s-1)')
        fig.update_layout(title=f"Flow duration curve <br> {location} at {river}")
        fig.update_traces(hovertemplate=None)
        fig.update_layout(hovermode="x unified")
        #################################################
        #########################################
        #natural log scale flow duration
        #########################################
        curvedf['natural_log'] = np.log(curvedf['Flow'])
        figLog = px.line(curvedf, y="natural_log", x="Exceedence", color="Year",  template="ggplot2", color_discrete_map={"All Years": '#869FA3'}, color_discrete_sequence=px.colors.qualitative.Light24)
        figLog.update_xaxes(title='% time flow exceeded')
        figLog.update_yaxes(title='Ln Flow (m3 s-1)')
        figLog.update_layout(title=f"Natural log flow duration curve <br> {location} at {river}")
        figLog.update_traces( hovertemplate=None)
        figLog.update_layout(hovermode="x unified")
        #remove all years
        #idx = (curvedf['Year'] != 'All Years').idxmax()
        #sort descending and get max year
        #append max year to dataframe
        #update graph to shpw max year

        #########################################
        #percentile flow duration
        #########################################
        arr = curvedf['Flow']
        pc10 = np.percentile(arr, 10)
        pc50 = np.percentile(arr, 50)
        pc95 = np.percentile(arr, 95)
        figPc = px.line(curvedf, y="Flow", x="Exceedence", color="Year", template="ggplot2", color_discrete_map={"All Years": '#869FA3'}, color_discrete_sequence=px.colors.qualitative.Light24)
        figPc.update_xaxes(title='% time flow exceeded')
        figPc.update_yaxes(title='Flow (m3 s-1)')
        figPc.update_layout(title=f"10th, 50th, 95th percentile flow duration curve <br> {location} at {river}")
        figPc.add_vline(x=pc10, line_width=3, line_color="blue",
                line_dash="dot", 
                annotation_text="10th percentile",
                annotation_position="top right",
                annotation_font_size=12,
                annotation_font_color="blue")
        figPc.add_vline(x=pc50, line_width=3,  line_color="green",
                line_dash="dot", 
                annotation_text="<br> <br> <br> 50th percentile",
                annotation_position="top right",
                annotation_font_size=12,
                annotation_font_color="green")
        figPc.add_vline(x=pc95, line_width=3, line_color="red",
                line_dash="dot", 
                annotation_text="<br> <br> <br><br> <br> <br> 95th percentile",
                annotation_position="top right",
                annotation_font_size=12,
                annotation_font_color="red")
        figPc.update_traces( hovertemplate=None)
        figPc.update_layout(hovermode="x unified")
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
        return False, dash.no_update, altmap, fig, figLog, figPc, figMassControl
    else:
        return False, dash.no_update, dash.no_update,  dash.no_update,  dash.no_update, dash.no_update, dash.no_update
    return False, dash.no_update, altmap, fig,  figLog, figPc, figMassControl
############################################
#Second app callback
@app.callback(
    Output('alert_noCurveData2', 'is_open'),
    Output('yearDropdownFlow2', 'options'),
    Output('altitudeMapCurveFlow2', 'figure'),
    Output('flowDurationCurvePlot2', 'figure'),
    Output('NaturalLog2', 'figure'),
    Output('percentile2', 'figure'),
    Output('MassCurve2', 'figure'),
    Input('stationDropDown2', 'value'),
    Input('yearDropdownFlow2', 'value'),
)

def callBackFlowAnayltics(stationNumber2, selected_years2):
    ######################
    #create global dataframes so the dataframes can be accessed
    global CurveFlowDatadf2
    global allYears2
    global massdf2
    global curvedf2
    element_id = ctx.triggered_id if not None else 'No clicks yet'
    if element_id == 'stationDropDown2':
        if stationNumber2 != None:
            #########################################
            #curve flow data
            #########################################
            CurveFlowData2 = getTimeSeries('gdf', stationNumber2)
            if CurveFlowData2 == []:
                return True, dash.no_update, dash.no_update, dash.no_update,dash.no_update,  dash.no_update, dash.no_update
            CurveFlowDatadf2 = pd.DataFrame(data=CurveFlowData2)
            allYears2 = CurveFlowDatadf2.Year.unique()
            return False, allYears2,  dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
        else:
            empty_years2 = []
            return False, empty_years2, go.Figure(), go.Figure(), go.Figure(), go.Figure(), go.Figure()
    elif element_id == 'yearDropdownFlow2':
        #################################
        #curve flow
        #################################
        curvedf2 = pd.DataFrame(columns = ["Year", "Flow", "Exceedence"])
        massdf2 = pd.DataFrame(columns = ["Year", "Days",  "Value", "Alldays"])
        if selected_years2 != None:
            ############################
            #curve flow data generation
            ############################
            
            dfsubset2 = CurveFlowDatadf2
            sort = np.sort(dfsubset2['Value'])[::-1]
            exceedence = np.arange(1.,len(sort)+1) / len(sort)
            x = sort
            y = exceedence*100
            curvedf2 = curvedf2.append(pd.DataFrame({'Year': 'All Years', 'Exceedence': y, 'Flow': x}))

            for i in selected_years2:
                ############################
                #mass curve
                ############################
                dfsubsetmass2 = CurveFlowDatadf2[CurveFlowDatadf2['Year'] == i]
                dfsubsetmass2.insert(0, 'Alldays', range(0, len(dfsubsetmass2), 1)) 
                massdf2 = massdf2.append(pd.DataFrame({'Year': dfsubsetmass2['Year'], 'Alldays': dfsubsetmass2['Alldays'],'Value': dfsubsetmass2['Value'] }))
                #massdf = massdf[massdf['Alldays'] == range(0, len(massdf), 1)]
                ############################
                #curve flow data generation
                ############################
                dfsubset2 = CurveFlowDatadf2[CurveFlowDatadf2['Year'] == i]
                sort = np.sort(dfsubset2['Value'])[::-1]
                exceedence = np.arange(1.,len(sort)+1) / len(sort)
                x = sort
                y = exceedence*100
                curvedf2 = curvedf2.append(pd.DataFrame({'Year': dfsubset2['Year'], 'Exceedence': y, 'Flow': x}))
        else:
            return False, dash.no_update,  dash.no_update, go.Figure(),  go.Figure(), go.Figure(), go.Figure()

        #########################################
        #Title information
        #########################################
        titleData2 = getgdfStatData(stationNumber2)
        titleinfo2 = pd.DataFrame(data=titleData2)
        location2 = titleinfo2['Value'].iloc[1]
        river2 = titleinfo2['Value'].iloc[2]
        #########################################
        #Mass curve figure
        #########################################
        massCurve2 = massdf2.assign(sum=massdf2.Value.cumsum())
        #massCurve1.insert(0, 'Alldays', range(0, len(massCurve1), 1))
        figMassControl2 = px.line(massCurve2, x="Alldays", y="sum", color='Year',
         template="ggplot2", color_discrete_sequence=px.colors.qualitative.Light24)
        figMassControl2.update_xaxes(title='Time (days)')
        figMassControl2.update_yaxes(title='Runoff')
        figMassControl2.update_traces( hovertemplate=None)
        figMassControl2.update_layout(hovermode="x unified")
        figMassControl2.update_layout(title=f"Cumulative mass curve of runoff <br> {location2} at {river2}")
        #########################################
        #curve flow figure
        #########################################
        fig2 = px.line(curvedf2, y="Flow", x="Exceedence", color="Year", template="ggplot2", color_discrete_map={"All Years": '#869FA3'}, color_discrete_sequence=px.colors.qualitative.Light24)
        fig2.update_xaxes(title='% time flow exceeded')
        fig2.update_yaxes(title='Flow (m3 s-1)')
        fig2.update_layout(title=f"Flow duration curve <br> {location2} at {river2}")
        fig2.update_traces(hovertemplate=None)
        fig2.update_layout(hovermode="x unified")
        #################################################
        #########################################
        #natural log scale flow duration
        #########################################
        curvedf2['natural_log'] = np.log(curvedf2['Flow'])
        figLog2= px.line(curvedf2, y="natural_log", x="Exceedence", color="Year",  template="ggplot2", color_discrete_map={"All Years": '#869FA3'}, color_discrete_sequence=px.colors.qualitative.Light24)
        figLog2.update_xaxes(title='% time flow exceeded')
        figLog2.update_yaxes(title='Ln Flow (m3 s-1)')
        figLog2.update_layout(title=f"Natural Log flow duration curve <br> {location2} at {river2}")
        figLog2.update_traces( hovertemplate=None)
        figLog2.update_layout(hovermode="x unified")
        #remove all years
        #idx = (curvedf['Year'] != 'All Years').idxmax()
        #sort descending and get max year
        #append max year to dataframe
        #update graph to shpw max year

        #########################################
        #percentile flow duration
        #########################################
        arr2 = curvedf2['Flow']
        pc102 = np.percentile(arr2, 10)
        pc502 = np.percentile(arr2, 50)
        pc952 = np.percentile(arr2, 95)
        figPc2 = px.line(curvedf2, y="Flow", x="Exceedence", color="Year", template="ggplot2", color_discrete_map={"All Years": '#869FA3'}, color_discrete_sequence=px.colors.qualitative.Light24)
        figPc2.update_xaxes(title='% time flow exceeded')
        figPc2.update_yaxes(title='Flow (m3 s-1)')
        figPc2.update_layout(title=f"10th, 50th, 95th percentile flow duration curve <br> {location2} at {river2}")
        figPc2.add_vline(x=pc102, line_width=3, line_color="blue",
                line_dash="dot", 
                annotation_text="10th percentile",
                annotation_position="top right",
                annotation_font_size=12,
                annotation_font_color="blue")
        figPc2.add_vline(x=pc502, line_width=3,  line_color="green",
                line_dash="dot", 
                annotation_text="<br> <br> <br> 50th percentile",
                annotation_position="top right",
                annotation_font_size=12,
                annotation_font_color="green")
        figPc2.add_vline(x=pc952, line_width=3, line_color="red",
                line_dash="dot", 
                annotation_text="<br> <br> <br><br> <br> <br> 95th percentile",
                annotation_position="top right",
                annotation_font_size=12,
                annotation_font_color="red")
        figPc2.update_traces( hovertemplate=None)
        figPc2.update_layout(hovermode="x unified")
        #########################################
        #map
        #########################################
        Location2 = getMapLocation(stationNumber2)
        Locationdf2 = pd.DataFrame(data=Location2)
        indexCol2 = []
        for value in Locationdf2["Value"]:
            indexCol2.append(0)
        Locationdf2["Index"] = indexCol2
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
        return False, dash.no_update,altmap2, fig2, figLog2, figPc2, figMassControl2
    else:
        return False, dash.no_update,  dash.no_update, dash.no_update,  dash.no_update, dash.no_update, dash.no_update
    return False, dash.no_update, altmap2, fig2,  figLog2, figPc2, figMassControl2
############################################





###################################
#Range
"""
curvedfRange = pd.DataFrame(columns = ["Year", "Flow", "Exceedence"])
#for total

for i in allYears:
    dfsubset = CurveFlowDatadf[CurveFlowDatadf['Year'] == i]
    sort = np.sort(dfsubset['Value'])[::-1]
    exceedence = np.arange(1.,len(sort)+1) / len(sort)
    x = sort
    y = exceedence*100
    curvedf = curvedf.append(pd.DataFrame({'Year': 'Range', 'Exceedence': y, 'Flow': x}))
    #to plot the lowest
#lowestFlow = min(x)
#curvedf = curvedf.append(pd.DataFrame({'Year': 'Lowest Flow', 'Exceedence': y,'Flow': lowestFlow}))
#highestFlow = max(x)
#curvedf = curvedf.append(pd.DataFrame({'Year': 'Highest Flow', 'Exceedence': y,'Flow': highestFlow}))
"""

