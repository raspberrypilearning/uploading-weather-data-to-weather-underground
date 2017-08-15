import time
import requests

WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
WUid = "-----" # modify this variable with your PWS ID
WUpwd = "------" # modify this variable with your PWS password
WUcreds = "ID=" + WUid + "&PASSWORD="+ WUpwd

pressure = 1017
humidity = 55
wind_average = 120
ambient_temp = 21
ground_temp =  19
wind_speed = 5.2
wind_gust =  10.2
rainfall = 1.5

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

ambient_temp_f = float("{0:.2f}".format(degc_to_degf(ambient_temp)))
ground_temp_f = float("{0:.2f}".format(degc_to_degf(ground_temp)))
humidity = float("{0:.2f}".format(humidity))
pressure_in = float("{0:.2f}".format(pa_to_inches(pressure)))
wind_speed_mph = float("{0:.2f}".format(khm_to_mph(wind_speed)))
wind_gust_mph = float("{0:.2f}".format(khm_to_mph(wind_gust)))
wind_average = float("{0:.2f}".format(wind_average))
rainfall_in = float("{0:.2f}".format(mm_to_inches(rainfall)))

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
#r= requests.get(WUurl+WUcreds+f_date+f_humid+f_wspeed+f_winddir+f_gust+f_airtemp+f_rain+f_press+f_groundtemp+f_action)
r= requests.get(
    WUurl+WUcreds +
    f_date+f_humid +
    f_wspeed +
    f_winddir +
    f_gust +
    f_airtemp +
    f_rain +
    f_press +
    f_groundtemp +
    f_action)
print("Received " + str(r.status_code) + " " + str(r.text) + " from WU")
