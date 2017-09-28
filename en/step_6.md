## Using Python to upload your data

One of the great things about Python is the huge number of libraries that people have written and made available for free. Here you're going to use the `requests` module, so make sure you've installed it.

[[[generic-python-requests]]]



- Now that you can make HTTP requests using Python, let's construct the code to send your Weather Station data to Weather Underground. First of all, import the Requests library. Add this line to the top of WU-upload.py.

    ```python
    import requests
    ```

- Then add some variables to hold important text strings to

	```python
	# create a string to hold the first part of the URL
	WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
	WU_station_id = "XXXXX" # Modify this variable so that in contains your PWS Id
	WU_station_pwd = "YYYYYYY" # Modify this variable so that in contains your Password
	WUcreds = "ID=" + WUid + "&PASSWORD="+ WUpwd

	```

- If you can't find where you noted down the Personal Weather Station (PWS) credentials which Weather Underground issued you, you can always look them up [here](https://www.wunderground.com/personal-weather-station/mypws).

- Now you need to add each one of your weather readings. If the values are not stored as strings, then you'll need to convert them before you can add them to `WUurl`. Unless you're using very expensive sensors, the readings probably won't be accurate to more than a couple of decimal places so you can also round them appropriately. This will make the final URL much easier to read, which will help if you need to do any debugging. It is also good practice to only present data that does not claim to be more accurate than it really is.

[[[rounding-numbers-with-python]]]

- For each of the raw values from the Weather Station, write the code to perform any required conversion and to then neatly format the value to two decimal places.

- To get started, write the code to take an atmospheric pressure reading called `pressure`, which is a floating-point number. Convert it from pascals to inches of mercury, and then turn it into a string called `pressure_in` rounded to two decimal places.

--- hints ---
--- hint ---
- You can use the function you wrote earlier to perform the unit conversion.
    ```python
    def pa_to_inches(pressure_in_pa):
        pressure_in_inches_of_m = pressure_in_pa * 0.02953
        return pressure_in_inches_of_m
    pressure_in = pa_to_inches(pressure)
    ```
--- /hint ---
--- hint ---
- Now use `.format` to create the rounded string:
    ```python
    pressure_in = float("{0:.2f}".format(pa_to_inches(pressure)))
    ```
---/hint---
---/hints---

- You can then use the same process for all of your other weather readings. If you have a schools' Weather Station kit, that will produce measurements for ambient as well as ground temperature, humidity, wind speed, wind direction and gusts, and rainfall. Some of these values will need to be converted into the appropriate units, others just need to be rounded.

--- hints ---
--- hint ---
- Your code should look like this:
    ```python
    ambient_temp_f = float("{0:.2f}".format(degc_to_degf(ambient_temp)))
    ground_temp_f = float("{0:.2f}".format(degc_to_degf(ground_temp)))
    humidity = float("{0:.2f}".format(humidity))
    pressure_in = float("{0:.2f}".format(pa_to_inches(pressure)))
    wind_speed_mph = float("{0:.2f}".format(khm_to_mph(wind_speed)))
    wind_gust_mph = float("{0:.2f}".format(khm_to_mph(wind_gust)))
    wind_average = float("{0:.2f}".format(wind_average))
    rainfall_in = float("{0:.2f}".format(mm_to_inches(rainfall)))
    ```
---/hint---
---/hints---

 - Then you can create a set of variables for each of the various parameters we need to include in the URL.
    ```python
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
    ```
- Note that you don't need to create a string for the time stamp of the reading. Weather Underground will create this value based on when it received the data if you use the parameter value 'now' in your HTTP request. If you were storing weather readings and uploading them in bulk later, you would need to format a time stamp for each record before sending it.

- Finally you can create the segment of the URL containing the measurement parameters and concatenate it with the domain name and directory part of the URL which you stored in the `WUurl` variable.

    ```python
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

    ```
