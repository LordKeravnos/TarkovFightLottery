import random


banList = ()
#overall banlist

def ammoNum():
    ammoGL = 0
    ammoNumerical = random.randint(1,45)
    ammoNumericalBool = bool(random.randint(0,1))
    if ammoNumericalBool == True:
        ammoGL = "greater than or equal to"
    else:
        ammoGL = "less than or equal to"

    print("Ammo must be {0} {1} Pen rating".format(ammoGL,ammoNumerical))

#script that randomises the ammo ban if the user picks the "numerical" option in main.main()

def armourNum():
    armourGL = 0
    armourNumerical = random.randint(1,6)
    armourNumericalBool = bool(random.randint(0,1))
    if armourNumericalBool == True:
        armourGL = "greater than or equal to"
    else:
        armourGL = "less than or equal to"
    
    print("Armour must be {0} class {1}".format(armourGL,armourNumerical))

#script that randomises the armour ban if the user picks the "numerical" option in main.main()

def backpackNum():
    bpGL = 0
    bpNumerical = random.randint(6,48)
    bpNumericalBool = bool(random.randint(0,1))
    if bpNumericalBool == True:
        bpGL = "greater than or equal to"
    else:
        bpGL = "less than or equal to"
    
    print("Backpack must be {0} {1} slots internal size".format(bpGL,bpNumerical))



def numerical():
    ammoNum()
    armourNum()
    backpackNum()

def loyalty():
    print("Not yet implemented")
#script that compiles the above ones for both options in main.main()