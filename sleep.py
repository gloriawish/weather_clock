import time
from wave_share_43inch_epaper import *
screen = Screen('/dev/ttyAMA0')
screen.connect()
screen.handshake()
screen.clear()
screen.update()
time.sleep(.3)
screen.sleep()
time.sleep(.3)
