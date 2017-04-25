#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3dev.auto import *
import time

def onTweet(mL,mR, sensor,home):
    mL.run_forever(speed_sp=-100)
    mR.run_forever(speed_sp=100)
    while(sensor.value()< 3):
#        if (motor.position < -590):
#            motor.run_timed(time_sp=500, speed_sp=500)
#            time.sleep(0.5)
#            motor.run_forever(speed_sp=-100)
        time.sleep(.01)
    mL.run_to_abs_pos(position_sp=home, speed_sp=700)
    mR.run_forever(speed_sp=-700)
    while (mL.position < home): time.sleep(.1)
    mR.stop()

if __name__ == '__main__':
    try:
        mA = ev3.MediumMotor('outA')
        mB = ev3.MediumMotor('outB')
        mB.reset()
        mA.reset()
        home=mA.position-40

        cs=ColorSensor()
        for i in range(25):
            onTweet(mA,mB,cs,home)
            print(i)
    except KeyboardInterrupt:
        mA.reset()
        mB.reset()
        print('exit')
