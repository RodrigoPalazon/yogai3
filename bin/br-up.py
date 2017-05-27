#!/usr/bin/env python

# Script to swap which workspace is on which monitor (output)
# Might not work as expected if at least one workspace is empty

import i3, os, subprocess
from pprint import pprint

def main():
    workspaces = i3.get_workspaces()
    workspace = [w['output'] for w in workspaces if w['focused'] is True][0]
    os.system( 'xrandr --output %s --brightness 1' %workspace)
if __name__ == '__main__':
    main()
