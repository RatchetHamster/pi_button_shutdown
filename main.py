#!/usr/bin/env python3

from gpiozero import Button
from signal import pause
import os

button = Button(23, pull_up=True, hold_time=2, hold_repeat=False)

def short_press():
    os.system("sudo reboot -h now")

def long_press():
    os.system("sudo shutdown -h now")

button.when_pressed = None          # not used
button.when_released = short_press  # fires only if not held
button.when_held = long_press
pause()

