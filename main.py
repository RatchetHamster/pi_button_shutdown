#!/usr/bin/env python3

from gpiozero import Button
from signal import pause
import os

BUTTON_PIN = 23
LONG_PRESS_TIME = 2.0  # seconds

button = Button(
    BUTTON_PIN,
    pull_up=True,
    hold_time=LONG_PRESS_TIME,
    hold_repeat=False
)

def short_press():
    print("Short press detected: rebooting")
    os.system("sudo reboot -h now")

def long_press():
    print("Long press detected: shutting down")
    os.system("sudo shutdown -h now")

button.when_pressed = None          # not used
button.when_released = short_press  # fires only if not held
button.when_held = long_press

print("Button monitor started (gpiozero)")
pause()
