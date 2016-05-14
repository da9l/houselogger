#!/usr/bin/python

import logging
import logging.handlers
import rrdtool
import temp_sensor
import time
import sys


# this script should take a number of parameters so it can be called from a mosquitto client
# with values. These values should be written to the rrd database
# Do all values have to be written at the same time?

def do_update():
  timestamp = time.time()
#  internal = temp_sensor.TempSensor("28-000005303678")
#  external = temp_sensor.TempSensor("28-000005604c61")
#  heater = temp_sensor.TempSensor("28-000005610c53")
# in case of error, retry after 5 seconds
  for retry in (5, 1):
    try:
      rrdtool.update("/opt/templog/data/templog.rrd",
                     "%d:%s:%s:%s" % (timestamp,
                                     internal.get_temperature(),
                                     external.get_temperature(),
                                     heater.get_temperature()))
      return
    except:
      logging.exception("retry in %is because of: ", retry)
      time.sleep(retry * 1000)

# set up logging to syslog to avoid output being captured by cron
syslog = logging.handlers.SysLogHandler(address="/dev/log")
syslog.setFormatter(logging.Formatter("templogger: %(levelname)s %(message)s"))
logging.getLogger().addHandler(syslog)

do_update()
