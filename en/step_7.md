## Using live data

- For testing and development, you used some fictitious data values, stored as variables in your code. Once you've tested your upload, you should delete these and use the code to process real data from your weather station.

![](images/image3.png)

- To perform regular uploads you could wrap your measuring and upload code in a loop. Alternatively you could have a one-shot script that is run at set intervals using Crontab.

[[[generic-python-while-true]]]

[[[nix-bash-crontab]]]

The Oracle Weather Station software uses the Crontab method to run a Python script called [log_all_sensors.py](https://github.com/raspberrypi/weather-station/blob/master/log_all_sensors.py) every 5 minutes. A simple way to modify your Weather Station so that it regularly uploads data to Weather Underground is to add the upload code you have written to this file.

If you've followed the [standard installation instructions](https://www.raspberrypi.org/learning/weather-station-guide/), this script should be run every five minutes via Cron, which is a sensible frequency for uploading to a site like Weather Underground.
(WU_test_upload.py).

--- hints ---
--- hint ---
If you get stuck, here is a basic example of a [modified log_all_sensors.py](https://github.com/raspberrypilearning/uploading-weather-data-to-weather-underground-v2/blob/master/en/resources/WU_test_upload.py) script.

--- /hint ---
--- /hints ---
