#coding=utf-8
import datetime
import json
import os
import sys
import time
import threading
from wave_share_43inch_epaper import *

GAP = 2

screen = Screen('/dev/ttyAMA0')
screen.connect()
time.sleep(GAP)
screen.handshake()

screen.clear()
screen.set_memory(MEM_SD)
screen.set_rotation(ROTATION_180)
screen.set_ch_font_size(FONT_SIZE_64)
screen.set_en_font_size(FONT_SIZE_64)

screen.bitmap(30, 240, "EKL.BMP")

screen.text(200,270,u"请插入网线")
screen.update()
time.sleep(GAP)
screen.disconnect()
time.sleep(GAP)



