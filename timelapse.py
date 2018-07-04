import datetime
import pytz
from time import sleep
from astral import Astral, Location
from crontab import CronTab
import settings

a = Astral()

###

#Raspberry Pi timelapse tutorial: https://www.raspberrypi.org/forums/viewtopic.php?t=72435
#Python-Crontab: http://stackabuse.com/scheduling-jobs-with-python-crontab/

### Define Location

l = Location()
l.name = settings.NAME
l.region = settings.REGION
l.latitude = settings.LATITUDE
l.longitude = settings.LONGITUDE
l.timezone = settings.TIMEZONE
l.elevation = settings.ELEVATION
l.sun()

utc=pytz.UTC

### Configure Cron

cron = CronTab(user='pi')  

sun = l.sun(date=datetime.date.today(), local=True)
#sun = l.sun(date=datetime.date(2018, 7, 4), local=True)
#print('Dawn:    %s' % str(sun['dawn']))
#print('Sunrise: %s' % str(sun['sunrise']))
#print('Noon:    %s' % str(sun['noon']))
#print('Sunset:  %s' % str(sun['sunset']))
#print('Dusk:    %s' % str(sun['dusk']))

### At dawn start the timelapse

dawn = sun['dawn']  # Gets the time of dusk in local time

now = datetime.datetime.now()
now = utc.localize(now)

time_difference = dawn - now
time_difference_in_seconds = time_difference.total_seconds()

sleep(time_difference_in_seconds)

job = cron.new(command='./webcam.sh')  # Add a new Cron job to start taking timelapse photos every minute
job.minute.every(1)

cron.write()

### At dusk end the timelapse

dusk = sun['dusk'] # Gets the time of dusk in local time

now = datetime.datetime.now()
now = utc.localize(now)

time_difference = dusk - now
time_difference_in_seconds = time_difference.total_seconds()

sleep(time_difference_in_seconds)

cron.remove(job) # Remove the Cron job to stop taking timelapse photos

### Process the timelapse

# Timelapse finished