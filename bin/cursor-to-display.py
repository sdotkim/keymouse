#!/usr/bin/env python3

import re
import subprocess
import sys

# Identify displays
def displaySort(e) :
    return e[4]

d = []
displaysRaw = [s for s in subprocess.check_output("xrandr --listmonitors | sed 1,1d | awk '{print $3}'", shell=True).decode("utf-8").split()]
for iii in range(len(displaysRaw)) :
    d.append([int(x) for x in re.split('x|\\+|\\/', displaysRaw[iii])])
d.sort(key=displaySort)


# Set direction, default: right
direction = 1
if sys.argv[1:] :
    direction = int(sys.argv[1])
if direction != 1 and direction != -1 :
    quit()

# Probe current cursor X position
cursor = int(subprocess.check_output(["xdotool getmouselocation --shell |head -n 1| awk -F '=' '{print $2}'"], shell=True, universal_newlines=True))


# Determine new coordinates on the Screen    
for jjj in range(len(d)) :
    if d[jjj][4] <= cursor <= d[jjj][4] + d[jjj][0] :
        kkk = jjj + direction
        if 0 <= kkk <= len(d) - 1 :
            subprocess.Popen([
                "xdotool", 
                "mousemove", 
                str(round(d[kkk][4] + d[kkk][0]/2)),
                str(round(d[kkk][5] + d[kkk][2]/2))
        ])
            
