#!/usr/bin/python3

from gpiozero import Robot, DigitalInputDevice
from time import sleep

from gpiozero import CamJamKitRobot  # Import the CamJam GPIO Zero Library


class Encoder(object):
    def __init__(self, pin):
        self._value = 0
        self.encoder = DigitalInputDevice(pin)
        self.encoder.when_activated = self._increment
        self.encoder.when_deactivated = self._increment
    def reset(self):
        self._value = 0
    def _increment(self):
        self._value += 1
    @property
    def value(self):
        return self._value

robot = CamJamKitRobot()

e1 = Encoder(18)
e2 = Encoder(17)

m1_speed = 0
m2_speed = 0

SAMPLETIME = 1
TARGET = 90
KP = 0.006
KD = 0.001
KI = 0.0001

e1_prev_error = 0
e2_prev_error = 0

e1_sum_error = 0
e2_sum_error = 0


while True:
    e1_error = TARGET - e1.value
    e2_error = TARGET - e2.value

    m1_speed += e1_error * KP + (e1_prev_error * KD) + (e1_sum_error * KI)
    m2_speed += e2_error * KP + (e2_prev_error * KD) + (e2_sum_error * KI)
  
    m1_speed = max(min(1, m1_speed), 0)
    m2_speed = max(min(1, m2_speed), 0)

    robot.left_motor.forward(m1_speed)
    robot.right_motor.forward(m1_speed)
    print("e1 {} e2 {}".format(e1.value, e2.value))
    print("m1 {} m2 {}".format(m1_speed, m2_speed)) 

    e1.reset()
    e2.reset()

    e1_prev_error = e1_error
    e2_prev_error = e2_error

    e1_sum_error += e1_error
    e2_sum_error += e2_error

    sleep(SAMPLETIME)


