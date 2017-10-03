## Uploading data to Weather Underground

To upload data to Weather Underground  you are going to use the standard HTTP protocol. This is what your web browser uses to fetch a web page whenever you're surfing the web.  Whenever you type a URL into the address bar or click a link on a web page, your browser will send an HTTP **GET** request to the web server asking for the page you want. Normally the page retrieved will be made of HTML and CSS code.  

Things are a little different when HTTP requests are used to upload data.

- Take a look at this example of sending data to Weather Underground:

https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?ID=XXXXX&PASSWORD=YYYYYYY&dateutc=now&humidity=59&action=updateraw

- If you copy and paste it into the address bar of your browser and try to visit this URL, you will just see a line of unformatted text complaining that the password and key were incorrect. This is an error message sent by the server because you have not supplied valid credentials: you would need to replace XXXXX and YYYYYYY with your Id and password.

Look closely at the URL and you'll see it contains a set of parameters separated by `&` symbols.

| Field | What it represents |
|-------|----------|
| https:// | Protocol |
| weatherstation.wunderground.com  | web server DNS name |
| /weatherstation/ | website directory path |
| updateweatherstation.php? | PHP command |
| ID=XXXXX| Weather Station ID |
| PASSWORD=YYYYYYY | Weather Underground Password |
| dateutc=now | Date/time the measurement was made|
| humidity=59 | A weather measurement, in this case, the Humidity reading |
| action=updateraw | Tells the server what kind of data to expect |
|||


All these parameters are needed. If they are omitted, then the upload will fail. You have to include at least one item of weather measurement data, but it doesn't have to be the humidity reading.

To upload readings for additional sensors - a temperature value for example - simply append that into the URL, making sure you use the `&` symbol to keep it separate from the other parameters.

Obviously you have to know what Weather Underground calls this measurement. In our example, `humidity` was not too tricky to work out. But the Oracle weather station has two temperature sensors, one for air temperature and one for soil/ground. What parameters should you use?

Fortunately, most providers of services like this will [publish the details](http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol){:target="_blank"} you need. You can see that we'd need to use `tempf` and `soiltempf` as our parameter names. It's also important to note that Weather Underground expects these readings to be supplied in Fahrenheit, so you may need to covert Celsius values before you upload them.

In fact, some of the other parameters use different units too:

| Name | Units | Sensor |
|-----|:----:|------|
|winddir| degrees | wind direction|
|windspeed| *mph* | wind speed|
|windgust| *mph* | Wind gust speed|
|rainin| *inches* | Rainfall|
|baromin| *inches* | Pressure|
|||

- Make a list of the data collected by your sensors, and use the information above to see if you need to perform any conversions before uploading your data. If your weather station has other sensors not covered here, you can refer to the protocol specification to see if they are accepted by Weather Underground.
