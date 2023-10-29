# Imports
import time
from adafruit_circuitplayground import cp
import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
# from adafruit_hid.keycode import Keycode

# Setup for bluetooth HID Service
hid = HIDService()
device_info = DeviceInfoService(software_revision=adafruit_ble.__version__,
                                manufacturer="Adafruit Industries")

# Setup Bluetooth advertisement
advertisement = ProvideServicesAdvertisement(hid)
advertisement.appearance = 961
scan_response = Advertisement()
scan_response.complete_name = "Right Glove"

# Make Bluetooth radio object
ble = adafruit_ble.BLERadio()

# Disconnect pre connected things so we can connnect with what we want
if ble.connected:
    for c in ble.connections:
        c.disconnect()

# Start advertising
ble.start_advertising(advertisement, scan_response)

# Initialize the keyboard   
k = Keyboard(hid.devices)
kl = KeyboardLayoutUS(k)

# TODO
# Initialize the mouse

# Bluetooth Loop
while True:
    
    i = 0
    cp.pixels.brightness = 0.05
    while not ble.connected:
        # Blue circle loop, showing waiting for connection
        time.sleep(.05)
        cp.pixels[i] = ((0, 0, 255))
        cp.pixels[i-1 % 10] = ((0, 0, 204))
        cp.pixels[i-2 % 10] = ((0, 0, 153))
        cp.pixels[i-3 % 10] = ((0, 0, 102))
        cp.pixels[i-4 % 10] = ((0, 0, 51))
        cp.pixels[i-5 % 10] = ((0, 0, 0))
        i += 1
        i %= 10
    cp.pixels.fill((0, 100, 0))
    time.sleep(1)
    cp.pixels.fill((0, 255, 0))
    time.sleep(1)
    cp.pixels.fill((0, 0, 0))
    
    #
    while ble.connected:
        # TODO Write some code to use the accelerometer to control keyboard input. 
        pass
i = 0
while True:
    print(i)
    i += 1
    time.sleep(1)