import turtle
from turtle import *
import time
import random

#global variable initializations
charGold=0
charHP=10
initHP=10
charDMG=[0,1,2,3]
enemHP=10
enemDMG=[0,1,2,3]
heal=5
weaponc=""
lvlupct=0
kinFlag=False
caveFlag=False
desFlag=False

time.sleep(0.01)

#read file
def readfile(file):
    with open(file, 'r') as file:
        file_contents = file.read()
        for char in file_contents:
            print(char, end='', flush=True)
            time.sleep(0.01)

#weapon selection
def weaponpick():
    global weapon
    while True:
        weapon = input("Which will you choose to defend yourself with on your journey? The sword, staff, or bow? - ")
        if weapon.lower() in ["sword", "staff", "bow"]:
            print("You grasp the " + weapon + ", and strap it to your back, feeling more confident than ever.")
            return weapon #Exit if valid choice
            break
        else:
            print("'Huh..? You'll take the...'" + weapon + "'? That's... not an option, brother. Did you mispeak?'") #Nonvalid choice

#Combat function
def combat():
    global charHP, enemHP, charDMG, enemHP, enemDMG, heal, initHP
    time.sleep(0.01)
    initHP=charHP #Used to keep consistent hp for level up function
    while charHP>0 or enemHP>0: #While both combatants are still alive
        print("You have " + str(heal) + " healing potions left.") #Remind how many healing potions they have
        dec=input("Type 'attack' to attack the enemy! Or type 'heal' to use a healing potion! - ")
        if dec=="attack":
            if weapon.lower() == "sword": #Dialogue for each weapon
                sword()
            elif weapon.lower() == "staff":
                staff()
            else:
                bow()
            # Check for a critical hit with 10% chance
            critical_chance = random.random()
            dmg = random.choice(charDMG) #Save dmg number
            if dmg==0:
                print("You missed!") #Miss
            elif critical_chance <= 0.1:
                dmg = (dmg * 2)  # Critical hit deals double damage
                enemHP = (enemHP - dmg)
                print("Critical Hit! You did " + str(dmg) + " damage to the enemy!")
                if enemHP==0 or enemHP<0: #Enemy dies
                    print("The enemy has fallen! Huzzah!")
                    levelup() #level up, then break
                    break
                else:
                    print("The enemy now has: " + str(enemHP) + "HP" )
            else:
                enemHP = (enemHP - dmg)
                print("You did " + str(dmg) + " damage to the enemy!")
                if enemHP==0 or enemHP<0:
                    print("The enemy has fallen! Huzzah!")
                    levelup()
                    break
                else:
                    print("The enemy now has: " + str(enemHP) + "HP" )
        elif dec=="heal":
            if heal>0:
                heal = heal-1
                healAmnt = random.choice([1,2,3,4,5]) #Heals a random amount between 1-5, uses a turn though
                charHP = charHP + healAmnt
                print("You have healed " + str(healAmnt) + "HP points.")
                print("You now have: " + str(charHP) + "HP" )
            else:
                print("You have no healing potions left!")
                continue
        else:
            print("That's not a decision!")
            continue
        print("The enemy attacks!")
        dmg=random.choice(enemDMG)
        if dmg==0:
            print("They missed!")
        else:
            charHP = (charHP - dmg)
            print("The enemy did " + str(dmg) + " damage to you!")
            if charHP==0 or charHP<0:
                print("You have died! Game over.")
                quit() #ends if death
            print("You now have: " + str(charHP) + "HP" )

def finalcombat(): #Used for last fight
    global charHP, enemHP, charDMG, enemHP, enemDMG, heal, initHP
    time.sleep(0.01)
    initHP=charHP
    while charHP>0 or enemHP>0:
        print("You have " + str(heal) + " healing potions left.")
        dec=input("Type 'attack' to attack the Minotaur! Or type 'heal' to use a healing potion! - ")
        if dec=="attack":
            if weapon.lower() == "sword":
                sword()
            elif weapon.lower() == "staff":
                staff()
            else:
                bow()
            # Check for a critical hit with 10% chance
            critical_chance = random.random()  # Generates a random number between 0 and 1
            dmg = random.choice(charDMG)
            if dmg==0:
                print("You missed!")
            elif critical_chance <= 0.1:
                dmg = (dmg * 2)  # Critical hit deals double damage
                enemHP = (enemHP - dmg)
                print("Critical Hit! You did " + str(dmg) + " damage to the Minotaur!")
                if enemHP==0 or enemHP<0:
                    readfile('goodending.txt')
                    break
                else:
                    print("The Minotaur now has: " + str(enemHP) + "HP" )
            else:
                enemHP = (enemHP - dmg)
                print("You did " + str(dmg) + " damage to the Minotaur!")
                if enemHP==0 or enemHP<0:
                    readfile('goodending.txt') #Win
                    quit()
                else:
                    print("The Minotaur now has: " + str(enemHP) + "HP" )
        elif dec=="heal":
            if heal>0:
                heal = heal-1
                healAmnt = random.choice([1,2,3,4,5])
                charHP = charHP + healAmnt
                print("You have healed " + str(healAmnt) + "HP points.")
                print("You now have: " + str(charHP) + "HP" )
            else:
                print("You have no healing potions left!")
                continue
        else:
            print("That's not a decision!")
            continue
        print("The Minotaur attacks!")
        dmg=random.choice(enemDMG)
        if dmg==0:
            print("They missed!")
        else:
            charHP = (charHP - dmg)
            print("The enemy did " + str(dmg) + " damage to you!")
            if charHP==0 or charHP<0:
                print("The Minotaur strikes you!")
                readfile('badending.txt') #Lose
                quit()
            print("You now have: " + str(charHP) + "HP" )

def human(): #Resets health and damage per boss
    global enemHP, enemDMG
    enemHP = 10
    enemDMG = [0,1,2,3]

def troll():
    global enemHP, enemDMG
    enemHP = 13
    enemDMG = [0,1,2,3,4]

def worm():
    global enemHP, enemDMG
    enemHP = 20
    enemDMG = [0,1,2,3,4,5,6]

def sword(): #Unique dialogue depending on weapopn choice
    list=["You swing your sword wide!", "You go for a brutal stab!", "You take a swipe at their legs with your sword!"]
    print(random.choice(list))
def staff():
    list=["You cast a fireball from your staff!", "You shoot bolts of electricity out!", "You summon magical rocks and sling them at the enemy!"]
    print(random.choice(list))
def bow():
    list=["You take a shot with your bow!", "You shoot for their eye!", "You unleash a volley of arrows!"]
    print(random.choice(list))

def levelup(): #Level up function
    global lvlupct, charHP, charDMG, heal, initHP
    while True:
        if lvlupct==0: #If they havent leveled up yet
            choice = input("You have leveled up! Type 'health' to increase your HP, or 'dmg' to increase your damage! - ")
            if choice.lower() == "health":
                charHP = 15
                print("You have increased your HP! You now have: " + str(charHP) + " health points.")
                lvlupct=1
                heal=5
                break
            elif choice.lower() == "dmg":
                charHP=10 #Reset health to full for next fight regardless
                charDMG = [0,2,3,4,5]
                print("You have increased your damage! You now have the potential to do up to 5 damage per turn!")
                lvlupct=1
                heal=5
                break
            else:
                print("That's not a valid choice!")
                continue
        elif lvlupct==1:
            choice = input("You have leveled up again! Type 'health' to increase your HP, or 'dmg' to increase your damage! - ")
            if choice.lower() == "health":
                if initHP == 10: #If they didn't choose health last time, make sure it only goes up by 5, not 10
                    charHP = 15
                else:
                    charHP = 20
                print("You have increased your HP! You now have: " + str(charHP) + " health points.")
                lvlupct=2
                heal=5
                break
            elif choice.lower() == "dmg":
                charHP=initHP
                charDMG = [0,3,4,5,6,7]
                print("You have increased your damage! You now have the potential to do up to 7 damage per turn!")
                lvlupct=2
                heal=5
                break
            else:
                print("That's not a valid choice!")
                continue
    
def travel(): #Looped travel function
    global kinFlag, caveFlag, desFlag, charGold
    while True:
        if charGold==100 or charGold>100: #If you get enough gold, run ending
            print("Finally! You managed to get enough gold to save your mother!")
            readfile('ending.txt')
            worm()
            finalcombat()
            break
        dest = input("Where will you go? North, west, or east? Or type 'q' to quit. - ")
        if dest.lower() == "north":
            if kinFlag==False: #Flags used to determine if they have/haven't visited yet
                readfile('kingdom.txt')
                dec=input(" Type 'fight' to enter combat, or 'run' to run out of the tavern! - ") #Run or fight interaction in kingdom
                if dec=="run":
                    kinFlag=True
                    readfile('dontfight.txt')
                    human()
                    combat()
                    wongold=random.randint(15, 65) #Gold prize between 15 and 65
                    charGold+=wongold
                    print("You won " + str(wongold) + "G! You now have " + str(charGold) + "G.")
                    print("The thief clutches his wounds before collapsing in the alley.")
                    print("You gather the gold he dropped and quickly exit the Kingdom, wary of other possible thieves.")
                    continue
                elif dec=="fight":
                    kinFlag=True
                    readfile('barfight.txt')
                    human()
                    combat()
                    wongold=random.randint(20, 70)
                    charGold+=wongold
                    print("You won " + str(wongold) + "G! You now have " + str(charGold) + "G.")
                    print("The bar stares in silence for a few before erupting in cheer. The gold is handed to you.")
                    print("After a few celebratory drinks, you exit the kingdom with your gold before another challenger appears.")
                    continue
            else:
                print("You have already explored this area! Try somewhere else.")
                continue
        elif dest.lower() == "west":
            if desFlag==False:
                desFlag=True
                readfile('desert.txt')
                worm()
                combat()
                wongold=random.randint(75, 100)
                charGold+=wongold
                print("You won " + str(wongold) + "G! You now have " + str(charGold) + "G.")
                print("With one last strike, the towering worm lets out one last cry and collapses.")
                print("A few seconds of silence goes by before you finally feel like you can breathe again.")
                print("You gather your well-earned prize, and make your way out of the desert, able to see another day.")
                continue
            else:
                print("You have already explored this area! Try somewhere else.")
                continue
        elif dest.lower() == "east":
            if caveFlag==False:
                caveFlag=True
                readfile('cave.txt')
                troll()
                combat()
                wongold=random.randint(30, 100)
                charGold+=wongold
                print("You won " + str(wongold) + "G! You now have " + str(charGold) + "G.")
                print("The troll lets out a pained roar as it slowly drops its bat and collapses against the cavern wall.")
                print("Water and debris fly past you, until the room finally falls silent. You catch your breath and inspect your winnings.")
                print("You follow a cracked passage in the back that leads you out to the other side of the mountain, seemingly undiscovered before you.")
                continue
            else:
                print("You have already explored this area! Try somewhere else.")
                continue
        elif dest.lower() == "q": #Quit statement
            quit()


