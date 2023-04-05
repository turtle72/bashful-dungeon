import random
from collections import Counter
import copy
layFull = {}
layoutX=()
layoutY=()
mX = (0)
mY = (0)
threeroom = {}
def layout():
    global layoutX
    global layoutY
    layoutX = (random.randint(3,6)+1)
    layoutY = (random.randint(3,6)+1)
    for item in range(1,layoutX):
        for i in range(1,layoutY):
            layFull[f"X:{item} Y:{i}"] = {}
room = {}


layout()

startingCord = []
endCord = []


def cords():
    global startingCord
    global endCord
    while Counter(startingCord) == Counter(endCord):
        startingCord = [random.randint(1,layoutX) , random.randint(1,layoutY)]
        endCord = [random.randint(1,layoutX) , random.randint(1,layoutY)]

cords()


roomY = random.randint(4,15)
roomX = random.randint(4,15)

for i in range(1,roomY):
    room["y" + str(i)] = ['_'] * roomX
    threeroom['y'+str(i)] = ['_'] * roomX




def placemon(m,c,id=False):
    
    global mx, my
    for i in range(c):
        mX = random.randint(1,(len(room["y1"]) - 1))
        mY = random.randint(1,(len(room) - 1))
        while room[f"y{mY}"][mX] != '_':
            mX = random.randint(1,(len(room["y1"]) - 1))
            mY = random.randint(1,(len(room) - 1))
        if id==False:
            threeroom[f"y{mY}"][mX] = m 
        elif id==True:
            threeroom[f"y{mY}"][mX] = f"{m}{c}"

        room[f"y{mY}"][mX] = threeroom[f"y{mY}"][mX]


def fullname(n):
    if n == 'g':
        return('goblin')
    if n == 'o':
        return('orc')
    if n == 't':
        return('troll')
    if n == 's':
        return('skeleton')
    if n == 'z':
        return('zombie')
    if n == 'w':
        return('werewolf')
    if n == 'z':
        return('vampire')
    

def genroom():
    global threeroom
    layout()
    cords()
    roomY = random.randint(4,15)
    roomX = random.randint(4,15)

    for i in range(1,roomY):
        room["y" + str(i)] = ['_'] * roomX
    threeroom = room
