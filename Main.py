from asyncio.windows_events import NULL
from distutils.cmd import Command
import os

from Commands import color 

# loading os
print('loading os')
import Commands
from configparser import ConfigParser
settings = 'config.ini'
config = ConfigParser()
config.read(settings)
print('config.ini loaded')
running = 1
os.system('cls||clear')
#main os funtionsecho
print("Python OS")
print("Beta v0.1\nOpen Source Edition\n==================\n\n")
while running == 1:
    temp = str(input(">")).split()
    match temp:
        case ['echo']:
            print("\n\x1b[37;41mNeed's prams\x1b[0m\n\u001b[38;5;242m>echo lol\nlol\n\x1b[0m")
        case ['echo', *pram]:
            Commands.echo(pram)
        case ["color", "fg"]:
            Commands.color()
        case ["color", "bg"]:
            Commands.colorB()
        case ["color", "test"]:
            Commands.color()
            Commands.colorB()
        case ["color","test","loop"]:
            i = 1
            while i == 1:
                Commands.color()
                Commands.colorB()
        case ['Clear']:
            os.system('cls||clear')
        case ['help']:
            Commands.help('')
        case ['help', *pram]:
            Commands.help(pram)

        case _:
            print("\033[37;41mNo Command or file with that name\033[0m")