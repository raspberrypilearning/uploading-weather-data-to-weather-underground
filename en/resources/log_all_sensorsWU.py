#!/usr/bin/python
import time
import requests
from datetime import datetime as dt
import sys
import interrupt_client, MCP342X, wind_direction, HTU21D, bmp085, tgs2600, ds18b20_therm
import database # requires MySQLdb python 2 library which is not ported to python 3 yet

# ------- WU URL and credentials ---------

WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
WUid = "XXXXXXX" # add your WS ID
WUpwd = "ZZZZZZZ" # add your password
WUcreds = "ID=" + WUid + "&PASSWORD="+ WUpwd


def pa_to_inches(pressure_in_pa):
    pressure_in_inches_of_m = pressure_in_pa * 0.02953
    return pressure_in_inches_of_m

def mm_to_inches(rainfall_in_mm):
    rainfall_in_inches = rainfall_in_mm * 0.0393701
    return rainfall_in_inches

def khm_to_mph(speed_in_kmh):
    speed_in_mph = speed_in_kmh * 0.621371
    return speed_in_mph

def degc_to_degf(temperature_in_c):
    temperature_in_f = (temperature_in_c * (9/5.0)) + 32
    return temperature_in_f

pressure = bmp085.BMP085()
temp_probe = ds18b20_therm.DS18B20()
air_qual = tgs2600.TGS2600(adc_channel = 0)
humidity = HTU21D.HTU21D()
wind_dir = wind_direction.wind_direction(adc_channel = 0, config_file="wind_direction.json")
interrupts = interrupt_client.interrupt_client(port = 49501)

db = database.weather_database() #Local MySQL db

wind_average = wind_dir.get_value(10) #ten seconds
ambient_temp = humidity.read_temperature()
ground_temp =  temp_probe.read_temp()
air_quality = air_qual.get_value()
pressure = pressure.get_pressure()
humidity = humidity.read_humidity()
wind_speed = interrupts.get_wind()
wind_gust =  interrupts.get_wind_gust()
rainfall = interrupts.get_rain()

print("Inserting...")

db.insert(ambient_temp, ground_temp, air_quality, pressure, humidity, wind_average, wind_speed, wind_gust, rainfall)
print("done")

interrupts.reset()

ambient_temp_f = float("{0:.2f}".format(degc_to_degf(ambient_temp)))
ground_temp_f = float("{0:.2f}".format(degc_to_degf(ground_temp)))
ambient_temp = float("{0:.2f}".format(ambient_temp))
ground_temp = float("{0:.2f}".format(ground_temp))
humidity = float("{0:.2f}".format(humidity))
pressure_in = float("{0:.2f}".format(pa_to_inches(pressure)))
pressure = float("{0:.2f}".format(pressure))
wind_speed_mph = float("{0:.2f}".format(khm_to_mph(wind_speed)))
wind_speed = float("{0:.2f}".format(wind_speed))
wind_gust_mph = float("{0:.2f}".format(khm_to_mph(wind_gust)))
wind_gust = float("{0:.2f}".format(wind_gust))
wind_average = float("{0:.2f}".format(wind_average))
air_quality = float("{0:.2f}".format(air_quality))
rainfall_in = float("{0:.2f}".format(mm_to_inches(rainfall)))
rainfall = float("{0:.2f}".format(rainfall))

# Weatherunderground
print("uploading to Weatherunderground")

f_date = "&dateutc=now"
f_humid = "&humidity=" + str(humidity)
f_wspeed = "&windspeedmph=" + str(wind_speed_mph)
f_gust = "&windgustmph=" + str(wind_gust_mph)
f_airtemp = "&tempf=" +  str(ambient_temp_f)  # degrees F
f_rain = "&rainin=" + str(rainfall_in)
f_press = "&baromin=" + str(pressure_in)   # inches
f_groundtemp = "&soiltempf=" + str(ground_temp_f)   # degrees F
f_winddir = "&winddir=" + str(wind_average)
f_action = "&action=updateraw"
r= requests.get(WUurl+WUcreds+f_date+f_humid+f_wspeed+f_winddir+f_gust+f_airtemp+f_rain+f_press+f_groundtemp+f_action)
print("Received " + str(r.status_code) + " " + str(r.text) + " from WU")
