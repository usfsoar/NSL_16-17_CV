'''
* ErrorIndicator is used to alert errors via LED's
*
* Only initialization errors considered
*
* Not much can be done on an error a mile in the air
'''

import RPi.GPIO as GPIO


class ErrorIndicator:
    LEDPINS = [17, 27, 22, 18]  # [Red1, Red2, Red3, Green4]

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for pin in self.LEDPINS:
            GPIO.setup(pin, GPIO.OUT)

    def _turn_led(self, led_num, on):  # 0 =< led_num =< 3
        if on:
            GPIO.output(self.LEDPINS[led_num], GPIO.HIGH)
        else:
            GPIO.output(self.LEDPINS[led_num], GPIO.LOW)

    def message(self, binary_order):
        i = 0
        for b in binary_order:
            self._turn_led(i, b)
            i += 1