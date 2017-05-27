#!/usr/bin/env python

# Script to swap which workspace is on which monitor (output)
# Might not work as expected if at least one workspace is empty

import i3, subprocess

def main():
	#get all workspaces and find the focused monitor
    workspaces = i3.get_workspaces()
    workspace = [w['output'] for w in workspaces if w['focused'] is True][0]
    #issue command to change brightness
    setBrightness = 'xrandr --output %s --brightness %s' %(workspace, 1)
    process = subprocess.Popen(setBrightness, shell=True, stdout=subprocess.PIPE)

if __name__ == '__main__':
    main()
