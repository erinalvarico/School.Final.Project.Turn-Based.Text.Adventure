'''
CMPT 120 Intro to Programming
Final Project: Pseudocode
Author: Erin Alvarico
Created: November 11, 2018
'''

# Pseudocode for game creation

'''
Prior to main code:
P.1. Import math
P.2. Import graphics
P.3. Functions
    P.3.1. damageToEnemy
        1. Runs if player selects to attack enemy
        2. Depending on enemy, takes current HP (Health Points) and subtracts from 
        current player attacking damage output
        3. if enemy has resistant properties or armor, damage taken is reduced
        4. if enemy HP is 0 or negative, run function deathOfEnemy
        5. if not, return and overwrite enemy's health
    P.3.2. healToAlly
        1. Runs if player is the class (cleric) and uses special ability
        2. player selects which ally to heal
        3. if ally's health is 0 or negative, it does not work and prompts
        to chose another ally
        4. if ally passes life condition, then player can heal and add HP to partner
        5. return new ally's health
    P.3.3. deathOfEnemy
        1. Runs if enemy HP is 0 or negative
        2. prints that enemy is dead
        3. enemy condition (if alive or dead) is changed
        4. return condition of life
        (The condition of life shows whether the player can attack the enemy
        again or not (No because it's dead it cannot die more))
    P.3.4. infoClassKnight
        1. print statement on:
            1. HP
            2. Type of attack
            3. Special attack
            4. Armor
            5. Weakness
            6. Would you like to choose this class?
    P.3.5. infoClassMage
        1. print statement on:
            1. HP
            2. Type of attack
            3. Special attack
            4. Armor
            5. Weakness
            6. Would you like to choose this class?
    P.3.6. infoClassCleric
        1. print statement on:
            1. HP
            2. Type of attack
            3. Special attack
            4. Armor
            5. Weakness
            6. Would you like to choose this class?
    P.3.7 ... More functions to be listed

1. Begin

2. Introduction to game:
    The game is a turn-based party game that can be played single-player
    or up to 4 other players. Similar to the tic-tac-toe code assignment,
    player turns will switch and other people can choose to play their own
    character.
    
3. Ask how many players are in the party:
    How many players will participate 1-4 
    1. if 1, only 1 player is made in the playerlist
    2. if 2, 2 players are stored and so on...
    
4. Ask about information of the players in the party
    The player can type in info for (class) to read a brief description
    of the class. After reading it will prompt to choose the selected
    class.

    Information will be stored and used as a reference:
    1. Name:
    the name of the player will store the character so that it is easy
    to determine which player turn it is.
    2. Class:
    player will be prompted to chose from 3 classes: knight, mage, cleric
    each class has a special attack function that only they can use.
    In addition to the different attack style, they have different HP
    levels and armor that determines if they have more damage dealt
    to their health.
    
    weakness levels:
    knight --> mage --> cleric --> knight
    
    3. Number:
    Chose a number between 1 and 10 to determine which player goes first.
    Player closest to 10 goes first.
    
    
5. More role-play print statements to give players more information about
    battling:
    1. print statement of scenario:
        4 enemies (not specified yet) in the playing field (most likely goblins)
        blocking the party's path. They intend to rob you, and you retaliate.
    2. print statement of 3 options during battle:
        1. Attack
            player inflicts damage
        2. Special Attack
            player can inflict damage or heal
        3. Defend
            player can take 0 damage for a turn
        
6. After all player information has been stored and initialized numbers
    are evaluated and player turns are determined.
    1. 4 enemies will generate random numbers from 1 to 10 with math function
    2. numbers are evaluated where which number closest to 10 goes first
    1. print statement of list of player and enemy turns
        
7. Battle commences:
    player 1 first goes and is prompts with 3 options:
    1. Attack
        P.1. Check class for type of damage
        1. Select enemy
        2. Enemy selection is given to attack function
        3. attack function runs
        4. store new HP of enemy from returned value
        5. end of turn
    2. Special Attack
        P.1. Check class for type of attack
        1. Select enemy or ally
        2. Enemy selection is given to special attack function
        3. special function runs
        4. store new HP of enemy or ally from returned value
        5. end of turn
    3. Defend
        1. player now has condition of immunity
        2. Stored condition eliminates damage
        3. end of turn
        
8. After end of player turn is given to next in line (list):
    1. if player, use other options listed above in battle
    2. if enemy, enemy generates random number from math function
    1 to 3 as:
        1. Attack
        2. Special Attack
        3. Defend
    same rules apply to player damage. End of turn.
    
9. Game ends once:
    1. Once all goblins are defeated
        1. good ending will play (function?) where party embarks on their
        journey after encounter WITHOUT anyone dying
        2. okay ending will play (function?) where party embarks on their journey
        after mourning and burying fallen allies.
    2. If all players are defeated
        1. bad ending will play (function?) where goblins are victorious and
        loots your camp and dead bodies.
        
10. Finishing code:
    A thank you for playing and enjoying the game. If player would like to play again
    (Might be too complicated to loop) to exit program and relaunch it.
    
11. Done with program
'''

