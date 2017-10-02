## What you will need

- Weather Underground registration is only open to people 13 years and older. If you're under 13 years old you will need someone older to register on your behalf.

- Some weather data.

### Hardware

- A Raspberry Pi
- A Raspberry Pi Oracle Weather Station kit
_OR_
- An equivalent set or sub-set of sensors. For example you could use
 a Sense HAT, or a [Pimoroni Enviro pHAT](https://shop.pimoroni.com/products/enviro-phat){:target="_blank"} which you can connect to the Pi

[[[rpi-sensehat-temperature]]]

[[[rpi-sensehat-pressure]]]

[[[rpi-sensehat-humidity]]]

### Software

- The latest version of Raspbian
- The Python `requests` library. It can be installed by opening a terminal window and typing:

    ```bash
    sudo pip3 install requests

    ```
 
- The [Oracle Weather Station software](https://www.raspberrypi.org/learning/weather-station-guide/software.md){:target="_blank"}.
_OR_
- Any libraries you need to use your sensors' data. The latest version of Raspbian already includes the following software packages:
- Python 3
- Sense HAT for Python 3

If for any reason you need to install a package manually, follow these instructions:

[[[rpi-install-software]]]
