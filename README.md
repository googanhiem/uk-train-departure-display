![](assets/full-logo.png)

**A replica, near real-time, miniature UK railway station train departure sign based upon a Raspberry Pi Zero and 256x64 SPI OLED display(s). Uses the publicly available [OpenLDBWS API by National Rail Enquiries](https://www.nationalrail.co.uk/).**

This version is designed to work better on docker (without balena), though it only has support for one display. It requires more hands on editing to work, so you should be familiar with Docker and a little bit of python to use this.

***commands below do not work yet***

First run

`docker pull ghcr.io/googanhiem/uk-train-departure-display-docker:latest`

Then run (putting your updated config.py file in your home dir /train-sign/)

`docker run -v ~/train-sign/config.py:/src/config.py ghcr.io/googanhiem/uk-train-departure-display-docker:latest --restart=always redis`

The config should look like, this [config.py](/config.py) file - More details on getting a station code and API key below in the [configuration](/docs/04-configuration.md)

## Highlights
- **See local departures**: Display the depatures from your local station at home for up to date train information.
- **3D-printable cases**: Print your own miniature case to keep everything tidy - both desktop and 'hanging' style available.

![](assets/blog-header.jpg)
![](docs/images/completed-unit.jpg)

## How to build

**Check out [the documentation](/docs/01-getting-started.md) for full hardware/software requirements and complete build guide.**

- [Getting Started](/docs/01-getting-started.md)
- [Connecting the display to the Pi](/docs/02-connecting-the-display-to-the-pi.md)
- [Assembling the Case](/docs/03-assembling-the-case.md)
- [Configuration](/docs/04-configuration.md)

## Credits

[Chrisys](https://github.com/chrisys/train-departure-display) did a lot of this, I just took stuff out, ha.

A big thanks to [Chris Hutchinson](https://github.com/chrishutchinson/) who originally started this project and inspired me to develop it further. [Blake](https://github.com/ghostseven) made some further improvements and this project was forked from [there](https://github.com/ghostseven/UK-Train-Departure-Display).

The fonts used were painstakingly put together by `DanielHartUK` and can be found on GitHub at https://github.com/DanielHartUK/Dot-Matrix-Typeface - A huge thanks for making that resource available!

Thanks to [@jajasilver](https://github.com/jajsilver/UK-Train-Departure-Display-NRE) and [@MatthewAscough](https://github.com/MatthewAscough/UK-Train-Departure-Display-NRE) for forming the basis of the OpenLDBWS implementation.
