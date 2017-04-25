#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3dev.auto import *
import time

mA = ev3.MediumMotor('outA')
mA.reset()
while(True):
    print(mA.position)
    time.sleep(0.5)
