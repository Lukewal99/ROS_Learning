#!/usr/bin/python3

import termios
import serial
import time

path = '/dev/ttyUSB0'

# Disable reset after hangup
with open(path) as f:
    attrs = termios.tcgetattr(f)
    attrs[2] = attrs[2] & ~termios.HUPCL
    termios.tcsetattr(f, termios.TCSAFLUSH, attrs)

ser = serial.Serial(path, 115200)

while True:
  time.sleep(1)

ser.close()

# etc.
