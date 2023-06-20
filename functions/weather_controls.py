import requests
import json
from datetime import datetime
import time
# from dotenv import dotenv_values
import os
from get_location import *

# Temperature Conversion Functions

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius)

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return round(fahrenheit)


# Load the environment variables
# dotenv_values('.env')

print(time.tzname[0])
# API Setup / Variables Required
def weather_checker():
    """ Contacts Open Weather Map API and Pulls Current Data Requested """
    
    # Enter your API key here
    api_key = "b8a2b9e1073dd3f990bdc8717b6d8f9d"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
 
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + location_city
    
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    
    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
    
        # store the value of "main"
        # key in variable y
        y = x["main"]
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
    
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
    
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
    
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
        
        #Imperial Measurements
        if get_measurement_system() == "imperial":
            # print following values
            current_temperature = kelvin_to_fahrenheit(current_temperature)
            print(" Temperature  = " +
                        str(current_temperature) + "°F" +
              "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
              "\n humidity (in percentage) = " +
                        str(current_humidity) +
              "\n description = " +
                        str(weather_description))
            
        # Metric Measurements
        elif get_measurement_system() == "metric":
            current_temperature = kelvin_to_celsius(current_temperature)
            print(" Temperature  = " +
                        str(current_temperature) + "°F" +
              "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
              "\n humidity (in percentage) = " +
                        str(current_humidity) + "%" +
              "\n description = " +
                        str(weather_description))
        else:
            print(" City Not Found ")