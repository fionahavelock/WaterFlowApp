##################
#API imports
import requests
import json

##################
#Data management imports
import pandas as pd


###################
#Strings to build the API web address

base_url = "https://nrfaapps.ceh.ac.uk/nrfa/ws/"
dataObject = "format=json-object"
timeSeries = "time-series?"
metaData = "station-info?"

#region help (Query API)
#######################
# Query API using requests and get repsonse as a json object
def queryAPI(query):
    response = requests.get(query)
    response = response.json()
    return response

#endregion

#You can only access time series data by station ID. This means we need to allow the user to choose a station ID (location)
#for curve flow data
#########################################

#API for the curve flow duration page(page 1) as well as the annual max and min page(page 3)
#This API uses the flow type and station number as the input

#########################################
def getTimeSeries(flowType, stationNumber):
    jsonData = queryAPI(base_url + timeSeries + dataObject + "&data-type=" + flowType + "&station=" + stationNumber)
    #make every even number a column and every odd number a column
    index = 0
    dataList = []
    #create empty dictionary
    tempDictionary = {}
    for i in jsonData['data-stream']:
        if index % 2 == 0:
            #spilt string to make the time series graph 
            date = i.split("-")
            tempDictionary['Year'] = int(date[0])
            tempDictionary['Month'] = int(date[1])
            tempDictionary['Day'] = int(date[2])
        else:
            tempDictionary['Value'] = i
            dataList.append(tempDictionary.copy())
        index +=1
    return dataList

###############################
#Map fpr the flow duration curve page and gauged daily flow

def getMapLocation(stationNumber):
    jsonMapData = queryAPI(base_url + metaData + "station=" + stationNumber + "&" + dataObject + "&fields=id,name,river,latitude,longitude,station-level")
    mapDatafromJson = jsonMapData['data'][0]
    dataList = []
    tempDictionary ={}
    for key,value in mapDatafromJson.items():
        tempDictionary['Key'] = key
        if value == None:
            value = 'N/A'
        tempDictionary['Value'] = value
        dataList.append(tempDictionary.copy())
    #mapdataframe = pd.DataFrame(dataList)
    return dataList

#########################################

#API for the gauged daily flow page. 
#This API uses only the station number as the input

#########################################
def getDailyTimeSeries(stationNumber):
    jsonData = queryAPI(base_url + timeSeries + dataObject + "&data-type=" + "gdf" + "&station=" + stationNumber)
    #make every even number a column and every odd number a column
    index = 0
    dataList = []
    #create empty dictionary
    tempDictionary = {}
    for i in jsonData['data-stream']:
        if index % 2 == 0:
            #spilt string to make the time series graph 
            date = i.split("-")
            tempDictionary['Year'] = int(date[0])
            tempDictionary['Month'] = int(date[1])
            tempDictionary['Day'] = int(date[2])
        else:
            tempDictionary['Value'] = i
            dataList.append(tempDictionary.copy())
        index +=1
    return dataList

################################
#for runoff precipation correlation
#for daily flow (runoff)
def getDailyTimeSeriesRunoff(stationNumber):
    jsonData = queryAPI(base_url + timeSeries + dataObject + "&data-type=" + "gdf" + "&station=" + stationNumber)
    #make every even number a column and every odd number a column
    index = 0
    dataList = []
    #create empty dictionary
    tempDictionary = {}
    for i in jsonData['data-stream']:
        if index % 2 == 0:
            #spilt string to make the time series graph 
            date = i.split("-")
            tempDictionary['Year'] = int(date[0])
            tempDictionary['Month'] = int(date[1])
            tempDictionary['Day'] = int(date[2])
        else:
            tempDictionary['Runoff'] = i
            dataList.append(tempDictionary.copy())
        index +=1
    return dataList

#for catchment daily rainfall
def getDailyTimeSeriescdr(stationNumber):
    jsonData = queryAPI(base_url + timeSeries + dataObject + "&data-type=" + "cdr" + "&station=" + stationNumber)
    #make every even number a column and every odd number a column
    index = 0
    dataList = []
    #create empty dictionary
    tempDictionary = {}
    for i in jsonData['data-stream']:
        if index % 2 == 0:
            #spilt string to make the time series graph 
            date = i.split("-")
            tempDictionary['Year'] = int(date[0])
            tempDictionary['Month'] = int(date[1])
            tempDictionary['Day'] = int(date[2])
        else:
            tempDictionary['Rainfall'] = i
            dataList.append(tempDictionary.copy())
        index +=1
    return dataList
################################
#end runoff precipation correlation

#get daily flow statistics
#https://nrfaapps.ceh.ac.uk/nrfa/ws/station-info?station=43009&format=json-object&fields=id,name,grid-reference,lat-long,river
def getgdfStatData(stationNumber):
    jsongdfStatData = queryAPI(base_url + metaData + "station=" + stationNumber + "&" + dataObject + "&fields=location,river,gdf-mean-flow,gdf-min-flow,gdf-first-date-of-min,gdf-last-date-of-min,gdf-max-flow,gdf-first-date-of-max,gdf-last-date-of-max,factors-affecting-runoff,description-flow-regime,description-station-hydrometry")
    gdfStatDatafromJson = jsongdfStatData['data'][0]
    dataList = []
    tempDictionary ={}
    for key,value in gdfStatDatafromJson.items():
        tempDictionary['Key'] = key
        if value == None:
            value = 'N/A'
        tempDictionary['Value'] = value
        dataList.append(tempDictionary.copy())
    gdfStatdataframe = pd.DataFrame(dataList)
    return gdfStatdataframe


#########################################

#API for the annual maximum page. 
#This API uses only the station number as the input

#########################################
def getBankfullData(stationNumber):
    jsonMapData = queryAPI(base_url + metaData + "station=" + stationNumber + "&" + dataObject + "&fields=bankfull-flow")
    mapDatafromJson = jsonMapData['data'][0]
    dataList = []
    tempDictionary ={}
    for key,value in mapDatafromJson.items():
        tempDictionary['Key'] = key
        if value == None:
            value = 'N/A'
        tempDictionary['Value'] = value
        dataList.append(tempDictionary.copy())
    #mapdataframe = pd.DataFrame(dataList)
    return dataList


def getTimeSeriesAmax(flowType, stationNumber):
    jsonData = queryAPI(base_url + timeSeries + dataObject + "&data-type=" + flowType + "&station=" + stationNumber)
    #make every even number a column and every odd number a column
    index = 0
    dataList = []
    #create empty dictionary
    tempDictionary = {}
    for i in jsonData['data-stream']:
        if index % 2 == 0:
            #spilt string to make the time series graph 
            date = i.split("-")
            tempDictionary['Year'] = int(date[0])
            tempDictionary['Month'] = int(date[1])
        else:
            tempDictionary['Value'] = i
            dataList.append(tempDictionary.copy())
        index +=1
    return dataList