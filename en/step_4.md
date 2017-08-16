## The Weather Underground upload protocol

The method for uploading data to Weather Underground uses the standard http protocol to send data. You'll probably be familiar with the format of http requests from using a web browser to visit web sites. Whenever you type a URL into the address bar  or click a link on a web page, your browser software will send an http request - called a *get* request -  to the webs server asking for the page you want to see. Normally the page retrieved will be made of [html and css](https://www.raspberrypi.org/learning/coder-html-css-lessons/).  Things are a little different when http requests are use to upload data, as with Weather Underground.

Take a look at this example:

[https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?ID=XXXXX&PASSWORD=YYYYYYY&dateutc=now&humidity=59&action=updateraw](https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?ID=XXXXX&PASSWORD=YYYYYYY&dateutc=now&humidity=59&action=updateraw)

If you clink on this link or copy and paste it into your browser, you should just see a line of unformatted text complaining that the password and key were incorrect. Let's break down the fields in the URL.

| Field | Analysis |
|-------|----------|
| https:// | Protocol |
| weatherstation.wunderground.com  | webserver DNS name |
| /weatherstation/ | website directory path |
| updateweatherstation.php? | PHP command |
| ID=XXXXX| 1st parameter |
| & | field separator |
| PASSWORD=YYYYYYY | 2nd parameter |
| & | field separator |
| dateutc=now | 3rd parameter |
| & | field separator |
| humidity=59 | 5th parameter |
| & | field separator |
| action=updateraw | final parameter |
|||


The first 2 fields look like a normal request for a webpage where the server's address and location on the directory tree are specified. Then we have the PHP command: PHP is a hugely populars open source general-purpose scripting language that is especially suited for web development and can be embedded into HTML. WeatherUnderground use PHP to handle the upload process. The rest of the URL consists of various parameters separated by an & symbol. You can see that first of all there is the ID of the weather station and password needed to add new records. These parameters are compulsory and must be part of any request to upload to Weather Underground.  Then there are the actual weather values themselves, in this case the time of the measurement and a single humidity reading. Finally there is the 'action' parameter - also compulsory -  which tells the server what sort of data to expect.

If we wanted to add more readings, a temperature value for example, we would simply add that into the URL, making sure we use the **&** symbol to keep it separate from the other parameters.

Obviously you have to know what the name of the parameter will be: in our example the 'humidity' was not too tricky to work out. But our weather station has two temperature sensors, one for air temperature and one for soil/ground. Fortunately, most providers of services like this will [publish the details](http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol) you need. You can see from the Weather Underground protocol that we'd need to use *tempf* and *soiltempf*. It's also important to note that  Weather Underground expects these readings to be supplied in Fahrenheit, so you'll need to covert our Celsius values before we upload them.

In fact some of the other parameters use different units too:

| Name | Units | Sensor |
|-----|:----:|------|
| winddir| degrees | wind direction|
|windspeed| *mph* | wind speed|
|windgust| *mph* | Wind gust speed|
|rainin| *inches* | Rainfall|
|baromin| *inches* | Pressure|
|||

Make a list of the data collected by your sensors and use the protocol specifications to see if you need to perform any conversions before uploading your data.
