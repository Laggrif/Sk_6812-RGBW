from rpi_ws281x import *
import RPi.GPIO as GPIO
import time

# LED strip configuration:
LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_RGBW
#LED_STRIP      = ws.SK6812W_STRIP

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN)

def Show(strip, color):
    for i in range(10):
        strip.setPixelColor(i, color)
        strip.show()

def Change(old):
    new = GPIO.input(23)
    if new != old:
        changed = True
    else:
        changed = False
    return changed, new



if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()

    old = GPIO.input(23)
    change = []

    while True:
        change = Change(old)
        old = change[1]
        if change[1] and change[0] == 1:
            Show(strip, Color(0,0,0,0))
        elif change[1] and change[0] == 0:
            Show(strip, Color(0,0,30,255))
        print(change[0], change[1], GPIO.input(23))
        time.sleep(1)
