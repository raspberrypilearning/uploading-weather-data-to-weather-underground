## Introduction

There are lots of ways to collect weather data with a Raspberry Pi: you could for example collect humidity, temperature, and pressure data with a Sense HAT, connect a UV light sensor to your GPIO pins, or even build a complete [Weather Station](https://www.raspberrypi.org/education/weather-station/) like the kits we recently sent to lucky schools around the world.

Once you're collecting data, you can start creating graphs to look at how your local climate is changing over time. You can also contribute your data to an online community like [Weather Underground](https://www.wunderground.com/).

Weather Underground brings together a global community of people who uploaded weather and air quality data. This data is displayed on the Weather Underground website, and can be used by other people, for example for forecasting. Many types of popular consumer weather stations can be used with Weather Underground, and the code for the Oracle Raspberry Pi school kit can also be modified to stream data in this way.

The instructions in this project are based around our Weather Station kit, but you should be able to adapt the process to upload whatever data you are collecting. As long as you're able to store your readings in a Python variable, you will be fine.  

Note: If you are using one of our Weather Station kits, or have designed your own version, this guide assumes that you have already built and installed it. If you have not done that yet, follow [these instructions](https://www.raspberrypi.org/learning/weather-station-guide/), and then come back here when you've finished!

The steps in this guide assume that you will be continuously uploading data to Weather Underground. If you have limited bandwidth or poor connectivity between your station and the internet, then you might want to consider a configuration that sends data every 15 minutes. The Weather Underground website will not display any data older than 20 minutes, so batch uploads of data are only really useful for historical storage. If you have one of out school Weather Station kits and frequent uploads cause problems, then you should probably use the Oracle database as described in the standard software build guide.

### What you will make

You'll use the Python `requests` library to upload data from your weather sensors to the Weather Underground website, where you will be able to monitor and analyse your measurements.

![](images/image4.png)

You can then use the Weather Underground widgets to display a weather summary on your own website.

(<a href="http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=IESHER4"><img src="http://banners.wunderground.com/cgi-bin/banner/ban/wxBanner?bannertype=pws250_both&weatherstationcount=IESHER4" width="250" height="150" border="0" alt="Weather Underground PWS IESHER4" /></a>)
