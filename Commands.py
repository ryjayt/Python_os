from multiprocessing.connection import wait
import os
import time
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

def help(pram):
    match pram:
        case ['echo']:
            print('Echo')
        case _:
            print('Help Menue')