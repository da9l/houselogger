 #!/bin/bash
#
# update .rrd database with CPU temperature
#
# $Id: update_cputemp 275 2013-05-16 05:20:56Z lenik $

#cd /home/lenik

# create database if not exists
[ -f cputemp.rrd ] || {
rrdtool create /opt/templog/data/templog.rrd --start now --step 60   \
DS:internal:GAUGE:600:-55:125  \
DS:external:GAUGE:600:-55:125  \
DS:heat:GAUGE:600:-55:125  \
DS:picpu:600:0:125 \
DS:internalHumidity:GAUGE:600:0:100 \
RRA:AVERAGE:0.5:1:576    \
RRA:AVERAGE:0.5:3:1344   \
RRA:AVERAGE:0.5:12:1488  \
RRA:AVERAGE:0.5:72:1984  \
RRA:MIN:0.5:72:1984      \
RRA:MAX:0.5:72:1984
}

