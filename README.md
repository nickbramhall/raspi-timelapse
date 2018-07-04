##Introduction

This set of scripts captures a timelapse using a webcam connected to the Raspberry Pi. The timelapse is taken between dawn and dusk. After the timelapse images have been captured the timelapse is processed and a .mp4 movie file created.

##Setup

* Setup a Python  virtual environment using requirements.txt
* Install gstream using 'sudo apt-get install gstreamer1.0-tools'
* Connect a USB webcam to the Raspberry Pi
* Ensure all the scripts have appropriate permissions
* Add and configure a **settings.py** file for your location into the scripts folder
* Create a folder for storing webcam images

Add the following Cron jobs:

1 0 * * * /path/to/scripts/timelapse-setup.sh
55 23 * * * /path/to/scripts/timelapse-process.sh

##Explanation

###timelapse-setup.sh

The purpose of this script is to run the timelapse.py file from the Virtual Environment. The file is run using a Cron job just after midnight to allow for local dawn and dusk times to be calculated.

###timelapse.py

The purpose of this script is to start and stop the timelapse capture according to local dawn and dusk times calculated using the **astral** module for Python.

The script sleeps until dawn and at that point adds a Cron job to run the timelapse capture script (webcam.sh) every minute

The script then sleeps until dusk and at that point removes the timelapse capture job

At this point the script ends.

###webcam.sh

This script uses fswebcam to capture a still image from a USB webcam connected to the Raspberry Pi. The current datetime is appended to the jpeg filename.

###timelapse-process.sh

This script runs once all images for the day have been captured. It sorts the images by datetime and then renames them from 0000.jpg upwards.

With the images renamed, gst-launch-1.0 is then used to compile a 24fps mp4 movie file of the timelapse. This is done using the Pi's GPU.

The output file is saved locally with the datetime appended.

##Future Plans

* Start the processing of the timelapse immediately after the last image is captured
* Name the captured images 0000.jpg as they are captured
