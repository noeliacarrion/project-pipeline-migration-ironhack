import pandas as pd
import requests
import matplotlib.pyplot as plt
import acquisition 
import clean
import api

def read_file(file):
    my_dataframe = acquisition.open_data(file)
    return my_dataframe

def cleaning(my_dataframe):
    columns_deleted =['Web ID','Reported Date', 'Information Source', 'URL', 'UNSD Geographical Grouping', 'Source Quality']
    my_dataframe = clean.dropcolumns(my_dataframe,columns_deleted)
    my_dataframe['Cause of Death'] = my_dataframe['Cause of Death'].apply(clean.cleanCauseDeath)
    my_dataframe['Location Description'] = my_dataframe['Location Description'].apply(clean.cleanLocation)
    my_dataframe = clean.FilterNumberCountry(my_dataframe, 'Location Description')
    my_dataframe = clean.fillNaN(my_dataframe,'Number of Females')
    return my_dataframe

def datafromApi(my_dataframe):
    my_dataframe['latitud'] = my_dataframe['Location Coordinates'].apply(api.get_lat) 
    my_dataframe['latitud'] = my_dataframe['Location Coordinates'].apply(api.get_lat)
    my_dataframe['longitud'] = my_dataframe['Location Coordinates'].apply(api.get_lon)
    lista_marzo = api.Apidata(data_clean)
    lista_febrero = api.Apidata1(data_clean)
    lista_enero = api.Apidata2(data_clean)
    lista_diciembre = api.Apidata3(data_clean)
    lista_noviembre = api.Apidata4(data_clean)
    lista_apis = api.makeData([lista_marzo, lista_febrero, lista_enero, lista_diciembre, lista_noviembre])
    return lista_apis


if __name__ == "__main__":
    data = read_file('../Input/MissingMigrants.csv')
    BASE_URL = "https://api.darksky.net/forecast" 
    data_clean = cleaning(data)
    dataframe_api = datafromApi(data_clean)
