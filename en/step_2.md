## What you will need

Weather Underground registration is only open to people 13 years and older. If you're under 13 years old you will need someone older to register on your behalf.

### Hardware

- A Raspberry Pi
- A Raspberry Pi Oracle Weather Station kit
*OR*
- An equivalent set of sub-set of sensors. For example you could use
 a Sense HAT, or a [Pimoroni Enviro pHAT](https://shop.pimoroni.com/products/enviro-phat){:target="_blank"}) which you can connect to the Pi

### Software

- The latest version of Raspbian
- The Python `requests` library. It can be installed by opening a terminal window and typing in:

```bash
sudo pip3 install requests
```


- The [Oracle Weather Station software](https://www.raspberrypi.org/learning/weather-station-guide/software.md){:target="_blank"}.
OR
- Any libraries you need to use your sensors' data. The latest version of Raspbian already includes the following software packages:
- Python 3
- Sense HAT for Python 3

If for any reason you need to install a package manually, follow these instructions:

[[[rpi-install-software]]]

Type this command into a terminal window to install the Sense HAT package:

```bash
sudo apt-get install sense-hat
```
