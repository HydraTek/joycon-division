
# Setup
from adafruit_circuitplayground import cp
import time
import random
# import math
import board
# import busio as io
import digitalio
# import adafruit_ht16k33.segments
from adafruit_hid.mouse import Mouse
import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
# from hid_gamepad import Gamepad

# Fancy Start up LEDs
cp.pixels.brightness = .01
for y in range(2):
    for x in range(10):
        time.sleep(0.1)
        cp.pixels[x % 10] = (255, 0, 0)
        cp.pixels[(x + 1) % 10] = (255, 128, 0)
        cp.pixels[(x + 2) % 10] = (255, 255, 0)
        cp.pixels[(x + 3) % 10] = (128, 255, 0)
        cp.pixels[(x + 4) % 10] = (0, 255, 0)
        cp.pixels[(x + 5) % 10] = (0, 255, 128)
        cp.pixels[(x + 6) % 10] = (0, 255, 255)
        cp.pixels[(x + 7) % 10] = (0, 128, 255)
        cp.pixels[(x + 8) % 10] = (0, 0, 255)
        cp.pixels[(x + 9) % 10] = (128, 0, 128)
cp.pixels.fill((0, 0, 0))

# Setup for bluetooth HID Service
hid = HIDService()
device_info = DeviceInfoService(
    software_revision=adafruit_ble.__version__, manufacturer="Adafruit Industries")

# Setup Bluetooth Advertisement
advertisement = ProvideServicesAdvertisement(hid)
advertisement.appearance = 961
scan_response = Advertisement()
scan_response.complete_name = "Right Glove"

# Make Bluetooth radio object
ble = adafruit_ble.BLERadio()
ble.name = 'Right Glove'

# Disconnect preconnected things so we can connect with what we want
if ble.connected:
    for c in ble.connections:
        c.disconnect()

# Start advertising
ble.start_advertising(advertisement, scan_response)

# Initialize Keyboard
k = Keyboard(hid.devices)
Kl = KeyboardLayoutUS(k)

# Initialize Mouse
mouse = Mouse(hid.devices)

# Making the button array
# The pins we are using
keypress_pins = [board.A6, board.A4, board.A5, board.A1]
# Array of button variables
key_pin_array = []
# Set the keys to something
keys_pressed = [Keycode.A, Keycode.B, Keycode.C, Keycode.D]
control_key = Keycode.SHIFT

# Initialize the button variable array key_pin_array
for pin in keypress_pins:
    key_pin = digitalio.DigitalInOut(pin)
    key_pin.direction = digitalio.Direction.INPUT
    key_pin.pull = digitalio.Pull.UP
    key_pin_array.append(key_pin)

while True:
    # Blueloop while waiting to bluetooth connect
    i = 0
    cp.pixels.fill((0, 0, 0))
    while not ble.connected:
        time.sleep(.05)
        cp.pixels[i] = ((0, 0, 255))
        cp.pixels[i-1 % 10] = ((0, 0, 204))
        cp.pixels[i-2 % 10] = ((0, 0, 153))
        cp.pixels[i-3 % 10] = ((0, 0, 102))
        cp.pixels[i-4 % 10] = ((0, 0, 51))
        cp.pixels[i-5 % 10] = ((0, 0, 0))
        i += 1
        i %= 10
    time.sleep(0.25)
    cp.pixels.brightness = 0.1
    for i in range(0, 220):
        cp.pixels.fill((0, 255 - i, 0))
        time.sleep(0.01)
    cp.pixels.fill((0, 0, 0))
    cp.pixels.brightness = .01

    
    # connected loop 
    val = [1, 2, 3]
    loops = 0
    while ble.connected:
        # Blinky light to indicate that we are in a loop
        if not loops % 2000:
            cp.pixels.fill(val)
            val = [random.randint(1, 255), 
                   random.randint(1, 255), 
                   random.randint(1, 255)]
            
        # Get accelerometer data NOT IN USE
        # ax, ay, az = cp.acceleration
        
        # Print accelerometer data every 100th loop
        # if not loops % 100:
        #    print("X acc = {:0.3}\nY acc = {:0.3}\nZ acc = {:0.3}".format(ax, ay, az))
        
        # Check if a button is pressed
        for key_pin in key_pin_array:
            if not key_pin.value:
                i = key_pin_array.index(key_pin)
                # Index finger is left click instead of a button press
                if i == 0: 
                    mouse.click(Mouse.LEFT_BUTTON)
                else:
                    key = keys_pressed[i]
                    k.press(key)
                    k.release_all()
        
        # sensitivity = 10
        # mouse movement NOT IN USE
        # mouse.move(math.floor(-ax / 9.8 * sensitivity), 
        #            math.floor(ay / 9.8 * sensitivity))
        loops += 1
   
    ble.stop_advertising()    
    ble.start_advertising(advertisement)
    time.sleep(2)