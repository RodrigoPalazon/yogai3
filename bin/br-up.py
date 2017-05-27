#!/usr/bin/env python

# Script to swap which workspace is on which monitor (output)
# Might not work as expected if at least one workspace is empty

import i3, subprocess

def main():
	#get all workspaces and find the focused monitor
    workspaces = i3.get_workspaces()
    workspace = [w['output'] for w in workspaces if w['focused'] is True][0]
    # get current brightness of focused monitor
    output = subprocess.check_output("xrandr --verbose | awk '/%s/{f=1}/Brightness:/ && f{print $2; exit}'" %workspace, shell=True)
    #issue command to change brightness
    newBrightnessValue = float(output)+0.2
    setBrightness = 'xrandr --output %s --brightness %s' %(workspace, newBrightnessValue)
    process = subprocess.Popen(setBrightness, shell=True, stdout=subprocess.PIPE)

if __name__ == '__main__':
    main()
