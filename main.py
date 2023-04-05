import random
import os
import ast
from AddtoInv import addtoInv
import getch
import roombuilder
from pyfiglet import Figlet
from weapon import weapon
import time
from monster import mnster, dice
os.system('clear')
chars = '_@*'
noMon = True
startchar = 3
def player_info():
    name = input("Enter username: ")
    fileName = ("Player" + name + "Inf" + ".txt")
    print(fileName)
    try:
        userInf = open(fileName, "r+")
    except:
        userInf = open(fileName, "a")
    else:
        userInf = open(fileName, "r+")
    fSize = os.path.getsize(fileName)
    if fSize != 0:
        dictInf = ast.literal_eval(userInf.read())
        print(dictInf)
    elif fSize == 0:
        dictInf = ({"level":1,
                    "inv":[""],
                    "curses":[""],
                    "exp":0,
                    "x":0,
                    "y":0,
                    "floor":0,
                    "room":0,
                    "HealthMax":1,
                    "healthCurrent":1,
                    "Dead":False,
                    'Speed':10})


    xpToNext = (float(dictInf["level"]) * 8) - dictInf["exp"]

    def xpcalc():
        nonlocal xpToNext
        if int(xpToNext) == 0:
            dictInf["level"] = dictInf["level"] + 1
            xpToNext = (float(dictInf["level"]) * 8) - dictInf["exp"]
            print("You leveled up! EXP to next: " + str(xpToNext)) 
        xpToNext = (float(dictInf["level"]) * 8) - dictInf["exp"]

    xpcalc()
    fScene = False

    print(str(xpToNext))

    def moveloop():
        global noMon
        starting()
        os.system('clear')
        roombuilder.room["y" + str(dictInf["y"])][dictInf["x"]] = '@'
        roombuilder.placemon('h',7)
        for item in roombuilder.room:
                print(roombuilder.room[item])
        while not dictInf["Dead"]:
            char = getch.getch()
            dictInf['Speed'] = dictInf['floor'] * 1.25
            dictInf['Speed'] = round(dictInf['Speed'])
            os.system('clear')
            

            if char == "w":
                if dictInf["y"] > 1:
                    roombuilder.room["y" + str(dictInf["y"])][dictInf["x"]] = '_'
                    dictInf["y"] -= 1
                    roombuilder.room["y" + str(dictInf["y"])][dictInf["x"]] = '@'

            elif char == "s":
                if dictInf["y"] < len(roombuilder.room):
                  roombuilder.room["y" + str(dictInf["y"])][dictInf["x"]] = '_'
                  dictInf["y"] += 1
                  roombuilder.room["y" + str(dictInf["y"])][dictInf["x"]] = '@'

            elif char == "a":
                if dictInf["x"] > 0:
                    roombuilder.room["y" + str(dictInf["y"])][dictInf["x"]] = '_'
                    dictInf["x"] -= 1
                    roombuilder.room["y" + str(dictInf["y"])][dictInf["x"]] = '@'

            elif char == "d":
                if dictInf["x"] < len(roombuilder.room["y" + str(dictInf["y"])])-1:
                    roombuilder.room["y" + str(dictInf["y"])][dictInf["x"]] = '_'
                    dictInf["x"] += 1
                    roombuilder.room["y" + str(dictInf["y"])][dictInf["x"]] = '@'
                    
            elif char == "-":
                break    
            
            for item in roombuilder.room:
                print(roombuilder.room[item])
            
            if roombuilder.threeroom['y'+str(dictInf['y'])][dictInf['x']] != '_':
                fight = mnster(roombuilder.threeroom['y'+str(dictInf['y'])][dictInf['x']],dictInf['level'])
                os.system('clear')
                print(Figlet(font='standard').renderText(' Entering Combat!'))
                time.sleep(0.5)
                os.system('clear')
                selSlot = 1
                sel = ''
                inInv = False
                print(sel)
                while dictInf['Dead'] == False:
                    inp = getch.getch()
                    os.system('clear')
                    if inp == 'd':
                        if selSlot < 3:
                            selSlot = selSlot + 1
                    if inp == 'a':
                        if selSlot -1 > 0:
                            selSlot = selSlot - 1
                    if inp == '-':
                        break
                    if selSlot == 1:
                        inInv = False
                        sel =  """
 ________    ___   ______
|* Attack|  |Inv| |Defend|
 --------    ---   ------
                        """
                    elif selSlot == 2:
                        inInv = True
                        sel =  """
 ________    ___   ______
| Attack|  |* Inv| |Defend|
 --------    ---   ------
                        """
                    elif selSlot == 3:
                        inInv = False
                        sel =  """
 ________    ___   ______
| Attack|  |Inv| |* Defend|
 --------    ---   ------
                        """
                    if inp == ' ':
                        if selSlot == 2:
                            print('Inv')
                        if selSlot == 1:
                            print("attack")
                        if selSlot == 3:
                            print('Defend')
                    print(sel)
                    print(selSlot)

                            
       
        print("Player Dead")
    def starting():
        dictInf["y"] = len(roombuilder.room)
        dictInf["x"] = len(roombuilder.room["y" + str(dictInf["y"])]) // 2

    def combat(m):
        monster = roombuilder.fullname(m)
        

    moveloop()

    dictInf["x"] = 2
    dictInf["y"] = 2
    userInf.seek(0)
    userInf.writelines(str(dictInf))
    userInf.close()



print(Figlet(font='standard').renderText('BASH-ful Dungeon'))
print('---------------------------------------------')
print('|      Type 1 to start, type 2 to end       |')
print('---------------------------------------------')

def starting():
    startchar = getch.getch()
    if startchar == '1':
        player_info()
    elif startchar == '2':
        print("Stopping BASH-FUL")
    else:
        starting()
starting()


#roombuilder.room["y" + str(3)][dictInf["x"]] = goblin(1,1)