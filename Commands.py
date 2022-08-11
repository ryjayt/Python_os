from multiprocessing.connection import wait
import os
import time
from configparser import ConfigParser
settings = 'config.ini'
config = ConfigParser()
config.read(settings)
def echo(Pram): #echo commadn
    strpram = ""
    for i in Pram:
        strpram = strpram + i + " "

    print(str(strpram))

def color(): # color command
    import sys
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print (u"\u001b[0m")

def colorB(): # background Collor command
    import sys
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
        print (u"\u001b[0m")

def help(pram): #help command
    match pram:
        case['colour']: #help colour
            print('Colour has 3 options \033[37;44mtest\033[0m, \033[32mFG\033[0m, \033[42mBG\033[0m\n test dose both BG and FG at the same time.to use the command\n>colour [pram]')
        case ['echo']: #help echo
            print('Echo prints evrything in the pram\n>Echo [pram]\n[pram]\n')
        case ['clear']: #help clear
            print('clear will \033[31mremove\033[0m evrything from the \033[32mTerminal\033[0m to clean it up\nTo use the command\n>clear')
        case ['all']: #list all commands
            print('All Commands\n------------\nBasic\n---\necho\nclear\ncolour')#basic
        case _: #Help Main
            print('Help Menue\n-----------\nPyrhon os is a simple pythos program made by\nfor more infomation on a command you can use the wiki \x1b[45mryjayt\x1b[0m\nTo use help command\n>help [pram]')

def update(): # update cheker and downloader
    if config['Systerm info']['version'] == str("0.0.2"):
        print('up to date')
    else:
        print('Needs updating')