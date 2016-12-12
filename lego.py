from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_D, LargeMotor, MediumMotor
from ev3dev.auto import INPUT_1, INPUT_2, ColorSensor, UltrasonicSensor
import time
import ev3dev.auto as auto
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
import ev3dev.core as core


#ultrasonicSensor = UltrasonicSensor(INPUT_1)
colorSensor = ColorSensor(INPUT_2)
clawMotor = MediumMotor(OUTPUT_B)
leftTire = LargeMotor(OUTPUT_A)# and LargeMotor(OUTPUT_D)
rightTire = LargeMotor(OUTPUT_D)
ir = InfraredSensor()

uss = core.UltrasonicSensor(INPUT_1)



#def getUltrasonic():
#    ultrasonicSensor.mode='US-DIS-CM'
#    return ultrasonicSensor.units
#
# def getColor():
#     colorSensor.mode='COL-REFLECT'
#     return colorSensor.value()
#
#
# #def findObject():
# while getUltrasonic > 5.5:

leftTire.run_timed(speed_sp=360, time_sp=600)
rightTire.run_timed(speed_sp=360, time_sp=600)
time.sleep(1)
if uss.distance_centimeters != 0:
    ev3.Sound.speak('Welcome to the E V 3 dev project!').wait()
#colorSensor.

#ev3.Sound.speak("Hello Ali")

#leftTire.run_timed(speed_sp = 360, time_sp = 600)
#rightTire.run_timed(speed_sp = 360, time_sp = 600)
#time.sleep(1)
#leftTire.run_timed(speed_sp = 360, time_sp = 600) and rightTire.run_timed(speed_sp = 360, time_sp = 600)
#rightTire.run_timed(speed_sp = 360, time_sp = 600)
#time.sleep(1)
#leftTire.run_timed(speed_sp = 360, time_sp = 600) and rightTire.run_timed(speed_sp = 360, time_sp = 600)
#rightTire.run_timed(speed_sp = 360, time_sp = 600)
#time.sleep(1)

clawMotor.run_timed(speed_sp = 720, time_sp = 500)
time.sleep(1)

leftTire.run_timed(speed_sp = 360, time_sp = 600) and rightTire.run_timed(speed_sp = 360, time_sp = 600)
rightTire.run_timed(speed_sp = 360, time_sp = 600)
time.sleep(1)
leftTire.run_timed(speed_sp = 360, time_sp = 600) and rightTire.run_timed(speed_sp = 360, time_sp = 600)
rightTire.run_timed(speed_sp = 360, time_sp = 600)
time.sleep(1)
leftTire.run_timed(speed_sp = 360, time_sp = 600) and rightTire.run_timed(speed_sp = 360, time_sp = 600)
rightTire.run_timed(speed_sp = 360, time_sp = 600)
time.sleep(1)

clawMotor.run_timed(speed_sp = -720, time_sp = 500)
time.sleep(1)

leftTire.run_timed(speed_sp = -360, time_sp = 600) and rightTire.run_timed(speed_sp = 360, time_sp = 600)
#rightTire.run_timed(speed_sp = -360, time_sp = 600)
time.sleep(1)
leftTire.run_timed(speed_sp = -360, time_sp = 600) and rightTire.run_timed(speed_sp = 360, time_sp = 600)
#rightTire.run_timed(speed_sp = -360, time_sp = 600)
time.sleep(1)

leftTire.run_timed(speed_sp = -360, time_sp = 1500)
time.sleep(1)

leftTire.run_timed(speed_sp = 360, time_sp = 600)
#rightTire.run_timed(speed_sp = 360, time_sp = 600)
time.sleep(1)

#def findTarget():
# while getColor > 15:
#     leftTire.run_timed(power=15, rotations=0.2)
#     rightTire.run_timed(power=15, rotations=0.2)
#     time.sleep(1)
# clawMotor.run_timed(power=75, rotations=-0.8)
# time.sleep(1)


