## Introduction

There are loads of ways to collect weather data with a raspberry Pi: you can collect humidity, temperature and pressure data with a SenseHat, connect a UV light sensor to your GPIO pins or even build a complete [Weather Station](https://www.raspberrypi.org/education/weather-station/) like the kits we recently sent to lucky schools around the world.

Once you're collecting data, it's great to plot graphs and look at how your local climate is changing over time. You can also contribute your data to an online community like Weather Underground.

Weather Underground has a global community of people supplying data from weather stations and air quality monitors to provide hyperlocal data and forecasting. Many types of popular consumer weather stations can be used with Weather Underground and the code for the Oracle Raspberry Pi school kit can also be modified to stream data in the same way.

The instructions in this  project are based around our Weather Station kit but you should be able to adapt the process to upload whatever data you are collecting.

*If you are using one of our Weather Station kits or have designed your own version, this guide assumes that you have already built and installed your it. If you have not done that yet, follow [these instructions](https://www.raspberrypi.org/learning/weather-station-guide/) and then come back here when you've finished!*

The steps in this guide assume that you will be regularly uploading data to Weather Underground. If you have limited bandwidth or poor connectivity between your station and the Internet then you might want to consider data a configuration that sends data every 15 minutes. The Weather Underground website will not display any data older than 20 minutes so batch uploads of data are only really useful for historical storage. If you have one of out school Weather Station kits and frequent uploads cause problems then you should probably use the Oracle database as described in the standard software build guide.

### What you will make

You'll use the Python requests library to upload data from your weather sensors to Weather Underground where you can monitor and analyse your measurements.

![](images/image4.png)

You can then use the Weather Underground widgets to display a weather summary on your own website.

(<a href="http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=IESHER4"><img src="http://banners.wunderground.com/cgi-bin/banner/ban/wxBanner?bannertype=pws250_both&weatherstationcount=IESHER4" width="250" height="150" border="0" alt="Weather Underground PWS IESHER4" /></a>)

Or:

()<object width="290" height="130"><param name="movie" value="http://www.wunderground.com/swf/pws_mini_rf_nc.swf?station=IESHER4&freq=&units=english&lang=EN" /><embed src="http://www.wunderground.com/swf/pws_mini_rf_nc.swf?station=IESHER4&freq=&units=english&lang=EN" type="application/x-shockwave-flash" width="290" height="130" /></object>)
