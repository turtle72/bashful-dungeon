import random


prefixWeapon = ['Mythril', 'Diamond', 'Gold', 'Obsidian', 'Emerald', 'Bone', 'Silver', 'Steel', 'Iron', 'Brass', 'Copper', 'Lead', 'Wooden']

baseWeapons = ['Sword', 'Wand', 'Dagger', 'Axe', 'Hammers', 'Bat', 'Brass knuckles', 'Cane', 'Stick', 'Pipe']

suffixWeapon = ['Of Green Burn', 'Of lightning', 'Of Flame', 'Of Frost', 'Of Speed', 'Of Poison', 'Of Tank', 'Of Curse','','',''] 

DoT = (0)

WeaponDmg = {'Weapon':{},'Prefix':{},'Suffix':{}}


def levcheck(l,p,b):
    if l > 10:
        if len(p)+5 < len(b):
            l = (((l//10)*10)//2)

            if l//2 > 500:
                return(500)
            else:
                return(l//2)
        else:
            return(0)
    else:
        return(0)


def weapon(f):
    

    luck_factor = 1 + f/5
    

    base_factor = 1 + f/2
    

    luck_level = random.randint(1, 10) * luck_factor
    

    prefix_weights = []
    for i in prefixWeapon:
        prefix_weights.append(((prefixWeapon.index(i)+1)//2)+levcheck(f,prefix_weights,prefixWeapon))
    prefix = random.choices(prefixWeapon, weights=prefix_weights, k=1)[0]
    
    base_weights = []
    for i in baseWeapons:
        base_weights.append(((baseWeapons.index(i)+1)//2)+levcheck(f,base_weights,baseWeapons))
    base = random.choices(baseWeapons, weights=base_weights, k=1)[0]

    suffix_weights = []
    for i in suffixWeapon:
        suffix_weights.append(((suffixWeapon.index(i)+1)//2)+levcheck(f,suffix_weights,suffixWeapon))
    suffix = random.choices(suffixWeapon, weights=suffix_weights, k=1)[0]
    
    
    WeaponDict = {'prefix':[prefixWeapon.index(prefix),prefix],'base':[baseWeapons.index(base),base],'suffix':[suffixWeapon.index(suffix),suffix]}
    print(WeaponDict['prefix'][1])
    return(WeaponDict)
print(weapon(10))