# #!/usr/bin/env python3

import numpy as np
import math
import time
from PIL import Image
import subprocess as subp


# (x-5)**2 + (y-5)**2 == 3**2
def point_on_circle(x,y,x2,y2,r):
    v = r**2 - 1 == (x-x2)**2 + (y-y2)**2
    v = v or r**2 + 1 == (x-x2)**2 + (y-y2)**2
    return v

#d = sqrt (x-x1)**2 + (y-y1)**2
def distance(x,y,x2,y2):
    return math.sqrt((x-x2)**2 + (y-y2)**2)

def draw_circle(arr,r,margin=3,center=[0,0]):
    if center == [0,0]:
        center=[arr.shape[0]//2,arr.shape[1]//2]
    x2,y2 = center
    x,y = arr.shape[0:2]
    for j in range(x):
        for k in range(y):
            if abs(round(distance(j, k, x2, y2)) -r) <= margin:
                arr[j,k]=[255,255,255]
    return arr

def draw_percentage(arr,r,percentage,margin=3, center=None):
    if center == None:
        center=[arr.shape[0]//2,arr.shape[1]//2]
    def f(x,r,x2,y2):
        return math.sqrt((x-x2)**2+r**2) + y2

def gen_lin(percentage):
    if percentage > 50:
        a = round(percentage/100*360)
        def f(x):
            if x<=0:
                return None
            return math.tan(a)*x
        return f
    elif percentage == 50:
        def f(x):
            if x<=0:
                return None
            else:
                return False
    elif percentage < 50:
        a = round(percentage/100*360)
        def f(x):
            if x >=0:
                return False
            return math.tan(a)*x


def gen_symbol(per):
    arr = np.zeros((50,100)).astype(np.uint8)
    arr[:,:per]=255
    arr[:10,-10:]=255
    arr[-10:,-10:]=255
    arr[0,:] = 0
    arr[-1,:]=0
    arr[1,:]=255
    arr[-2,:]=255
    arr[2,:]=0
    arr[-3,:]=0
    return arr.astype(np.uint8)

def get_power():
    cmd = 'upower -i /org/freedesktop/UPower/devices/DisplayDevice | grep percentage'
    o = subp.run(cmd,shell=True,text=True, capture_output=True)
    o = o.stdout
    o = list(o)
    loc = o.index('%')
    per = o[loc-2:loc]
    per=''.join(per)
    try:
        per=int(per)
    except:
        subp.run('dunstify battery simbol needs help in get_per!',shell=True)

    return per

per = 70
per = get_power()
arr = gen_symbol(per)
img = Image.fromarray(arr)
img.save('/home/trollroy/.config/custom_run_scripts/battery-symbol/bat.png')
