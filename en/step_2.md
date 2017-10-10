## What you will need

--- collapse ---
---
title: Notes for Raspberry Pi Oracle Weather Station schools
---

If you are using one of our Oracle Weather Station kits, or have designed your own version, this guide assumes that you have already built and installed it. If you have not done that yet, follow [these instructions](https://www.raspberrypi.org/learning/weather-station-guide/), and then come back here when you've finished!

This guide assumes that you will be continuously uploading data to Weather Underground. You can do this **and** continue to upload data to the Oracle database. If you have limited bandwidth or poor connectivity between your station and the internet, then you might want to consider a configuration that sends data every 15 minutes. The Weather Underground website will not display any data older than 20 minutes, so batch uploads of data are only really useful for historical storage. If you have one of out school Weather Station kits and frequent uploads cause problems, then you should probably stick to only using the Oracle database as described in the standard software build guide.

--- /collapse ---


### Hardware

- A Raspberry Pi
- A Raspberry Pi Oracle Weather Station kit
_OR_
- An equivalent set or sub-set of sensors you can connect to the Pi, for example a [Sense HAT](https://www.raspberrypi.org/products/sense-hat/) or a [Pimoroni Enviro pHAT](https://shop.pimoroni.com/products/enviro-phat){:target="_blank"}


### Software

- The latest version of Raspbian
- Python 3

    ```bash
    sudo apt-get install python3

    ```
- The Python requests library, which can be installed by opening a terminal window and typing:

    ```bash
    sudo pip3 install requests

    ```

- The [Oracle Weather Station software](https://www.raspberrypi.org/learning/weather-station-guide/software.md){:target="_blank"}.
_OR_
- Any libraries you need to use your sensors' data. The latest version of Raspbian already includes the following software packages:

- Sense HAT for Python 3

If for any reason you need to install a package manually, follow these instructions:

[[[rpi-install-software]]]

### Additional notes

- Weather Underground registration is only open to people 13 years and older. If you're under 13 years old, you will need someone older to register on your behalf.
