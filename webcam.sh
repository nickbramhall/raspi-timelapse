#! /bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 640x480 --no-banner /home/pi/Apps/timelapse/timelapse-stills/$DATE.jpg

cp -p /home/pi/Apps/timelapse/timelapse-stills/$DATE.jpg /home/pi/Apps/timelapse/app/static/images/latest.jpg