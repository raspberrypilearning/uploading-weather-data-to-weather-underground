## Using Python to convert your data

The Weather Underground protocol requires some measurement data to be in different units to those collected natively by our Raspberry Pi Weather Station.

Let's start with atmospheric pressure. Our standard [Weather Station pressure sensor](https://www.raspberrypi.org/learning/sensing-the-weather/lesson-9/worksheet/) records value in Pascals (Pa), and Weather Underground wants to receive this data in inches. If you search for how to convert between the two units, you may become confused, as there are several different ways of using inches in connection with pressure readings: pounds per square inch, inches of water, air, and mercury. The last one in that list, inches of mercury, is the most common and that's the one Weather Underground wants.

Let's define a Python function to perform the conversion. Open a new Python file with Idle (or your favourite Python IDE) and save it into /home/pi as WU-upload.py.

[[[generic-python-simple-functions]]]

- To convert from Pa to inches of mercury, we need to multiply by 0.02953:

    ```python
    def pa_to_inches(pressure_in_pa):
        pressure_in_inches_of_m = pressure_in_pa * 0.02953
        return pressure_in_inches_of_m

    ```
- Test the function by adding the line:

    ```python
    print(pa_to_inches(100))
    ```

- Now run your code. It should display the answer: 2.953

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

- The final conversion that you need to make is for the wind speeds. The code used to [process Weather Station kit anemometer readings](https://www.raspberrypi.org/learning/sensing-the-weather/lesson-2/worksheet/) provides values in km/h, whereas Weather Underground is expecting mph.

--- hints ---
--- hint ---
- You need to look up what conversion factor is required to convert kilometers per hour to miles per hour.
--- /hint ---
--- hint ---
- You should find that 1 km/h equals 0.621371 mph. Given that conversion factor, you will need to multiply your wind speed value in km/h by 0.0393701.
--- /hint ---
--- hint ---
- Write this as a Python function:
    ```python
    def khm_to_mph(speed_in_kmh):
        speed_in_mph = speed_in_kmh * 0.621371
        return speed_in_mph    
    ```
--- /hint ---
--- /hints ---
