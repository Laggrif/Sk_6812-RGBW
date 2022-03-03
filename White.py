import time

from rpi_ws281x import *
from gpiozero import Button

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

B1 = Button(0)
B2 = Button(5)
B3 = Button(6)
B4 = Button(13)


def White(strip, color):
    for i in range(strip.numPixels() - 68):
        strip.setPixelColor(68+i, color)
    strip.show()

if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL,
                              LED_STRIP)
    strip.begin()

    hue = 255
    hue2 = 255

    White(strip, Color(hue2, hue2, hue2, hue))

    while True:
        White(strip, Color(0, 10, 30, 255))
