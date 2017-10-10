
## Using live data

- For testing and development, you used some made-up data values, stored as variables in your code. Once you've tested your upload, you should delete these and use the code to process real data from your weather station.

[[[rpi-sensehat-temperature]]]

[[[rpi-sensehat-pressure]]]

[[[rpi-sensehat-humidity]]]

![](images/image3.png)

- To perform regular uploads, you could have a one-shot script which is run at set intervals using **Cron**.

[[[nix-bash-crontab]]]

--- hints ---
--- hint ---
If you get stuck, here is a basic example of a simple data uploader based on the Sense HAT.

```python
#!/usr/bin/python3
import requests
from sense_hat import SenseHat

sense = SenseHat()

humidity = sense.get_humidity()
ambient_temp = sense.get_temperature()
pressure = sense.get_pressure()

WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
WU_station_id = "XXXXXX" # modify with your PWS ID
WU_station_pwd = "YYYYYY" # modify with your PWS password
WUcreds = "ID=" + WU_station_id + "&PASSWORD=" + WU_station_pwd
date_str = "&dateutc=now"
action_str = "&action=updateraw"

def hpa_to_inches(pressure_in_hpa):
    pressure_in_inches_of_m = pressure_in_hpa * 0.02953
    return pressure_in_inches_of_m

def degc_to_degf(temperature_in_c):
    temperature_in_f = (temperature_in_c * (9/5.0)) + 32
    return temperature_in_f

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
```

--- /hint ---
--- hint ---
Edit your crontab file by typing the following command in a terminal window:
    ```
    crontab -e
    ```

--- /hint ---
--- hint ---
Then add the following line to your crontab file:
    ```
    */5 * * * * python3 /home/pi/WU-sensehat-live.py
    ```
--- /hint ---
--- /hints ---

- Alternatively, you could wrap your code for measuring and uploading in a loop and pause between iterations.

[[[generic-python-while-true]]]

--- hints ---
--- hint ---
You may need to re-arrange your code somewhat so that only the lines which deal with measurement and upload are inside the loop. All string definitions that do not change for each reading should be outside of the loop.
--- /hint ---
--- hint ---
If you get stuck, here is a basic example of a simple data uploader based on the Sense HAT script.

```python
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
```

--- /hint ---

--- /hints ---

--- collapse ---
---
title: Notes for Raspberry Pi Oracle Weather Station schools
---

The Oracle Weather Station software uses the crontab method to run a Python script called [log_all_sensors.py](https://github.com/raspberrypi/weather-station/blob/master/log_all_sensors.py) every five minutes. A simple way to modify your Weather Station so that it regularly uploads data to Weather Underground is to add the upload code you have written to this file.

If you've followed the [standard installation instructions](https://www.raspberrypi.org/learning/weather-station-guide/), this script should be run every five minutes, which is a sensible frequency for uploading to a site like Weather Underground.

If you get stuck, here is a basic example of a [modified log_all_sensors.py](resources/log_all_sensorsWU.py) script.

--- /collapse ---

Once you have data uploading regularly, you can use your Weather Underground PWS page to see how your local climate is changing over time.

![](images/image4.png)

