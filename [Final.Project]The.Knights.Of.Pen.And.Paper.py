'''
Class: CMPT120 Intro to Programing
Author: Erin Alvarico
Date: December 06, 2018
[ FINAL PROJECT ] Text-Based/Turn-Based RPG Adventure
'''

# [ Imports ]
# ---------------------------------------------------------------------------------------------------------------

# I imported 'math' tools because my code will need to rely on
# randomly generated numbers for CPU attacks as well as initiating
# turn style battling. To keep track of all information, I believe
# it would be most useful storing with numbers.
# I used 'sys' for forcing my program to terminate when player dies or
# to exit the game peacefully.

from random import randint
import math
import sys

# [ Branch Class ]
# ----------------------------------------------------------------------------------------------------------------

# This is the function that calls to the other separate classes the player
# can choose from. Essentially this enlightens the reader with what he/she
# can chose from. Multiple if loops are used to return different outputs
# to declare the info desired. A while loop is used to ensure player writes
# a viable answer.
def chooseAClass():

    # Variables used and returned
    chose_k = "knight"
    chose_m = "mage"
    chose_c = "cleric"

    # Visual of options via print statements
    print("")
    print("[ There are three types of classes you can choose from:                          ]")
    print("[                                                                                ]")
    print("[ 1. Knight                                                                      ]")
    print("[ 2. Mage                                                                        ]")
    print("[ 3. Cleric                                                                      ]")
    print("[                                                                                ]")
    print("[ Please type a class to read a description of its skills and attributes.        ]")
    print("")

    # Input for what desired class player wants to see
    chosen_class = input("What class would you like to learn more about? [ Knight/Mage/Cleric ] ").lower()

    # While loop to ensure player inputs viable variable to showcase the info of a selected class
    while chosen_class != chose_k or chosen_class != chose_m or chosen_class != chose_c:
        # Knight Class
        if chosen_class == chose_k:
            return chose_k

        # Mage Class
        if chosen_class == chose_m:
            return chose_m

        # Cleric Class
        if chosen_class == chose_c:
            return chose_c

        # Prints if invalid answer
        print("That is not a valid choice, please select a class provided.")
        print("")

        chosen_class = input("What class would you like to learn more about? [ Knight/Mage/Cleric ] ").lower()


# [ Classes ] **Figuratively and Literally**
# -----------------------------------------------------------------------------------------------------------------

# The [ Knight ] Class basically stores all the basic information
# about the character and their specialty. Returns all info for
# player to inquire and understand all of the advantages of this class.
def infoKnightClass():

    # Statistics and attributes of 'Knight' class
    kClass = "Knight"
    hp = 150
    attk_typ = "Melee"
    attk_dmg = 50
    spc_attk = "Unwavering Resolve"
    spcatk_dmg = 60
    armor = "Silver plated armor"
    wkns = "Cleric"

    # Printed description to player to understand 'Knight' Class
    print("--[ Knight ]---------------------------------------------------")
    print("")
    print("The knight is a noble line of work, trained in the arts of")
    print("finely tuned swordsmanship and defense. They seek to protect")
    print("those who cannot protect themselves, fighting off enemies")
    print("that invade their territory. Great tacticians and ever")
    print("loyal companions.")
    print("")
    print("--[ Statistics ]-----------------------------------------------")
    print("")
    print("[ Health ] ", hp)
    print("[ Attack Type ] ", attk_typ)
    print("[ Attack Damage ] ", attk_dmg)
    print("[ Special Attack ] ", spc_attk)
    print("Unwavering Resolve strengthens a knight's determination and")
    print("vigor, allowing them to release a heavy attack without hesitation")
    print("that may cause enemy to flinch or be stunned.")
    print("[ Special Attack Damage ] ", spcatk_dmg)
    print("[ Armor ] ", armor)
    print("[ Weak Against ] ", wkns)
    print("")
    print("---------------------------------------------------------------")

    # Input to choose class (.lower to take every variation of 'yes' or 'no'

    print("")
    class_choice = input(" Will you choose this class? [ Yes/No ] ").lower()
    print("")

    # Variables to determine answer and action in if loop

    kList = [ kClass, hp, attk_typ, attk_dmg, spc_attk, spcatk_dmg, armor, wkns]
    choice = False
    choice_no = "no"
    choice_yes = "yes"

    # Choice: Would the player like to chose the class
    # If loop to either a) select class type or b) go back
    # to selection for info on each class
    while class_choice != choice_no or choice_yes:
        # Return to selection
        if class_choice == choice_no:
            print("Very well, perhaps there is a different class more suited")
            print("to your play style.")
            print("")
            print("I will now return you to the class selection list.")
            print("")

            return choice, kList

        # Choose class
        if class_choice == choice_yes:
            print("A brilliant choice, my friend! May your strength and valor aid")
            print("you in your quest to protect others!")
            print("")
            choice = True

            return choice, kList

        # Prints when invalid answer
        print("That is not a valid choice, my friend.")

        print("")
        class_choice = input(" Will you choose this class? [ Yes/No ] ").lower()
        print("")


# The [ Mage ] Class basically stores all the basic information
# about the character and their specialty. Returns all info for
# player to inquire and understand all of the advantages of this class.
def infoMageClass():

    # Statistics and attributes of 'Mage' class
    mClass = "Mage"
    hp = 100
    attk_typ = "Magic"
    attk_dmg = 40
    spc_attk = "Phoenix Fireball"
    spcatk_dmg = 65
    armor = "Enchanted silk robes"
    wkns = "Knight"

    # Printed description to player to understand 'Mage' Class
    print("--[ Mage ]-----------------------------------------------------")
    print("")
    print("The mage is a prestigious field of work, as these sorcerers")
    print("study the wonders of elemental, arcane and enchantment magic.")
    print("They yearn to learn the aspects of everything around them.")
    print("Empowered by knowledge, mages seek to use their powers to")
    print("change the world around them to their benefit.")
    print("")
    print("--[ Statistics ]-----------------------------------------------")
    print("")
    print("[ Health ] ", hp)
    print("[ Attack Type ] ", attk_typ)
    print("[ Attack Damage ] ", attk_dmg)
    print("[ Special Attack ] ", spc_attk)
    print("Phoenix Fireball is an elite elemental level area-affect spell which")
    print("summons a fiery phoenix ally to burn down his/her foes. The flaming")
    print("bird comes down as a hellfire, covering the battlefield.")
    print("[ Special Attack Damage ] ", spcatk_dmg)
    print("[ Armor ] ", armor)
    print("[ Weak Against ] ", wkns)
    print("")
    print("---------------------------------------------------------------")

    # Input to choose class (.lower to take every variation of 'yes' or 'no'

    print("")
    class_choice = input(" Will you choose this class? [ Yes/No ] ").lower()
    print("")

    # Variables to determine answer and action in if loop

    mList = [mClass, hp, attk_typ, attk_dmg, spc_attk, spcatk_dmg, armor, wkns]
    choice = False
    choice_no = "no"
    choice_yes = "yes"

    # Choice: Would the player like to chose the class
    # If loop to either a) select class type or b) go back
    # to selection for info on each class

    while class_choice != choice_no or choice_yes:
        # Returns to class selection
        if class_choice == choice_no:
            print("Very well, perhaps there is a different class more suited")
            print("to your play style.")
            print("")
            print("I will now return you to the class selection list.")
            print("")

            return choice, mList

        # Accepts class
        if class_choice == choice_yes:
            print("A brilliant choice, my friend! May your strength and valor aid")
            print("you in your quest to protect others!")
            print("")
            choice = True

            return choice, mList

        # Prints if invalid input
        print("That is not a valid choice, my friend.")

        print("")
        class_choice = input(" Will you choose this class? [ Yes/No ] ").lower()
        print("")

# The [ Cleric ] Class basically stores all the basic information
# about the character and their specialty. Returns all info for
# player to inquire and understand all of the advantages of this class.
def infoClericClass():

    # Statistics and attributes of 'Cleric' class
    cClass = "Cleric"
    hp = 120
    attk_typ = "Cleansing"
    attk_dmg = 35
    spc_attk = "Grace of the Gods"
    spcatk_dmg = 45
    armor = "Blessed ceremonial robes"
    wkns = "Mage"

    # Printed description to player to understand 'Cleric' Class
    print("--[ Cleric ]---------------------------------------------------")
    print("")
    print("The cleric is a holy lineage, preaching the word of God and")
    print("his works to the world. They specialize in the art of ")
    print("exorcism to banish the demons that plague the lands as well")
    print("as restoration to heal the ailments and injuries of their")
    print("fellow bretheren.")
    print("")
    print("--[ Statistics ]-----------------------------------------------")
    print("")
    print("[ Health ] ", hp)
    print("[ Attack Type ] ", attk_typ)
    print("[ Attack Damage ] ", attk_dmg)
    print("[ Special Attack ] ", spc_attk)
    print("Grace of the Gods calls upon the help of the Lords above to grace")
    print("their fellow teammates with blessings and heal their battle")
    print("wounds. This spell is a singular cast upon one ally.")
    print("[ Special Attack Damage ] ", spcatk_dmg)
    print("[ Armor ] ", armor)
    print("[ Weak Against ] ", wkns)
    print("")
    print("---------------------------------------------------------------")

    # Input to choose class (.lower to take every variation of 'yes' or 'no'

    print("")
    class_choice = input(" Will you choose this class? [ Yes/No ] ").lower()
    print("")

    # Variables to determine answer and action in if loop

    cList = [cClass, hp, attk_typ, attk_dmg, spc_attk, spcatk_dmg, armor, wkns]
    choice = False
    choice_no = "no"
    choice_yes = "yes"

    # Choice: Would the player like to chose the class
    # If loop to either a) select class type or b) go back
    # to selection for info on each class

    while class_choice != choice_no or choice_yes:
        # Returns to class selection
        if class_choice == choice_no:
            print("Very well, perhaps there is a different class more suited")
            print("to your play style.")
            print("")
            print("I will now return you to the class selection list.")
            print("")

            return choice, cList

        # Accepts class
        if class_choice == choice_yes:
            print("A brilliant choice, my friend! May your strength and valor aid")
            print("you in your quest to protect others!")
            print("")

            return choice, cList

        print("That is not a valid choice, my friend.")

        print("")
        class_choice = input(" Will you choose this class? [ Yes/No ] ").lower()
        print("")

# [ Ally ]
# ----------------------------------------------------------------------------------------------------------------

# I decided to add a personal player in the game, similar to
# many RPG games that have a party system. Acts very much like
# the player's functions, but with a more storyline built-in
# vibe.
def lilyInfo(lilyList):

    # transfer list variables to use in function
    infoList = lilyList

    lClass = infoList[0]
    hp = infoList[1]
    attk_typ = infoList[2]
    attk_dmg = infoList[3]
    spc_attk = infoList[4]
    spcatk_dmg = infoList[5]
    armor = infoList[6]
    wkns = infoList[7]

    # Printed description to player to understand 'Blade Dancer' Class
    print("--[ Blade Dancer ]-----------------------------------------------")
    print("")
    print("The Blade Dancer is a quirky and challenging class, often used")
    print("by those who find the art of fighting much like a dance. You")
    print("can find those who master this art to be nimble on their feet")
    print("and strike as fast as a viper! They love to put on a dazzling")
    print("show!")
    print("")
    print("--[ Statistics ]-----------------------------------------------")
    print("")
    print("[ Health ] ", hp)
    print("[ Attack Type ] ", attk_typ)
    print("[ Attack Damage ] ", attk_dmg)
    print("[ Special Attack ] ", spc_attk)
    print("Slash Storm sends a flurry of strikes to tear through their")
    print("opponent. This attack normally hits more than once, where")
    print("the amount of slashes combined, the more damage.")
    print("[ Special Attack Damage ] ", spcatk_dmg)
    print("[ Armor ] ", armor)
    print("[ Weak Against ] ", wkns)
    print("")
    print("---------------------------------------------------------------")

# [ Opponent ]
# -----------------------------------------------------------------------------------------------------------------

# In the story, Bill is a coded CPU that the player must
# defeat in order to successfully finish the game. This
# function, much like Lily's is designed to show the depth
# of character and variables hidden in characters.
def billyInfo(billyList):

    # Transfer list variables to function
    infoList = billyList

    lClass = infoList[0]
    hp = infoList[1]
    attk_typ = infoList[2]
    attk_dmg = infoList[3]
    spc_attk = infoList[4]
    spcatk_dmg = infoList[5]
    armor = infoList[6]
    wkns = infoList[7]

    # Printed description to player to understand 'Brawler' Class
    print("--[ Brawler ]--------------------------------------------------")
    print("")
    print("The Brawler fighting-style is more suited for those with a")
    print("quick temper and raging determination. Masters of mixed")
    print("martial arts, these opponents are challenging to take down")
    print("as one swift mistake can lead to your demise. They value more")
    print("brawn over brain!")
    print("")
    print("--[ Statistics ]-----------------------------------------------")
    print("")
    print("[ Health ] ", hp)
    print("[ Attack Type ] ", attk_typ)
    print("[ Attack Damage ] ", attk_dmg)
    print("[ Special Attack ] ", spc_attk)
    print("K.O. Punch is a devastating one hit disaster, where a brawler")
    print("sends a steely fist into a spotted vital opening in your")
    print("defense. Can leave player stunned.")
    print("[ Special Attack Damage ] ", spcatk_dmg)
    print("[ Armor ] ", armor)
    print("[ Weak Against ] ", wkns)
    print("")
    print("---------------------------------------------------------------")

# [ Functions ]
# ----------------------------------------------------------------------------------------------------------------

# Gives the player three choices in which he/she can choose how to
# fight and defeat Bill. Options are coded as numbers to change
# every turn much like how we learned in the tic-tac-toe lab.
def turnChoices():

    # Variables used to return
    attack = "1"
    specialAttack = "2"
    inspect = "3"

    # Visual for player to see options via print statements
    print("[ What will you do?                                                        ]")
    print("----------------------------------------------------------------------------")
    print("")
    print("1. Attack")
    print("2. Special Attack")
    print("3. Inspect")
    print("")
    print("----------------------------------------------------------------------------")
    print("")

    # Player input to determine what to return
    action = str(input("Select an action: [ 1/2/3 ] "))

    # While loop to ensure there is a viable input given
    while action != attack or specialAttack or inspect:
        # Attack option
        if action == attack:
            return attack

        # Special Attack option
        if action == specialAttack:
            return specialAttack

        # Inspect option
        if action == inspect:
            return inspect

        # Printed when invalid option: prompts input again
        print("")
        print("That is not a correct input, please choose a course of action.")
        print("")

        action = str(input("Select an action: [ 1/2/3 ] "))

# This function uses math to determine the amount of hp
# a player has. Hp will determine the course of battle,
# Whether the player wins or the player loses.
def damageToEnemy(list, opList):

    # Transferring lists
    damageList = list
    enemyList = opList

    # Subtracting health from opponent via normal attack damage
    enemyList[1] = enemyList[1] - damageList[3]

    # Informing player of status of players
    print("")
    print("[ ", damageList[2], " attack for ", damageList[3], " damage!                             ]")

    # Returning updated lists
    return damageList, enemyList


# This function uses math to determine the amount of hp
# a player has. Hp will determine the course of battle,
# Whether the player wins or the player loses.
def specialAttack(list, opList):

    # Transferring lists
    specialList = list
    enemyList = opList

    # Subtracting health from opponent via special attack damage
    enemyList[1] = enemyList[1] - specialList[5]

    # Informing player
    print("")
    print("[ ", specialList[4], " is launched for ", specialList[5], " damage!                      ]")

    # Returning updated lists
    return specialList, enemyList

# Inspecting players and their abilities, this can
# help the player determine and anticipate opponent's
# next moves and when to be on the offense.
def inspect(players):

    # Transferring list
    candidates = players

    # Asks which player the player would like to check their stats
    print("")
    print("[ Which player would you like to inspect?                                                   ]")

    # Input given
    inspected = input("Please choose player: [ Lily/Bill ] ").lower()

    # While loop to ensure given answer is appropriate
    while inspected != "lily" or "bill":
        # Check stats of Lily
        if inspected == "lily".lower():
            return candidates[1]

        # Check stats of Bill
        if inspected == "bill".lower():
            return candidates[2]

        # Printed if not a valid input
        print("")
        print("I do not understand. Please choose a player to inspect.")
        print("")

        inspected = input("Please choose player: [ Lily/Bill ] ").lower()

# This function only is used when player decides
# to choose to play the cleric class, in which healing
# is a special option for gameplay.
def healToAlly(list, lilyList):

    # Transferring lists
    healList = list
    allyList = lilyList

    # Prompts user to whom do they want to perform the heal to?
    print("")
    print("[Who do you wish to heal?                                                ]")
    print("")

    # Input given
    heal = input("Choose player to heal: [ Self/Lily ] ").lower()

    # While statement to ensure that a viable option is given

    while heal != "self" or "lily":
        # Self healing spell
        if heal == "self":
            # Adding special attack damage to health
            healList[1] = healList[1] + healList[5]

            # Informing player of actions and new health
            print("")
            print("[ ", healList[4], " is casted over yourself for ", healList[5], " health!                             ]")
            print("[ You now have ", healList[1], " health.                                                              ]")

            # Return updated lists
            return healList, allyList

        # Heal ally, Lily
        if heal == "lily":
            # Adding special attack to health
            allyList[1] = allyList[1] + healList[5]

            # Informing player of actions and new health
            print("")
            print("[ ", healList[4], " is casted over Lily for ", healList[5], " health!                                 ]")
            print("[ Lily now has ", healList[1], " health.                                                              ]")

            # Return updated lists
            return healList, allyList

        # Prints if a non-viable input is given
        print("")
        print("That is not a correct input. Please choose a player to heal:")
        print("")

        heal = input("Choose player to heal: [ Self/Lily ] ").lower()

# If Lily's hp is 0 then Lily can no longer play!
# Lily loses the ability to be played and commanded.
def deathToAlly(lilyList):

    deathList = lilyList
    deathAlly = False

    if deathList[1] == 0:
        print("")
        print("[ Uh oh! Lily's health has depleted: Ally has fallen!                                                 ]")
        deathAlly = True
        return deathAlly
    else:
        print("")
        print("[ Lily is still in good shape!                                                                        ]")
        return deathAlly

# If Player hp is 0 then the game ends the
# program, as the player has failed. Player
# can play again if they run the program again.
def deathToPlayer(pList):

    deathList = pList
    deathPlayer = False

    if deathList[1] == 0:
        print("")
        print("[ Uh oh! Your health has depleted: You have been defeated...                                   ]")
        print("")

        print("[ FAILURE: END OF GAME ]")
        deathPlayer = True
        return deathPlayer
    else:
        print("")
        print("[ Phew, you're still in good shape! Keep fighting!                                            ]")
        return deathPlayer

# If the player is successful in killing the CPU
# the player wins the game! If Bill's health is 0,
# Bill is unable to play, therefore the player wins!
def deathToEnemy(billyList):

    deathList = billyList
    deathBill = False

    if deathList[1] == 0:
        print("[ Billy has no more health: Enemy has succumbed to their wounds!                                      ]")
        print("")

        print("[ VICTORY! ]")
        deathBill = True

        return deathBill
    else:
        print("[ Billy is still standing! Keep up the fire!                                                          ]")
        print("")

        return deathBill

# [ Main Class ]
# ----------------------------------------------------------------------------------------------------------------

# Where the main storyline and text is. The turn-based combat is included in here,
# while functions are referenced in a while loop that continues until either the
# Player or the CPU dies.
def main():

    # First line of code displayed to Player
    print("Greetings player!")

    # Since my game has a lot of reading, story and depth, I believed that a 'stopper'
    # would help the player read all the text and dialogue as he/she plays
    # I tried spacing all the lines as best as I could.
    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("Welcome to the world of Coderica, the land of infinite adventures!")

    # Input personalized name for Player. .capitalize() function to ensure the
    # Player's name is written grammatically correct
    print("")
    player_name = input("What do people call you? [Name] ").capitalize()
    print("")

    # Variable name is re-called to feel personalized in game
    print(player_name, "? What a wonderful name!")
    print("Haha, I'm just joking with you, of course I remember my good old friend's calling!")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    # Asks Player to write an integer for their age
    print("I must congratulate you on your birthday, dear friend, you're turning...")
    player_age = int(input("My word have I forgotten? Please, remind me! [Number]  "))

    # Recalled variable again to fit the story: very much like the mad-libs lab
    print("")
    print(player_age, "! That's right you're ", player_age, " this year- oh my you're")
    print("getting quite old already huh? I'm kidding, I'm kidding!")
    print("")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("It's quite a milestone, isn't it? Everyone is so excited to see you")
    print("mature into such a strong and determined soul.")
    print("")
    print("It also marks the day you planned on leaving this small, old town, right?")
    print("What? Don't look at me like that, of course I know! I can tell from the")
    print("look in your eyes from the first day I met you, you were a dreamer.")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("No, being an air-head like yourself isn't bad. Small town life just")
    print("doesn't suit you as it fits the rest of us. And that's okay!")
    print("")
    print("Don't feel guilty, we all encourage you to follow your dreams!")
    print("Just remember to write back every once and awhile, and be sure")
    print("that I'll hunt you down if you don't keep that promise!")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("Now what are you waiting for? Go pack and get ready, everyone's")
    print("waiting to throw you the biggest 'farewell and safe travels' party")
    print("anyone has ever seen! I'll be waiting for you, future adventurer,")
    print("don't keep them waiting!")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    # [ Introductory Messages ]
    # ------------------------------------------------------------------------------------------------------------

    # The start of the real story and not the prep phase.
    print("[ CHAPTER 1: EVERYDAY TAVERN SQUABBLE ]")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[ You have been traveling for months, visiting all kinds of lands ranging    ]")
    print("[ from big, bustling cities to small, tight-knit towns. It's been a          ]")
    print("[ big passion of yours to travel the world, and finally for your ", player_age, "th      ]")
    print("[ birthday you embarked on your journey! In order for you to survive the     ]")
    print("[ perils of the unforgiving world, you seeked masters of various professions ]")
    print("[ to teach you their craft. You even used those skills to help a few here    ]")
    print("[ there.                                                                     ]")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[ You approach a small, nicely developed town with cobblestone walls and     ]")
    print("[ oil lantern lamp posts to light up your path. The weather hasn't been very ]")
    print("[ kind to you, raining on almost every day you've departed the cityscape a   ]")
    print("[ week ago. You decide to step into a seemingly-welcoming, well-lit tavern.  ]")
    print("[ Just as you enter the main door, a cheerful beautiful barmaid greets you.  ]")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[Barmaid ???] Welcome traveler, you look quite weary!")
    print("[Barmaid ???] Here, follow me I'll sit you down real quick!")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[ She cheerfully gestures towards a small opening in the bustling crowd. She  ]")
    print("[ Squeezes her way through, guiding you to a small round, wooden table close  ]")
    print("[ to the barside. Other waitresses can be seen rushing in and out of the      ]")
    print("[ kitchen carrying piles of dishes out for the packs of hungry adventurers.   ]")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[Barmaid ???] Here you are! My name is Lily, I'm the proud owner of this whole")
    print("lively establishment!")
    print("[Barmaid Lily] Say, I haven't seen your face before: new around these parts?")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[ You eagerly nod yes, and briefly explain how you have just started your     ]")
    print("[ adventure. She beams with happiness and hands you a menu. Lily then hollers ]")
    print("[ up to the nearby bartender.                                                 ]")
    print("")

    print("[Barmaid Lily] Hey Willie, whip up one of our house favorite beers for my new")
    print("friend!")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[ The bartender briefly glances at the bubbly woman and simply nods in         ]")
    print("[ acknowledgment.                                                              ]")
    print("")

    print("[Barmaid Lily] That's real nice that you're exploring the world for yourself!")
    print("There's really so many wonders in the world-gosh you should bring me along too!")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[ Lily gives a bright and energetic laugh, almost lighting up the noisy tavern. ]")
    print("[ You can definitely see why she's the head of the pub. Suddenly she gasps and  ]")
    print("[ points at your weapon in excitement.                                          ]")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[Barmaid Lily] I haven't seen one of those before, it's shocking! What type of")
    print("warrior are you?")

    classConfirmed = False

    # Calls first function: choose a class to declare what type of fighter
    # the player would like to be

    class_select = str(chooseAClass())

    while classConfirmed != True:
        # 'pList' is to store all class attributes to use later on in turn-based
        # combat
        # If loops to determine which class was returned and selected for the player to
        # be

        if class_select == "knight".lower():
            select, pList = infoKnightClass()

            if select == True:
                break

        if class_select == "mage".lower():
            select, pList = infoMageClass()

            if select == True:
                break

        if class_select == "cleric".lower():
            select, pList = infoClericClass()

            if select == True:
                break

        print("")
        print("It seems that you didn't select a class yet!")
        print("Please revisit the possible classes:")

        class_select = str(chooseAClass())

    input("[ Press < Enter > to Continue ]")

    print("")
    print("[ Lily nods in approval, enraptured by your detailed description of your training  ]")
    print("[ and adventures. Willie slides a tankard across the bar table perfectly within    ]")
    print("[ comfortable reach.                                                               ]")
    print("")

    # First use of the transferred variables list
    print("[Barmaid Lily] Wow, a ", pList[0], " huh? That's so cool- I wish I could be one!")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[ A loud, mocking laugh suddenly interrupts your pleasant chat with Lily. Lily     ]")
    print("[ pauses and turns around, seemingly annoyed at the approaching figure. A tall     ]")
    print("[ bulky male comes staggering closer: clearly he's had too much to drink.          ]")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[Drunk Man] Oi, little pipsqueak, you call yourself an adventurer? HAHAHAHAHA, more")
    print("like a sorry excuse for a wash rag used to sweep my bum!")
    print("")

    print("[Barmaid Lily] Hey, Bill! Watch what you're saying or I'll toss you out this instant!")
    print("You drank too much again haven't you?!")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[Drunk Bill] Ehhh, I'm not THAT drunk Lils! You know I can hold my liquor!")
    print("")

    print("[ Bill belches and lets out a hearty laugh. Lily seems disgusted.                  ]")
    print("")

    print("[Drunk Bill] Hey there little runt, what say you go hand and hand with ole' Billy?")

    # CPU challenges Player to fight: input determines how fight starts
    print("")
    choice_fight = input("Billy has challenged you to a duel. Will you accept? [ Yes/No ] ").lower()

    # Both ally and enemy lists are created with their attributes to use in turn-based
    # combat
    lilyList = ["Blade Dancer", 130, "Melee", 30, "Slash Storm", 60, "Barmaid dress", "knight"]
    billyList = ["Brawller", 200, "Melee", 35, "K.O. Punch", 100, "Untasteful spandex trousers", "mage"]

    # If player said yes... version a) intro to battle
    if choice_fight == "yes".lower():

        print("")
        print("[Drunk Bill] Alright, alright! Perhaps I underestimated you, pipsqueak! You got the balls to say")
        print("yes at least!")
        print("[Drunk Bill] ... But ya in for a beating! NO one wins against big ole' Billy! BWHAHAHAHA")

        print("")
        input("[ Press < Enter > to Continue ]")
        print("")

        print("[ Lily grabs your arm before you can even get up. She looks at you a little worried.   ]")
        print("")

        print("[Barmaid Lily] Listen, I'm so sorry you have to deal with this. This is my bar, so I'm")
        print("more than happy to help you in your battle!")
        print("")

        print("< Lily joins your party!                                                               >")

        print("")
        input("[ Press < Enter > to Continue ]")
        print("")

        print("[ Bill takes a couple steps back as you rise and walk around your table to the open    ]")
        print("[ floor. Lily follows behind you, unsheathing her own weapon: an intricately decorated ]")
        print("[ expanding/shrinking metal pole-arm. You question for a brief second where in the      ]")
        print("[ world Lily could have gotten that, let alone wield it with skill. You shrug it off   ]")
        print("[ as a question for another time.                                                      ]")

        print("")
        input("[ Press < Enter > to Continue ]")
        print("")

        print("[Drunk Bill] Whenever you're ready runt, I'll give ya the first blow. HAHAHA")
        print("")

        print("[ INITIATING BATTLE SEQUENCE ]")

    # If player said no or anything else... version b) intro to battle
    else:
        print("")
        print("[ Bill seems to get more annoyed by your polite decline. He rolls his shoulders and  ]")
        print("[ lets out an agitated growl, slamming his fist against the table. The amount of     ]")
        print("[ force put into that swing surely made a dent in Lily's poor table.                 ]")

        print("")
        input("[ Press < Enter > to Continue ]")
        print("")

        print("[Drunk Bill] What do you mean no? Scared to fight eh? You really aren't cut out for  ]")
        print("this adventuring thing afterall!")
        print("")

        print("[ He takes another swing this time at your face. Luckily, Lily had deflected the     ]")
        print("[ with her ornate expanding/shrinking polearm. You wonder where she even got that... ]")

        print("")
        input("[ Press < Enter > to Continue ]")
        print("")

        print("[Barmaid Lily] ENOUGH! Bill, I swear if you swing at one of my customers I will put  ]")
        print("you through that window like I did last Wednesday!")
        print("")
        print("< Lily joins your party!                                                             >")

        print("")
        input("[ Press < Enter > to Continue ]")
        print("")

        print("[ Bill, shaking off the stun of the blow Lily had knocked him back with now glares   ]")
        print("[ daggers at the both of you. He seems to be prepping to strike!                     ]")
        print("")

        print("[Barmaid Lily] Are you okay? Come here, let's kick Bill out of the bar, I'll need some")
        print("backup! I don't want him beating up my customers again!")
        print("")

        print("[ INITIATING BATTLE SEQUENCE ]")

    # [ Turn - based choice battle ]
    # ------------------------------------------------------------------------------------------------------------

    # Start of turn-based battling
    # Very similar to tic-tac-toe but with three opponents
    # Players are put into a list to determine and introduce the turn
    # Starts off with Player making the first move.

    turn = 1
    players = [player_name, "Lily", "Bill"]

    # Lists to help switch and use the same functions for various outputs
    # and inputs
    list = []
    opList = []

    # While loop determining whether the CPU's health is 0 or not. If the hp
    # reaches 0, the player moves on in the storyline and wins!
    while billyList[1] != 0:

        # If it is Player's turn...
        if turn == 1:

            # Marks which attributes to use and who the Player is attacking
            list = pList
            opList = billyList

            # Informing player
            print("[ It is ", players[0], "'s turn!                                                  ]")

            # Pause
            print("")
            input("[ Press < Enter > to Continue ]")
            print("")

            # Call to function to determine action
            play = turnChoices()

            # Actions are determined by numbers to call the correct function
            # Normal attack:
            if play == "1":
                list, billyList = damageToEnemy(list, opList)

            # Special Attack:
            if play == "2":

                # If cleric class...
                if list[0] == "cleric":
                    list, lilyList = healToAlly(list, lilyList)
                else:
                 pList, billyList = specialAttack(list, opList)

            # Inspect
            if play == "3":
                ins = inspect(players)

                # Which player is inspected
                if ins == "Lily":
                    lilyInfo(lilyList)
                if ins == "Bill":
                    billyInfo(billyList)

            # Checks for the death of player
            if deathToPlayer(pList) == True:
                sys.exit()

            # Check for the death of ally
            if deathToAlly(lilyList) == True:
                print("[ Ally Slain ]")

            # Check for death of opponent
            if deathToEnemy(billyList)== True:
                break

            # Pause
            print("")
            input("[ Press < Enter > to Continue ]")
            print("")

        # Ally's turn...
        if turn == 2:
            list = lilyList
            opList = billyList
            print("[ It is ", players[1], "'s turn!                                                  ]")

            print("")
            input("[ Press < Enter > to Continue ]")
            print("")

            play = turnChoices()

            if play == "1":
                list, billyList = damageToEnemy(list, opList)
            if play == "2":
                list, billyList = specialAttack(list, opList)
            if play == "3":
                ins = inspect(players)

                if ins == "lily":
                    lilyInfo(list)
                if ins == "billy":
                    billyInfo(billyList)

            # Checks for the death of player
            if deathToPlayer(pList) == True:
                sys.exit()

            # Check for the death of ally
            if deathToAlly(lilyList) == True:
                print("[ Ally Slain ]")

            # Check for death of opponent
            if deathToEnemy(billyList) == True:
                break

            print("")
            input("[ Press < Enter > to Continue ]")
            print("")

        # Opponent's turn...
        # Fully controlled by random math
        # Only options are attack and special attack,
        # will finish turn quickly.
        if turn == 3:
            list = billyList
            print("[ It is ", players[2], "'s turn!                                                  ]")

            print("")
            input("[ Press < Enter > to Continue ]")
            print("")

            action = randint(1, 4)
            opponent = randint(1, 4)

            if opponent >= 2:
                opList = pList
            if opponent <= 2:
                opList = lilyList

            if action >= 2:
                if opponent >= 2:
                    list, pList = damageToEnemy(list, opList)
                if opponent < 2:
                    list, lilyList = damageToEnemy(list, opList)

            if action < 2:
                if opponent >= 2:
                    list, pList = specialAttack(list, opList)
                if opponent < 2:
                    list, lilyList = specialAttack(list, opList)

            # Checks for the death of player
            if deathToPlayer(pList) == True:
                sys.exit()

            # Check for the death of ally
            if deathToAlly(lilyList) == True:
                print("[ Ally Slain ]")

            # Check for death of opponent
            if deathToEnemy(billyList) == True:
                break

            print("")
            input("[ Press < Enter > to Continue ]")
            print("")

        # Change of turn once every function is checked
        # goes from 1 to 3
        turn = turn % 3 + 1

    # Break when successfully beaten the CPU, back to role-play
    print("")
    print("[ Drunk Bill flies through the front door and lands hard on the outside pavement. He groans  ]")
    print("[ in pain, sluggishly squirming on the floor from the beating he just had. Lily lets out a   ]")
    print("[ victorious yelp and sheaths her weapon. You do the same.                                   ]")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[Barmaid Lily] I'm sorry about that ruckus folks! Drinks on the house this time!")
    print("")

    print("[ The other citizens and adventurers cheer and holler, clearly this type of stuff happens all ]")
    print("[ the time. Lily seems like she's enjoying the attention and happiness of her customers.      ]")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    print("[Barmaid Lily] Thank you so much, you saved my lil' tavern from becoming a bloodbath! You're  ]")
    print("welcome to stay anytime you like, free of charge!")
    print("")

    print("[ You graciously thank Lily for her hospitality. Perhaps your adventure is beginning to get   ]")
    print("[ interesting. Perhaps you'll stay awhile in this quaint town.                                ]")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    # Thank you and clarifying end to the game to notify player
    print("[ END OF CHAPTER 1: EVERYDAY TAVERN SQUABBLE ]")
    print("------------------------------------------------------------------------------------")
    print("")
    print("Congratulations on finishing chapter 1! The next chapters are still in development,")
    print("please stay tuned and thank you for playing!")

    print("")
    input("[ Press < Enter > to Continue ]")
    print("")

    # Peaceful exit of game as game was successfully beaten and played
    print("[ PROGRAM WILL NOW TERMINATE ]")
    sys.exit()

main()
