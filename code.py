# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Sophie
#Apr 11
#
# Move a servo with a potentiometer in sync

import time
import board
import pwmio
import servo
from analogio import AnalogIn

# create a PWMOut object on Pin 16.
# pwm: Pulse-width module
# pwm is a measure of elapsed time between the leading and trailing edges of a single pulse of energy
pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)

# sets pot pin to pin 26/A0
potentionmeter = AnalogIn(board.GP26) 

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm, min_pulse = 650, max_pulse = 2500)

while True:
    print((potentionmeter.value))
    potentiometer_value = potentionmeter.value
    print(potentiometer_value)

    # changing range to 1-180
    angle = potentiometer_value * (180/65535)

    #changes value of servo angle
    my_servo.angle = angle
    time.sleep(1)