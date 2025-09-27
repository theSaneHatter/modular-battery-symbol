#!/usr/bin/env python3

import subprocess as subp
import time
import os

proc = subp.Popen(['/usr/bin/python3', '/home/trollroy/.config/custom_run_scripts/battery-symbol/main.py'])
#needs to be long enough for the genorator to run i think
time.sleep(5)

