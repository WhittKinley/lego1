from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_D, LargeMotor, MediumMotor
from ev3dev.auto import INPUT_1, INPUT_2, ColorSensor, UltrasonicSensor
import time
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *

ultrasonicSensor = UltrasonicSensor(INPUT_1)
colorSensor = ColorSensor(INPUT_2)
clawMotor = MediumMotor(OUTPUT_B)
leftTire = LargeMotor(OUTPUT_A)# and LargeMotor(OUTPUT_D)
rightTire = LargeMotor(OUTPUT_D)

ir = ev3.InfraredSensor()
ir.set_prox_mode() # proximity mode
ir.get_distance() # for prox mode
ir.set_remote_mode() # for using the remote control
ir.get_remote_command() # get remote control command
ir.set_seek_mode() # follow remote control when button pressed
ir.get_all_direction_and_distance #  for seek mode
ir.get_direction_and_distance(chan) #  for seek mode
if (ir.get_distance() == 1):
    ev3.Sound.speak('Welcome to the E V 3 dev project!').wait()

while True:
    ev3.Leds.set_color(ev3.Leds.LEFT, (ev3.Leds.GREEN, ev3.Leds.RED)[ir.value()])

def getUltrasonic():
    ultrasonicSensor.mode='US-DIS-CM'
    return ultrasonicSensor.units
#
# def getColor():
#     colorSensor.mode='COL-REFLECT'
#     return colorSensor.value()
#
#
# #def findObject():
# while getUltrasonic > 5.5:

if(ultrasonicSensor.distance_centimeters(1)):
    leftTire.run_timed(speed_sp=360, time_sp=600)
    rightTire.run_timed(speed_sp=360, time_sp=600)
    time.sleep(1)
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


