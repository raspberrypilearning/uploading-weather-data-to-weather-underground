## Testing

- Before you modify your Weather Station code to include a Weather Underground upload, it is a good idea to test it first. Assemble all the various code elements above into a single file and then make up some test data for the normal Weather Station measurement variables:

| Measurement variable |
|--------------------|
| pressure |
| humidity |
| wind_average |
| ambient_temp |
| ground_temp |
| wind_speed |
| wind_gust |
| rainfall |


One easy way is to simply look at the last actual values recorded by your weather station and use those.

You can find an example of a Python test script [here](WU_test_upload.py).

- Run your code and check that your return code (r.status.code) is 200 and that you receive a *success* response (r.text). If your response is something else, check your code and make sure that your have included the correct PWS Id and password in your request.

- If your code produces the correct responses, visit your PWS page on the Weather Underground website and verify that your data has been uploaded. Check that the values make sense for the relevant units.
![](images/image3.png)

- Once you're happy with your tests, integrate this code with the scripts running on your Weather station. A simple way to do this is to modify the [log_all_sensors.py](https://github.com/raspberrypi/weather-station/blob/master/log_all_sensors.py) file which, if you've followed the [standard installation instructions](https://www.raspberrypi.org/learning/weather-station-guide/), should be run every 5 minutes via crontab. This is a sensible frequency for uploading to a site like Weather Underground.

--- hints ---
--- hint ---
If you get stuck, here is a basic example of a [modified log_all_sensors.py](log_all_sensorsWU.py) script.

--- /hint ---
--- /hints ---