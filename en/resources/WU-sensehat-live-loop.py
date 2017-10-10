#!/usr/bin/python3
import requests
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

def hpa_to_inches(pressure_in_hpa):
    pressure_in_inches_of_m = pressure_in_hpa * 0.02953
    return pressure_in_inches_of_m

def degc_to_degf(temperature_in_c):
    temperature_in_f = (temperature_in_c * (9/5.0)) + 32
    return temperature_in_f


WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
WU_station_id = "ICAMBRID157"
WU_station_pwd = "fd8yqhwv"
WUcreds = "ID=" + WU_station_id + "&PASSWORD=" + WU_station_pwd
date_str = "&dateutc=now"
action_str = "&action=updateraw"

while True:

    humidity = sense.get_humidity()
    ambient_temp = sense.get_temperature()
    pressure = sense.get_pressure()

    humidity_str = "{0:2f}".format(humidity)
    ambient_temp_str = "{0:2f}".format(degc_to_degf(ambient_temp))
    pressure_str = "{0:2f}".format(hpa_to_inches(pressure))

    r = requests.get(
        WUurl +
        WUcreds +
        date_str +
        "&humidity=" + humidity_str +
        "&tempf=" + ambient_temp_str +
        "&baromin=" + pressure_str +
        action_str)

    print("Received " + str(r.status_code) + " " + str(r.text))
    sleep(300)
