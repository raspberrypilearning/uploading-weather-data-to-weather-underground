## Testing

- If you're using an Oracle Weather Station, Before you modify your weather station code to include a Weather Underground upload, it is a good idea to test your new section of code. Assemble all the various code elements above into a single file and then make up some test data for the normal Weather Station measurement variables:

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
||


- One easy way is to use last actual values recorded by your weather station.

You can find an example of a Python test script [here](WU_test_upload.py).

- Run your code and check that your return code (r.status.code) is `200`, and that you receive a `success` response (r.text). If your response is something else, check your code and make sure that your have included the correct PWS ID and password in your request.

- If your code produces the correct responses, visit your PWS page on the Weather Underground website and verify that your data has been uploaded. Check that the values make sense for the relevant units.
![](images/image3.png)

- Once you're happy with your tests, integrate this code with the scripts running on your weather station. If you're using a Raspberry Pi Weather Station, a simple way to do this is to modify the [log_all_sensors.py](https://github.com/raspberrypi/weather-station/blob/master/log_all_sensors.py) code. If you've followed the [standard installation instructions](https://www.raspberrypi.org/learning/weather-station-guide/), this script should be run every five minutes via Cron, which is a sensible frequency for uploading to a site like Weather Underground.

--- hints ---
--- hint ---
If you get stuck, here is a basic example of a [modified log_all_sensors.py](https://github.com/raspberrypilearning/uploading-weather-data-to-weather-underground-v2/blob/master/en/resources/WU_test_upload.py) script.

--- /hint ---
--- /hints ---
