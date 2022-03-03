import time

from rpi_ws281x import *
import sys

# LED strip configuration:
import Strandtest

LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_RGBW
#LED_STRIP      = ws.SK6812W_STRIP


def Show(strip, color):
    for i in range(strip.numPixels() - 68):
        strip.setPixelColor(68+i, color)
    strip.show()

def Decoder(str,  progressive = False):
    colors = []
    c = ""
    string = str
    alpha = 255
    for i in range(len(string)):
        if string[0] != ",":
            c += string[0]
        elif string[0] == ",":
            colors.append(c)
            c = ""
        string = string[1:]
    colors.append(c)
    if len(colors) == 5:
        alpha = int(colors[4])
    if (len(colors) > 5) or (len(colors) < 4):
        print("error")
        print(len(colors))
        return
    LED_BRIGHTNESS = alpha
    try:
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    except:
        print("aie")
    strip.begin()
    """
    if progressive:
        for i in range(255, 0, -1):
            Show(strip, Color(int(int(colors[1]) / i), int(int(colors[0]) / i), int(int(colors[2]) / i), int(int(colors[3]) / i)))
            time.sleep(i/3000)
    else:
        Show(strip, Color(int(colors[1]), int(colors[0]), int(colors[2]), int(colors[3])))
    """
    Show(strip, Color(int(colors[1]), int(colors[0]), int(colors[2]), int(colors[3])))
    # TODO remove after making progressive light
    return Color(int(colors[1]), int(colors[0]), int(colors[2]), int(colors[3]))


if __name__ == '__main__':
    #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    #strip.begin()
    if len(sys.argv) > 1:

        if len(sys.argv) == 3:
            alpha = sys.argv[2]
        else:
            alpha = "255"

        arg1 = sys.argv[1]
        programs = ["rb", "th"]

        try:
            arg1 = int(sys.argv[1])
        except:
            pass

        if arg1 in programs:
            strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, int(alpha), LED_CHANNEL, LED_STRIP)
            strip.begin()
            if arg1 == programs[0]:
                while True:
                    Strandtest.rainbow(strip)
            if arg1 == programs[1]:
                while True:
                    Strandtest.theaterChaseRainbow(strip)
        else:
            if arg1 == 0 or arg1 == "d":
                arg1 = "0,0,0,0"
            elif arg1 == 1:
                arg1 = "0,0,0,1"
            elif arg1 == 2:
                arg1 = "1,0,0,0"
            elif arg1 == 3:
                arg1 = "0,0,40,255"
            elif arg1 == "r":
                arg1 = "255,0,0,0"
            elif arg1 == "g":
                arg1 = "0,255,0,0"
            elif arg1 == "b":
                arg1 = "0,0,255,0"
            elif arg1 == "w":
                arg1 = "0,0,40,255"

            else:
                sys.exit(f"Bad input, input was \"{sys.argv[1]}\"")
            Decoder(arg1 + "," + alpha, True)

        print(arg1 + "," + alpha)

    else:
        r=0
        g=0
        b=0
        w=0

        while True:
            i = input("")
            if i == "exit":
                sys.exit("Successfully Shut down")
            try:
                #r = input("r")
                #Show(strip, Color(g, r, b ,w))
                #g = int(input("g"))
                #Show(strip, Color(g, r, b ,w))
                #b = int(input("b"))
                #Show(strip, Color(g, r, b ,w))
                #w = int(input("w"))
                #Show(strip, Color(g, r, b ,w))
                Decoder(i)
            except:
                print("bad input")