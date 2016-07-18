#!/usr/bin/env python
# coding: utf-8

import json
import os
import time

import Adafruit_DHT

h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
result = {'temp': int(t), 'humidity': int(h), 'update': int(time.time())}

fmt = "{temp}-{humidity}%"

print fmt.format(**result)