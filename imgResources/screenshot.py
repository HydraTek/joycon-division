from PIL import ImageGrab
from time import sleep
savepath = 'imgSrc/'   
inc = 0

try:
    while True:
        health = ImageGrab.grab(bbox=(570,990,660,1050))
        health.save(savepath + 'health' + str(inc) + '.jpg')
        ammo = ImageGrab.grab(bbox=(1205,990,1290,1040)) 
        ammo.save(savepath + 'ammo' + str(inc) + '.jpg')
        inc += 1
        sleep(1)
except KeyboardInterrupt:
    print('Took ' + str(2 * inc) + 'screenshots')