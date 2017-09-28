## The Weather Underground upload protocol

The method for uploading data to Weather Underground uses the standard HTTP protocol to send data.  Whenever you type a URL into the address bar or click a link on a web page, your browser software will send an HTTP request, called a **get** request, to a web server asking for the page you want to see. Normally the page retrieved will be made of HTML and CSS code.  Things are a little different when HTTP requests are use to upload data.

- Take a look at this example:

https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?ID=XXXXX&PASSWORD=YYYYYYY&dateutc=now&humidity=59&action=updateraw

- If you were to copy and paste it into your browser, you should just see a line of unformatted text complaining that the password and key were incorrect because we have not supplied valid credentials.

Let's break down the fields in the URL.

| Field | Analysis |
|-------|----------|
| https:// | Protocol |
| weatherstation.wunderground.com  | web server DNS name |
| /weatherstation/ | website directory path |
| updateweatherstation.php? | PHP command |
| ID=XXXXX| Weather Station ID |
| & | field separator |
| PASSWORD=YYYYYYY | Weather Underground Password |
| & | field separator |
| dateutc=now | Date/time the measurement was made|
| & | field separator |
| humidity=59 | A weather measurement, in this case, the Humidity reading |
| & | field separator |
| action=updateraw | Tells the server what kind of data to expect |
|||


All these parameters are needed to make a valid request. If they are not included, then the upload will fail. You don't have to include the humidity reading but you must send at least one item of weather measurement data.

If you wanted to add more readings, a temperature value for example,  simply add that into the URL, making sure you use the `&` symbol to keep it separate from the other parameters.

Obviously you have to know what the name of the parameter will be: in our example the 'humidity' was not too tricky to work out. But our weather station has two temperature sensors, one for air temperature and one for soil/ground. Fortunately, most providers of services like this will [publish the details](http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol){:target="_blank"} you need. You can see from the Weather Underground protocol that we'd need to use 'tempf' and 'soiltempf' as our parameter names. It's also important to note that Weather Underground expects these readings to be supplied in Fahrenheit, so you'll need to covert Celsius values before you upload them.

In fact, some of the other parameters use different units too:

| Name | Units | Sensor |
|-----|:----:|------|
| winddir| degrees | wind direction|
|windspeed| *mph* | wind speed|
|windgust| *mph* | Wind gust speed|
|rainin| *inches* | Rainfall|
|baromin| *inches* | Pressure|
|||

- Make a list of the data collected by your sensors, and use the protocol specifications to see if you need to perform any conversions before uploading your data.
