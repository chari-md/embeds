# firmware: https://micropython.org/download/ESP32_GENERIC_S3/
# docs: https://docs.micropython.org/en/latest/esp32/quickref.html

from machine import Pin, Timer

led = Pin(2, Pin.OUT)
tim = Timer()


def tick(timer):
    global led
    led.toggle()


tim.init(period=1000, mode=Timer.PERIODIC, callback=tick)
