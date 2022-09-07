from multiprocessing.connection import wait
import os
import time
from configparser import ConfigParser
from typing import Type
settings = 'config.ini'
config = ConfigParser()
config.read(settings)

def options():
    if config['Systerm Settings']['AutoUpdate'] == 'on':
        print('1 Auto update = \x1b[32mon\x1b[0m')
    else:
        print('1 Auto update = \x1b[31moff\x1b[0m')