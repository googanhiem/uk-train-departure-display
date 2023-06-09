![](assets/full-logo.png)

**A replica, near real-time, miniature UK railway station train departure sign based upon a Raspberry Pi Zero and 256x64 SPI OLED display(s). Uses the publicly available [OpenLDBWS API by National Rail Enquiries](https://www.nationalrail.co.uk/).**

This version worked better on docker (sans balena), only support one display. Edit the src/config.py with your api code and station info.

***commands below do not work yet***

First run

`docker pull ghcr.io/googanhiem/uk-train-departure-display-docker:latest`

Then run (putting your updated config.py file in your home dir /train-sign/)

`docker run -v ~/train-sign/config.py:/src/config.py ghcr.io/googanhiem/uk-train-departure-display-docker:latest --restart=always redis`


## Highlights

- **See local departures**: Display the depatures from your local station at home for up to date train information.
- **3D-printable cases**: Print your own miniature case to keep everything tidy - both desktop and 'hanging' style available.
- **Dual display support**: Run two displays each showing departures from different platforms from a single Raspberry Pi.

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
