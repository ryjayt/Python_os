
from cgi import test
from ntpath import join
import os

fileObj = open("Apps\Hello World.txt", "r")
arrwords = fileObj.read().splitlines()
fileObj.close()
fileObj = open("Apps\Hello World.txt", "r")
arrundo = fileObj.read().splitlines()
fileObj.close()
strname = " "
intnum = 0
intsave = int(0)
print("python editor v1.1\ntype help for help menue")
print("-----------------\n")


def funread(strname, arrwords, intnum):
    intnum = 0
    for i in arrwords:  # prints text file
        intnum += 1
        strname = str(intnum) + " " + i
        print(strname)


x = 0
while x == 0:
    funread(strname, arrwords, intnum)
    stredit = str(input("> ")).split()
    match stredit:    
        
        case ['add', '>', 'r']: #add at the end repetivly
            y = 1
            os.system('cls||clear')  
            while y == 1:
                print('Type stop to stop')
                funread(strname, arrwords, intnum)
                stredit = str(input("> ")).split()
                match stredit:
                    case ['stop']:
                        y = 0
                    case [*text]:
                        tex =" ".join([str(item) for item in text])
                        arrwords.append(tex)
                        os.system('cls||clear')                  

        case ['add','>', line, *text]:  #add at pasific line
            tex =" ".join([str(item) for item in text])
            if line.isdigit() == True:
                arrwords.insert(int(line) - 1, tex)
            else:
                arrwords.append(tex)
            intsave = 1
            
        case ['add', *text]: # add
            tex =" ".join([str(item) for item in text])
            arrwords.append(tex)

        case ["save"]:  #save
            print("Writing to document do not stop program")
            fileobj = open("Apps\Hello World.txt", "r+")
            fileobj.truncate(0)
            fileobj.close
            with open("Apps\Hello World.txt", "w") as filwrite:
                for i in arrwords:  # prints text file
                    filwrite.write(i + "\n")
                    print(i)
            filwrite.close
            print("done")
            intsave = 0

        case ['remove', 'all']:
            arrwords = []
            intsave = 1

        case ['remove','>', *line]: # remove
            a = 0
            for i in line:
                if i.isdigit() == True:
                    if int(i)-1 < len(arrwords):
                        arrwords.pop(int(i) - 1 - a)
                        a + 1
                    else:
                        print('Cant not remove ' + str(i) + ' dose not exist')
                else:
                    print(str(i) + ' is not a number')

        case ['remove']:
            arrwords.pop()

        case ['clear']: # clear 
            os.system('cls||clear')
        case ['cls']:
            os.system('cls||clear')

        case ['undo']: # undo
            arrwords = []
            for i in arrundo:
                arrwords.insert(len(arrwords), i)

        case ['exit']: # exit
            if intsave == 1:
                stredit = (
                    input("you still save unsaved edits\nare you sure (y/n) > "))
                if stredit == "y":
                    print("exit with out saving")
                    x = 1
                else:
                    print("Did not exit")
                    x = 0
            else:
                print("Exit")

        case ['help']:
            print('\n\x1b[32mhelp menue\x1b[0m')
            print('> mean optinal settings by puting in a > \n * a pramiter that needed even if you dont add a >')
            print('add > line *text\nadd > r \nadd *text \nremove > line \nremove all \nremove \nclear \nundo \nsave \nExit')

        case ['about']:
            print('\nUsed to be known as Kempy editor, was rewitten for python os 0.2.0')
