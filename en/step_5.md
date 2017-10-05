## Using Python to convert your data

The Weather Underground protocol requires some measurement data to be in different units to those collected by the Raspberry Pi Oracle Weather Station or the SenseHat library functions.

Let's start with atmospheric pressure.

[[[generic-theory-what-is-pressure]]]

The Oracle [Weather Station pressure sensor](https://www.raspberrypi.org/learning/sensing-the-weather/lesson-9/worksheet/) records value in Hectopascals (hPa), and Weather Underground wants to receive this data in inches. If you search for how to convert between the two units, it is easy to become confused, as there are several different ways of using inches in connection with pressure readings: pounds per square inch, inches of water, air, and mercury. The last one in that list, **inches of mercury**, is the most common and that's the one Weather Underground wants.

If you are using the SenseHat, your pressure data will be in millibars which fortunately are equivalent to hPa.

Let's define a Python function to perform the conversion.

- Open a new Python file with Idle (or your favourite Python IDE) and save it into `/home/pi` as `WU-upload.py`.

- Create a function called `hpa_to_inches` that takes the data `pressure_in_hpa` as an argument.

[[[generic-python-simple-functions]]]

- To convert from hPa to inches of mercury, we need to multiply by 0.02953 and return the result.

    ```python
    def hpa_to_inches(pressure_in_hpa):
        pressure_in_inches_of_m = pressure_in_hpa * 0.02953
        return pressure_in_inches_of_m

    ```
- Test the function by adding the line below. This is not part of the function declaration so make sure you don't indent it.

    ```python
    print(hpa_to_inches(100))
    ```

- Now run your code. It should display the answer: 2.9530000000003. That's a lot of decimal places! We'll deal with that later.

Another unit involving inches is the amount of rainfall measurement. Write and test a function in Python to convert a rainfall value from mm to inches.

--- hints ---
--- hint ---
- You need to find out what conversion factor is required to convert mm to inches. You could estimate this simply by looking a ruler. For a more accurate answer, you could search online.
--- /hint ---
--- hint ---
- You should find that 1 millimetre equals 0.0393701 inches. Given that conversion factor, you will need to multiply your rainfall value in mm by 0.0393701.
--- /hint ---
--- hint ---
- Write this as a Python function:
```python
def mm_to_inches(rainfall_in_mm):
    rainfall_in_inches = rainfall_in_mm * 0.0393701
    return rainfall_in_inches
```
--- /hint ---
--- /hints ---

- SenseHat and Oracle Weather Station temperature sensors report their readings in Celsius so they need to be converted to Fahrenheit.
Create a function called `degc_to_degf` that takes the data `temperature_in_c` as an argument and returns the result in Fahrenheit.

--- hints ---
--- hint ---
- You need to find out what conversion factor is required to convert Celsius to Fahrenheit.
--- /hint ---
--- hint ---
- This formula is trickier than a simple multiplication. You need to multiply by 9/5 *and then* add 32.
--- /hint ---
--- hint ---
```python
def degc_to_degf(temperature_in_c):
    temperature_in_f = (temperature_in_c * (9/5.0)) + 32
    return temperature_in_f
```
    --- /hint ---
    --- /hints ---   


- A final conversion that you might need to make is for wind speeds. The code used to [process Weather Station kit anemometer readings](https://www.raspberrypi.org/learning/sensing-the-weather/lesson-2/worksheet/) provides values in km/h, whereas Weather Underground is expecting mph.

--- hints ---
--- hint ---
- You need to look up what conversion factor is required to convert kilometers per hour to miles per hour.
--- /hint ---
--- hint ---
- You should find that 1 km/h equals 0.621371 mph. Given that conversion factor, you will need to multiply your wind speed value in km/h by 0.621371.
--- /hint ---
--- hint ---
- Write this as a Python function:
    ```python
    def kmh_to_mph(speed_in_kmh):
        speed_in_mph = speed_in_kmh * 0.621371
        return speed_in_mph    
    ```
--- /hint ---
--- /hints ---
Before you move on to the next stage, make sure you have added all the conversion functions for your weather data to `WU-upload.py`.
