import random
speed = 0
baseHealth = 0
currentHealth = 0
currentTurnDmg = 0
DoT = 0
DoTurn = 0
exp = 0
def calc(i):
    i = (i//2)
    if i < 1:
        return(1)
    elif i < 75:
        return(i)
    else:
        return(75)

def dice(d):
    total = 0
    for item in range(int(str(d).split('d')[0])): total = total + random.randint(1,int(str(d).split('d')[1]))
    return(total)
def mnster(m,l):
    level = (calc(l))
    speed = 0
    baseHealth = 0
    currentHealth = 0
    currentTurnDmg = 0
    DoT = 0
    DoTurn = 0
    exp = 0
    if m == 'g':
        speed = level + 15
        baseHealth = level - 4
        currentHealth = level - 4
        currentTurnDmg = 0
        DoT = 0
        DoTurn = level + dice('1d3')
        exp = level -1
        gold = level//2 + 5
        #return('goblin')
    if m == 'o':
        speed = level - 5
        baseHealth = level + 5
        currentHealth = level + 5
        currentTurnDmg = 0
        DoT = 0
        DoTurn = level + dice('1d4')
        exp = level + 2
        gold = 2
        #return('orc')
    if m == 't':
        speed = level - 3
        baseHealth = level + 4
        currentHealth = level + 4
        currentTurnDmg = 0
        DoT = 0
        DoTurn = level + dice('1d3') + 1
        exp = level + 5
        gold = 3
        #return('troll')
    if m == 's':
        speed = level + 5
        baseHealth = level - 2
        currentHealth = level - 2
        currentTurnDmg = 0
        DoT = 0
        DoTurn = level + dice('1d3')
        exp = level + 5
        gold = 3
        #return('skeleton')
    if m == 'z':
        speed = level - 10
        baseHealth = level + 5
        currentHealth = level + 5
        currentTurnDmg = 0
        DoT = 0
        DoTurn = level + dice('1d5')
        exp = level + 10
        gold = 6
        #return('zombie')
    if m == 'w':
        speed = level + 12
        baseHealth = level +5
        currentHealth = level + 5
        currentTurnDmg = 0
        DoT = 0
        DoTurn = level + dice('1d8')
        exp = level + 12
        gold = 12
        #return('werewolf')
    if m == 'v':
        speed = level +3
        baseHealth = level - 2
        currentHealth = level - 2
        currentTurnDmg = level + 3
        DoT = 0
        DoTurn = level + dice('1d8') + dice('1d4')
        exp = level + 20
        gold = 35
        #return('vampire')
    monsterStats={'speed':speed,
                  'baseHealth':baseHealth,
                  'currentHealth':currentHealth,
                  'currentTurnDmg':currentTurnDmg,
                  'Dot':DoT,
                  'DoTurn':DoTurn,
                  'exp':exp,
                  'gold':gold,}
    return(monsterStats)