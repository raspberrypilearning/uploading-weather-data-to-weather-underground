## Using Python to convert your data

You can see from the Weather Underground protocol that it requires some measurement data to be in different units to those collected natively by our Weather Station.

- Let's start with atmospheric pressure.  Our standard [Weather Station pressure sensor](https://github.com/raspberrypilearning/sensing-the-weather/blob/master/lesson-9/worksheet.md) records value in Pascals (Pa) and Weather Underground wants to receive this data in Inches. If you search for how to convert between the two units you may become confused as there are several different ways of using Inches in connection with pressure readings: pounds per square inch, inches of water, air and mercury. The last on in that list - inches of mercury - is the most common and that's the one Weather Underground wants. To convert from Pa to inches of mercury we need to multiply by 0.02953:

    ```Python
    def pa_to_inches(pressure_in_pa):
        pressure_in_inches_of_m = pressure_in_pa * 0.02953
        return pressure_in_inches_of_m

    ```


Another unit involving inches is the amount of rainfall measurement. Write a function in Python to convert a rainfall value from mm to inches.


--- hints ---
--- hint ---
You need to find out what conversion factor is required to mathematically convert mm to inches. You could estimate this simply by looking a ruler. For a more accurate answer, your could search online.  In this case you should find that 1 mm equals 0.0393701 inches.
--- /hint ---
--- hint ---
Given that conversion factor, you will need to multiply your rainfall value in millimeters by 0.0393701.
--- /hint ---
--- hint ---
Write this as a Python function:

    ```Python
    def mm_to_inches(rainfall_in_mm):
        rainfall_in_inches = rainfall_in_mm * 0.0393701
        return rainfall_in_inches

    ```
--- /hint ---
--- /hints ---

- The final conversion that you need to make is for the wind speeds. The [code used to process Weather Station kit anemometer readings](https://github.com/raspberrypilearning/sensing-the-weather/blob/master/lesson-2/worksheet.md) provides values in km/h whereas Weather Underground is expecting mph.

--- hints ---
--- hint ---
You need to find out what conversion factor is required to mathematically convert kilometers per hour to miles per hour.   In this case you should find that 1 khm equals 0.621371 mph.
--- /hint ---
--- hint ---
Given that conversion factor, you will need to multiply your wind speed value in khm by 0.0393701.
--- /hint ---
--- hint ---
Write this as a Python function:

    ```Python
    def khm_to_mph(speed_in_kmh):
        speed_in_mph = speed_in_kmh * 0.621371
        return speed_in_mph
        
    ```
--- /hint ---
--- /hints ---
