print('loading Moduals')
from asyncio.windows_events import NULL
from distutils.cmd import Command
import os
import Commands
import options
from configparser import ConfigParser
from Commands import color 
import Logo

# loading os
os.system('cls||clear')
print('loading os')
settings = 'config.ini'
config = ConfigParser()
config.read(settings)
print('config.ini loaded')
running = 1
if config['Systerm Settings']['AutoUpdate'] == 'on':
    print("checking for updates")
    Commands.update()
if config['Systerm Settings']['DebugMode'] == 'on':
    print('Debug mode is\033[32m on\033[0m')
    pause = input('Press Enter to continue')
os.system('cls||clear')
#main os funtionsecho
Logo.logo()
os.system('cls||clear')
print("Python OS")
version = config['Systerm info']['version']
print('Beta '+ version +'\n==================\n\n')
while running == 1:
    temp = str(input(">")).split()
    match temp:
        case ['echo']:
            print("\n\x1b[37;41mNeed's prams\x1b[0m\n\u001b[38;5;242m>echo lol\nlol\n\x1b[0m")
        case ['echo', *pram]:
            Commands.echo(pram)
        case ["colour", "fg"]:
            Commands.color()
        case ["colour", "bg"]:
            Commands.colorB()
        case ["colour", "test"]:
            Commands.color()
            Commands.colorB()
        case ["colour","test","loop"]:
            i = 1
            while i == 1:
                Commands.color()
                Commands.colorB()
        case ['clear']:
            os.system('cls||clear')
        case ['cls']:
            os.system('cls||clear')
        case ['help']:
            Commands.help('')
        case ['help', *pram]:
            Commands.help(pram)
        case ['shutdown']:
            running = 0
        case ['start', *pram]:
            Commands.start(pram)
        case ['settings']:
            options.options()
        case ['crash']:
            Commands.crash('Test')
        case _:
            print("\033[37;41mNo Command or file with that name\033[0m")