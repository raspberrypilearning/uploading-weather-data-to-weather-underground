## Using Python to upload our data

One of the great things about Python is the huge number of libraries that have been written. In this case you're going to use the *requests* module so make sure you've [installed](step_2.md) it.

[[[generic-python-requests]]]

1. Now you can make http requests using Python, let's construct the code to send your Weather Station data to Weather Underground. First of all,  create a few variables to hold important text strings.

    ```python
    # create a string to hold the first part of the URL
    WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
    WUid = "XXXXX" # Modify this variable so that in contains your PWS Id
    WUpwd = "YYYYYYY" # Modify this variable so that in contains your Password
    WUcreds = "ID=" + WUid + "&PASSWORD="+ WUpwd

    ```

    If you can't remember your PWS credentials you can always find them [here](https://www.wunderground.com/personal-weather-station/mypws).

1. Now, for each of the raw values from the Weather Station, this code performs any required conversion and then neatly formats the numerical vale to 2 decimal places.

    ```python
    ambient_temp_f = float("{0:.2f}".format(degc_to_degf(ambient_temp)))
    ground_temp_f = float("{0:.2f}".format(degc_to_degf(ground_temp)))
    humidity = float("{0:.2f}".format(humidity))
    pressure_in = float("{0:.2f}".format(pa_to_inches(pressure)))
    wind_speed_mph = float("{0:.2f}".format(khm_to_mph(wind_speed)))
    wind_gust_mph = float("{0:.2f}".format(khm_to_mph(wind_gust)))
    wind_average = float("{0:.2f}".format(wind_average))
    air_quality = float("{0:.2f}".format(air_quality))
    light = float("{0:.2f}".format(get_light()))
    rainfall_in = float("{0:.2f}".format(mm_to_inches(rainfall)))

    ```

 1. Then you can create a set of variables for each of the various parameters we need to include in the URL.

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
1. Note that you don't need to create a string for the date/timestamp of the reading. Weather Underground will create this value based on when it received the data if you use the parameter value 'now' in your http request. If you were storing weather readings and uploading them in bulk later, you would need to format a date/timestamp for each record before sending it.

1. Finally you can create the segment of the URL containing the measurement parameters and concatenate it with the domain name and directory part of the URL which you stored in the *WUurl*  variable earlier.

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
