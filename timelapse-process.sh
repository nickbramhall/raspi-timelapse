#! /bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

cd /home/pi/webcam

ls -1 -c -r | xargs rename 's/.*/our $i; sprintf("%04d.jpg", $i++)/e'

gst-launch-1.0 multifilesrc location=%04d.jpg index=1 caps="image/jpeg,framerate=24/1" ! jpegdec ! omxh264enc ! avimux ! filesink location=timelapse_$DATE.mp4