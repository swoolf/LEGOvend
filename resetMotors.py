#!/usr/bin/env python3
import ev3dev.ev3 as ev3

mA = ev3.MediumMotor('outA')
mB = ev3.MediumMotor('outB')
mA.reset()
mB.reset()

