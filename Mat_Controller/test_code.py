"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.03
time_on = 0.17
while True:
    led[0] = (255, 0, 0)
    time.sleep(time_on)

    led[0] = (0, 255, 0)
    time.sleep(time_on)

    led[0] = (0, 0, 255)
    time.sleep(time_on)

    led[0] = (255, 0, 0)
    time.sleep(time_on)

    led[0] = (255, 255, 0)
    time.sleep(time_on)
    led[0] = (0, 0, 0)

    time.sleep(3 * time_on)

    led[0] = (255, 0, 0)
    time.sleep(time_on)

    led[0] = (0, 255, 0)
    time.sleep(time_on)

    led[0] = (0, 0, 255)
    time.sleep(time_on)

    led[0] = (255, 0, 0)
    time.sleep(time_on)

    led[0] = (255, 255, 0)
    time.sleep(time_on)

    led[0] = (255, 0, 0)
    time.sleep(time_on)

    led[0] = (0, 255, 0)
    time.sleep(time_on)

    led[0] = (0, 0, 255)
    time.sleep(time_on)

    led[0] = (255, 0, 0)
    time.sleep(time_on)

    led[0] = (255, 255, 0)
    time.sleep(time_on)

    led[0] = (255, 0, 0)
    time.sleep(time_on)

    led[0] = (0, 0, 255)
    time.sleep(time_on)

    led[0] = (0, 255, 0)
    time.sleep(time_on)
    led[0] = (0, 0, 0)

    time.sleep(3 * time_on)
