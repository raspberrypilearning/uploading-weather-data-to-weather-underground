## Using Python to upload our data

One of the great things about Python is the huge number of libraries that have been written. In this case you're going to use the *requests* module so make sure you've [installed](step_2.md) it.

[[[generic-python-requests]]]

- Now you can make http requests using Python, let's construct the code to send your Weather Station data to Weather Underground. First of all,  create a few variables to hold important text strings.

    ```python
    # create a string to hold the first part of the URL
    WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
    WUid = "XXXXX" # Modify this variable so that in contains your PWS Id
    WUpwd = "YYYYYYY" # Modify this variable so that in contains your Password
    WUcreds = "ID=" + WUid + "&PASSWORD="+ WUpwd

    ```

    If you can't remember your PWS credentials you can always find them [here](https://www.wunderground.com/personal-weather-station/mypws).

- Now you need to add in each one of your weather readings. If the values are not stored as strings then you'll need to convert them before you can add them to `WUurl`. Unless you're using very expensive sensors, the readings probably won't be accurate to more than a couple of decimal places so you can also round them appropriately. This will make the final URL much easier to read if you need to do any debugging. It is also good practice to only present data that appears to be more precise than it really is.

[[[rounding-numbers-with-python]]]

- Now, for each of the raw values from the Weather Station, write the code performs any required conversion and then neatly formats the numerical vale to 2 decimal places.

- To get you started, write the code to take an atmospheric pressure reading `pressure` which is a **float**, convert it from Pascals to Inches of Mercury, and then convert it to a string `pressure_in` rounded to 2 decimal places.

--- hints ---
--- hint ---
- First of all, you can use the function you wrote earlier to perform the units conversion.
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

- You can then use the same process for all of the other weather readings that you have. If you have a schools' Weather Station Kit, that will produce ambient & ground temperature, humidity, wind speed, direction & gusts and  rainfall values. Some of these will need converting into the appropriate units, others just need to be rounded.

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
- Note that you don't need to create a string for the date/timestamp of the reading. Weather Underground will create this value based on when it received the data if you use the parameter value 'now' in your http request. If you were storing weather readings and uploading them in bulk later, you would need to format a date/timestamp for each record before sending it.

- Finally you can create the segment of the URL containing the measurement parameters and concatenate it with the domain name and directory part of the URL which you stored in the *WUurl*  variable earlier.

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
