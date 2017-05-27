#!/usr/bin/env python

# Script to swap which workspace is on which monitor (output)
# Might not work as expected if at least one workspace is empty

import i3, os, subprocess
from pprint import pprint

def getActiveMonitor():
        #Find display monitor
        monitor = subprocess.check_output("xrandr -q | grep ' connected' | cut -d ' ' -f1", shell=True)
        if(monitor != ""):
            monitor = monitor.decode().split('\n')[0]
        return monitor

def getCurrentBrightness():
    #Find current brightness
    currB = subprocess.check_output("xrandr --verbose | grep -m 2 -i brightness | cut -f2 -d ' '", shell=True)
    if(currB != ""):
        currB = currB.decode().split('\n')[0]
        currB = int(float(currB) * 100)
    else:
        currB = ""
    return currB

def main():
    workspaces = i3.get_workspaces()
    workspace = [w['output'] for w in workspaces if w['focused'] is True][0]

    print(getCurrentBrightness())
    os.system( 'xrandr --output %s --brightness 1' %workspace)
if __name__ == '__main__':
    main()
