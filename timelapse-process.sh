#! /bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

cd /home/pi/Apps/timelapse/timelapse-stills

ls -1 -c -r | xargs rename 's/.*/our $i; sprintf("%04d.jpg", $i++)/e'

gst-launch-1.0 multifilesrc location=%04d.jpg index=1 caps="image/jpeg,framerate=24/1" ! jpegdec ! omxh264enc ! avimux ! filesink location=/home/pi/Apps/timelapse/timelapse-videos/timelapse_$DATE.avi

rm -rf /home/pi/Apps/timelapse/timelapse-stills/*

cp -p /home/pi/Apps/timelapse/timelapse-videos/timelapse_$DATE.avi /home/pi/Apps/timelapse/app/static/videos/latest.avi