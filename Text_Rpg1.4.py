#Python first game (By Jack)

import cmd
import textwrap
import sys
import os
import time
import random
import pdb
import json
screen_width = 100


### Player Setup ###
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 1
        self.mp = 1
        self.atk = 0
        self.mpatk = 0
        self.money = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False
myPlayer = player()
### Title screen ###
def title_screen_selections():
    option = input('> ')
    while option.lower() not in ['play', 'help', 'leave', 'load']:
        print('please enter a valid command')
        option = input('> ')
    if option.lower() == ('play'):
        setup_game()
    elif option.lower() == ('load'):
        loadgame()
        main_game_loop()
    elif option.lower() == ('help'):
        help_menu()
    elif option.lower() == ('leave'):
        sys.exit()

def title_screen():
    os.system('clear')
    print('#########################')
    print('#Welcome To The Text RPG#')
    print('#########################')
    print('#        -Play-         #')
    print('#        -Load-         #')
    print('#        -Help-         #')
    print('#        -Leave-        #')
    print('#########################')
    title_screen_selections()

lv = 1
xp = 0
oldlv = 0
lvhp = 0
lvmp = 0
lvatk = 0
lvmpatk = 0
ironsword = False
ironarmor = False
coppersword = False
copperarmor = False
steelsword = False
steelarmor = False
arcanebook = False
masterbook = False
#save/load files
def loadgame():
    try:
        global ironsword
        global ironarmor
        global coppersword
        global copperarmor
        global steelsword
        global steelarmor
        global lvhp 
        global lvmp
        global lvatk
        global lvmpatk
        global oldlv
        global lv
        print('loading game...')
        data={}
        with open('savegame.txt') as infile:
            data=json.load(infile)
        myPlayer.name = data['player'][0]['name']
        myPlayer.job = data['player'][0]['job']
        myPlayer.hp = data['player'][0]['hp']
        myPlayer.mp = data['player'][0]['mp']
        myPlayer.atk = data['player'][0]['atk']
        myPlayer.mpatk = data['player'][0]['mpatk']
        myPlayer.money = data['player'][0]['money']
        myPlayer.location = data['player'][0]['location']
        lv = data['player'][0]['lv']
        lvhp = data['player'][0]['lvhp']
        lvmp = data['player'][0]['lvmp']
        lvatk = data['player'][0]['lvatk']
        lvmpatk = data['player'][0]['lvmpatk'] 
        xp = data['player'][0]['xp'] 

        ironsword = data['shop'][0]['ironsword']
        ironarmor = data['shop'][0]['ironarmor']
        coppersword = data['shop'][0]['coppersword']
        copperarmor = data['shop'][0]['copperarmor']
        steelsword = data['shop'][0]['steelsword']
        steelarmor = data['shop'][0]['steelarmor']
        steelsword = data['shop'][0]['arcanebook']
        steelarmor = data['shop'][0]['masterbook'] 

        zonemap['a1'][SOLVED] = data['zonemapsave'][0]['a1']
        zonemap['a2'][SOLVED] = data['zonemapsave'][0]['a2']
        zonemap['a3'][SOLVED] = data['zonemapsave'][0]['a3']
        zonemap['a4'][SOLVED] = data['zonemapsave'][0]['a4']
        zonemap['b1'][SOLVED] = data['zonemapsave'][0]['b1']
        zonemap['b2'][SOLVED] = data['zonemapsave'][0]['b2']
        zonemap['b3'][SOLVED] = data['zonemapsave'][0]['b3']
        zonemap['b4'][SOLVED] = data['zonemapsave'][0]['b4']
        zonemap['c1'][SOLVED] = data['zonemapsave'][0]['c1']
        zonemap['c2'][SOLVED] = data['zonemapsave'][0]['c2']
        zonemap['c3'][SOLVED] = data['zonemapsave'][0]['c3']
        zonemap['c4'][SOLVED] = data['zonemapsave'][0]['c4']
        zonemap['d1'][SOLVED] = data['zonemapsave'][0]['d1']
        zonemap['d2'][SOLVED] = data['zonemapsave'][0]['d2']
        zonemap['d3'][SOLVED] = data['zonemapsave'][0]['d3']
        zonemap['d4'][SOLVED] = data['zonemapsave'][0]['d4'] 
        if ironarmor == True:
            if myPlayer.job == 'warrior':
                myPlayer.hp = 10
            if myPlayer.job == 'mage':
                myPlayer.hp = 9
            if myPlayer.job == 'priest':
                myPlayer.hp = 8 
        elif copperarmor == True:
            if myPlayer.job == 'warrior':
                myPlayer.hp = 11
            if myPlayer.job == 'mage':
                myPlayer.hp = 10
            if myPlayer.job == 'priest':
                myPlayer.hp = 9 
        elif steelarmor == True:
            if myPlayer.job == 'warrior':
                myPlayer.hp = 12
            if myPlayer.job == 'mage':
                myPlayer.hp = 11
            if myPlayer.job == 'priest':
                myPlayer.hp = 10
        elif ironsword == True:
            if myPlayer.job == 'warrior':
                myPlayer.atk = 4
            if myPlayer.job == 'mage':
                myPlayer.atk = 4
            if myPlayer.job == 'priest':
                myPlayer.atk = 4 
        elif coppersword == True:
            if myPlayer.job == 'warrior':
                myPlayer.atk = 5
            if myPlayer.job == 'mage':
                myPlayer.atk = 5
            if myPlayer.job == 'priest':
                myPlayer.atk = 5
        elif steelsword == True:
            if myPlayer.job == 'warrior':
                myPlayer.atk = 6
            if myPlayer.job == 'mage':
                myPlayer.atk = 6
            if myPlayer.job == 'priest':
                myPlayer.atk = 6 
        elif arcanebook == True:
            if myPlayer.job == 'warrior':
                myPlayer.mpatk = 5
            if myPlayer.job == 'mage':
                myPlayer.mpatk = 5
            if myPlayer.job == 'priest':
                myPlayer.mpatk = 6 
        elif masterbook == True:
            if myPlayer.job == 'warrior':
                myPlayer.mpatk = 6
                myPlayer.mp = 3 
            if myPlayer.job == 'mage':
                myPlayer.mpatk = 6 
                myPlayer.mp = 5
            if myPlayer.job == 'priest':
                myPlayer.mpatk = 7
                myPlayer.mp = 7
        else:
            if 'warrior' in myPlayer.job:
                myPlayer.hp = 9
                myPlayer.mp = 3
                myPlayer.atk = 3
                myPlayer.mpatk = 4
            if 'mage' in myPlayer.job:
                myPlayer.hp = 8
                myPlayer.mp = 4
                myPlayer.atk = 3
                myPlayer.mpatk = 4
            if 'priest' in myPlayer.job:
                myPlayer.hp = 7
                myPlayer.mp = 6
                myPlayer.atk = 3
                myPlayer.mpatk = 5
            myPlayer.hp += lvhp 
            myPlayer.mp += lvmp
            myPlayer.atk += lvatk
            myPlayer.mpatk += lvmpatk
            oldlv == lv            
    except Exception as e:
        print(str(e))
        print('No save file found.')
        title_screen()
    

def savegame():
    data = {}
    data['player'] = []
    data['player'].append({
        'name' : myPlayer.name,
        'job' : myPlayer.job,
        'hp' : myPlayer.hp,
        'mp' : myPlayer.mp,
        'atk' : myPlayer.atk,
        'mpatk' : myPlayer.mpatk,
        'money' : myPlayer.money,
        'location' : myPlayer.location,
        'lv' : lv,
        'lvhp' : lvhp, 
        'lvmp' : lvmp,  
        'lvatk' : lvatk,
        'lvmpatk' : lvmpatk,
        'xp' : xp
    })
    data['shop'] = []
    data['shop'].append({
        'ironsword' : ironsword,
        'ironarmor' : ironarmor,
        'coppersword' : coppersword,
        'copperarmor' : copperarmor,
        'steelsword' : steelsword,
        'steelarmor' : steelarmor,        
        'arcanebook' : arcanebook,
        'masterbook' : masterbook,


    })
    data['zonemapsave'] = []
    data['zonemapsave'].append({
        'a1' : zonemap['a1'][SOLVED],
        'a2' : zonemap['a2'][SOLVED],
        'a3' : zonemap['a3'][SOLVED],
        'a4' : zonemap['a4'][SOLVED],
        'b1' : zonemap['b1'][SOLVED],
        'b2' : zonemap['b2'][SOLVED],
        'b3' : zonemap['b3'][SOLVED],
        'b4' : zonemap['b4'][SOLVED],
        'c1' : zonemap['c1'][SOLVED],
        'c2' : zonemap['c2'][SOLVED],
        'c3' : zonemap['c3'][SOLVED],
        'c4' : zonemap['c4'][SOLVED],
        'd1' : zonemap['d1'][SOLVED],
        'd2' : zonemap['d2'][SOLVED],
        'd3' : zonemap['d3'][SOLVED],
        'd4' : zonemap['d4'][SOLVED],
    })

    with open('savegame.txt','w') as outfile:
        json.dump(data, outfile)



def help_menu():
    print('############################')
    print('#Welcome To The Text RPG!  #')
    print('############################')
    print('-Use the \'move\'to move   #')
    print('-Use Commands to interact  #')
    print('-Like /" Look/" to inspect.#')
    print('#        Have Fun!         #')
    print('############################')
    title_screen_selections()

 ##### Gameplay Programming #####

#shop
def shop(): 
    global ironsword
    global ironarmor
    global coppersword
    global copperarmor
    global steelsword
    global steelarmor
    global arcanebook
    global masterbook
    if myPlayer.money < 25:
        print('you do not have enough money. go to the park and examine to get 25 money. (only can be done 1 time per game.)')
    print('ironsword = 25    ironarmor = 50\n    coppersword = 150    copperarmor = 150\n   steelsword = 500   steelarmor = 500\n arcanebook = 75 masterbook = 225')
    print('you have')
    print(myPlayer.money)
    buy = input('> ')
    if buy == 'ironsword' and myPlayer.money >= 25:
        ironsword = True
        coppersword = False
        steelsword = False
        myPlayer.money -= 25
    elif buy == 'ironarmor' and myPlayer.money >= 50:
        ironarmor = True
        copperarmor = False
        steelarmor = False 
        myPlayer.money -= 50
    elif buy == 'coppersword' and myPlayer.money >= 150: 
        ironsword = False
        coppersword = True
        steelsword = False 
        myPlayer.money -= 150
    elif buy == 'copperarmor' and myPlayer.money >= 150:
        ironarmor = False
        copperarmor = True
        steelarmor = False 
        myPlayer.money -= 150
    elif buy == 'steelsword' and myPlayer.money >= 500:
        ironsword = False
        coppersword = False
        steelsword = True 
        myPlayer.money -= 500
    elif buy == 'steelarmor' and myPlayer.money >= 500:    
        ironarmor = False
        copperarmor = False
        steelarmor = True
        myPlayer.money -= 500
    elif buy == 'arcanebook' and myPlayer.money >= 75:
        arcanebook = True
        masterbook = False
        myPlayer.money -= 75
    elif buy == 'masterbook' and myPlayer.money >= 225:    
        masterbook = True
        arcanebook = False
        myPlayer.money -= 225
    while buy not in ['ironsword', 'ironarmor', 'coppersword', 'copperarmor', 'steelsword', 'steelarmor', 'arcanebook', 'masterbook']:
        print('please enter a valid item. type a valid item name')
        buy = input('> ')
        if buy == 'ironsword' and myPlayer.money >= 25:
            ironsword = True
            coppersword = False
            steelsword = False
            myPlayer.money -= 25
        elif buy == 'ironarmor' and myPlayer.money >= 50:
            ironarmor = True
            copperarmor = False
            steelarmor = False 
            myPlayer.money -= 50
        elif buy == 'coppersword' and myPlayer.money >= 150: 
            ironsword = False
            coppersword = True
            steelsword = False 
            myPlayer.money -= 150
        elif buy == 'copperarmor' and myPlayer.money >= 150:
            ironarmor = False
            copperarmor = True
            steelarmor = False 
            myPlayer.money -= 150
        elif buy == 'steelsword' and myPlayer.money >= 500:
            ironsword = False
            coppersword = False
            steelsword = True 
            myPlayer.money -= 500
        elif buy == 'steelarmor' and myPlayer.money >= 500:    
            ironarmor = False
            copperarmor = False
            steelarmor = True
            myPlayer.money -= 500
        elif buy == 'arcanebook' and myPlayer.money >= 75:
            arcanebook = True
            masterbook = False 
            myPlayer.money -= 75
        elif buy == 'masterbook' and myPlayer.money >= 225:    
            masterbook = True
            arcanebook = False
            myPlayer.money -= 225 
    if ironarmor == True:
        if myPlayer.job == 'warrior':
            myPlayer.hp = 10
        if myPlayer.job == 'mage':
            myPlayer.hp = 9
        if myPlayer.job == 'priest':
            myPlayer.hp = 8 
    elif copperarmor == True:
        if myPlayer.job == 'warrior':
            myPlayer.hp = 11
        if myPlayer.job == 'mage':
            myPlayer.hp = 10
        if myPlayer.job == 'priest':
            myPlayer.hp = 9 
    elif steelarmor == True:
        if myPlayer.job == 'warrior':
            myPlayer.hp = 12
        if myPlayer.job == 'mage':
            myPlayer.hp = 11
        if myPlayer.job == 'priest':
            myPlayer.hp = 10
    elif ironsword == True:
        if myPlayer.job == 'warrior':
            myPlayer.atk = 4
        if myPlayer.job == 'mage':
            myPlayer.atk = 4
        if myPlayer.job == 'priest':
            myPlayer.atk = 4 
    elif coppersword == True:
        if myPlayer.job == 'warrior':
            myPlayer.atk = 5
        if myPlayer.job == 'mage':
            myPlayer.atk = 5
        if myPlayer.job == 'priest':
            myPlayer.atk = 5
    elif steelsword == True:
        if myPlayer.job == 'warrior':
            myPlayer.atk = 6
        if myPlayer.job == 'mage':
            myPlayer.atk = 6
        if myPlayer.job == 'priest':
            myPlayer.atk = 6 
    elif arcanebook == True:
        if myPlayer.job == 'warrior':
            myPlayer.mpatk = 5
        if myPlayer.job == 'mage':
            myPlayer.mpatk = 5
        if myPlayer.job == 'priest':
            myPlayer.mpatk = 6 
    elif masterbook == True:
        if myPlayer.job == 'warrior':
            myPlayer.mpatk = 6
            myPlayer.mp = 3 
        if myPlayer.job == 'mage':
            myPlayer.mpatk = 6 
            myPlayer.mp = 5
        if myPlayer.job == 'priest':
            myPlayer.mpatk = 7
            myPlayer.mp = 7
    else:
        if 'warrior' in myPlayer.job:
            myPlayer.hp = 9
            myPlayer.mp = 2
            myPlayer.atk = 3
            myPlayer.mpatk = 4
        if 'mage' in myPlayer.job:
            myPlayer.hp = 8
            myPlayer.mp = 4
            myPlayer.atk = 3
            myPlayer.mpatk = 4
        if 'priest' in myPlayer.job:
            myPlayer.hp = 7
            myPlayer.mp = 6
            myPlayer.atk = 3
            myPlayer.mpatk = 5
        
        
 #map
ZONENAME = ''
DESCRIPTION = 'descriptio'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'up', 'west'
RIGHT = 'up', 'east'
a1 = 'p'
a2 = 'p'
a3 = 'p'
a4 = 'p'
b1 = 'p'
b2 = 'p'
b3 = 'p'
b4 = 'p'
c1 = 'p'
c2 = 'p'
c3 = 'p'
c4 = 'p'
d1 = 'p'
d2 = 'p'
d3 = 'p'
d4 = 'p'
    
solved_places = {'a1': False,'a2': False,'a3': False,'a4': False,
                     'b1': False, 'b2': False,'b3': False,'b4': False,
                     'c1': False,'c2': False,'c3': False,'c4': False,
                     'd1': False, 'd2': False,'d3': False,'d4': False,}
#zone info
zonemap = {
    'a1':{ZONENAME: 'Town Market', DESCRIPTION: 'you can buy stuff here.', EXAMINATION: 'Welcome to the shop.', SOLVED: False, UP: 'a1', DOWN: 'b1', LEFT: 'a1',  RIGHT: 'a2'},
    'a2':{ZONENAME: 'Town Entrance', DESCRIPTION: 'People Live and Work here.', EXAMINATION: 'you see a building.', SOLVED: False, UP: 'a2', DOWN: 'b2', LEFT: 'a1', RIGHT: 'a3'},
    'a3':{ZONENAME: 'Town Park', DESCRIPTION: 'People relax here.', EXAMINATION: 'You find 25 money in the leaves.', SOLVED: False, UP: 'a3', DOWN: 'b3', LEFT: 'a2', RIGHT: 'a4'},
    'a4':{ZONENAME: 'Town Hall', DESCRIPTION: 'The Mayor Lives here.', EXAMINATION: 'Private Property...', SOLVED: False, UP: 'a4', DOWN: 'b4', LEFT: 'a3', RIGHT: 'a4'},
    'b1':{ZONENAME: 'Plains', DESCRIPTION: 'Just a boring plains', EXAMINATION: 'examine', SOLVED: False, UP: 'a1', DOWN: 'c1', LEFT: 'b1', RIGHT: 'b2'}, 
    'b2':{
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your Home',
        EXAMINATION: 'Still feels like Home.(Nothing has changed.)',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3':{
        ZONENAME: 'Desert',
        DESCRIPTION: 'Just a boring desert',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4':{
        ZONENAME: 'Woods',
        DESCRIPTION: 'Just a boring forest.',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4', 
        LEFT: 'b3',
        RIGHT: 'b4',
    },
    'c1':{
        ZONENAME: 'Very easy',
        DESCRIPTION: 'Very easy',
        EXAMINATION: 'you have entered a fight.',
        SOLVED: False,
        UP: 'b1', 
        DOWN :'d1',
        LEFT: 'c1', 
        RIGHT: 'c2'
    },
    'c2':{
        ZONENAME: 'Very easy',
        DESCRIPTION :'Very easy',
        EXAMINATION: 'you have entered a fight.',
        SOLVED: False,
        UP: 'b2', 
        DOWN: 'd2', 
        LEFT: 'c1',
        RIGHT: 'c3'
    },
    'c3':{
        ZONENAME: 'easy',
        DESCRIPTION: 'easy',
        EXAMINATION: 'you have entered a fight.',
        SOLVED: False,
        UP: 'b3', 
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4'
    },    
    'c4':{
        ZONENAME: 'easy',
        DESCRIPTION: 'easy',
        EXAMINATION: 'you have entered a fight.',
        SOLVED: False,
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: 'c4',
    },
    'd1':{
        ZONENAME: 'normal',
        DESCRIPTION: 'normal',
        EXAMINATION: 'you have entered a fight.',
        SOLVED: False,
        UP: 'c1',
        DOWN: 'd1', 
        LEFT: 'd1',
        RIGHT: 'd2'
    },
    'd2':{
        ZONENAME: 'normal',
        DESCRIPTION: 'normal',
        EXAMINATION: 'you have entered a fight.',
        SOLVED: False,
        UP: 'c2',
        DOWN: 'd2',
        LEFT: 'd1',
        RIGHT: 'd3'
    },
    'd3':{
        ZONENAME: 'hard',
        DESCRIPTION: 'hard',
        EXAMINATION: 'you have entered a fight.',
        SOLVED: False,
        UP: 'c3',
        DOWN: 'd3',
        LEFT: 'd2',
        RIGHT: 'd4'
    },
    'd4':{
        ZONENAME: 'Beat To win!',
        DESCRIPTION: 'Very hard...',
        EXAMINATION: 'you have entered your FINAL fight. heheheheheh....',
        SOLVED: False,
        UP: 'c4',
        DOWN: 'd4',
        LEFT: 'd3',
        RIGHT: 'd4', 
        }}
    
#game interactivity
#combat
def fight(enemymaxhp,enemyatk,enemymagicatk,moneyearned,finalboss,xp_earned):
    global xp
    enemyhp = enemymaxhp
    yourhp = myPlayer.hp
    mp = myPlayer.mp
    print('you can choose to attack with \'attack\' and \'magic\' you will waste your turn if you use magic but dont have 2 mana') 
    while not yourhp < 1 and not enemyhp < 1:
        print('you ' + '#' * yourhp + 'your mana ' + '#' * mp + 'enemy ' + '#' * enemyhp) 
        doneattack = input('> ')
        if doneattack == 'attack':
            enemyhp = (enemyhp - myPlayer.atk)     
        elif doneattack == 'magic' and mp >= 2:
            enemyhp = (enemyhp - myPlayer.mpatk)
            mp = (mp - 2)
        while doneattack not in ['attack', 'magic']:
            doneattack = input('> ')
            if doneattack == 'attack':
                enemyhp = (enemyhp - myPlayer.atk)    
            elif doneattack == 'magic' and mp >= 2:
                enemyhp = (enemyhp - myPlayer.mpatk)
                mp = (mp - 2)
        randomvar = random.randint(1,3)    
        randomvar2 = random.randint(1,3)
        if randomvar2 == 1:
            enemyrandatk = enemymagicatk
        else:
            enemyrandatk = enemyatk
        yourhp = (yourhp - enemyrandatk)
        if mp < myPlayer.mp and randomvar == 1:
             mp = 1 + mp
    if enemyhp < 1: #beat the enemy
        myPlayer.money = moneyearned + myPlayer.money
        xp += xp_earned
    if finalboss == 1 and enemyhp < 1:
        print('You have Saved this world. Go on to do good. ')
        sys.exit()
    if yourhp < 1:
        print('GAME OVER...')
        sys.exit()

def print_location():
    print('\n' +('#' * (4 + len(myPlayer.location))))
    print('# you have #')
    print(myPlayer.money)
    print('#' + myPlayer.location.upper() + '#')
    print('#' + zonemap[myPlayer.location][ZONENAME] + '#')
    print('#' + zonemap[myPlayer.location][DESCRIPTION] + '#')
    print('\n' +('#' * (4 + len(myPlayer.location))))

def prompt():
    global oldlv
    global lv
    global lvhp
    global lvmp
    global lvatk
    global lvmpatk
    print('\n' + '===============================')
    print('you can move, look, REDACTED and levelstats') 
    action = input('> ')
    acceptable_actions = ['move', 'go', 'walk', 'leave', 'examine', 'interact', 'look', 'debugwwssadad', 'levelstats']
    while action.lower() not in acceptable_actions:
        print('unknown action, try again')
        action = input('> ')
    if action.lower() == 'leave':
        savegame()
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'interact', 'look']:
        player_examine(action.lower())
    elif action.lower() == 'debugwwssadad':
        myPlayer.money = 9001
        lv = 5
    elif action.lower() == 'levelstats':
        sparelv = lv - oldlv
        print('You are at')
        print(lv)
        print('levels')
        print('you have')
        print(sparelv) 
        print('free')
        lvbuy = input('what do you want to get (health, mana, attack and magic_attack)')
        if lvbuy == 'health' and sparelv >= 1:
            myPlayer.hp += lvhp
            sparelv -= 1
        elif lvbuy == 'mana' and sparelv >= 1:
            myPlayer.mp += lvmp
            sparelv -= 1
        elif lvbuy == 'attack' and sparelv >= 1:
            myPlayer.atk += lvatk
            sparelv -= 1
        elif lvbuy == 'magic_attack' and sparelv >= 1:
            myPlayer.mpatk += lvmpatk
            sparelv -= 1
        elif sparelv == 0:
            print('level up dangit! you NOOB.')
        oldlv = lv - sparelv

def player_move(myAction):
    print(' 1 2 3 4')
    print(' _ _ _ _')
    print('|_|_|_|_|a')
    print('|_|_|_|_|b')
    print('|_|_|_|_|c')
    print('|_|_|_|_|d \n')
    ask = 'where would you like to move to? (you start at b2 and you can go north,south,east&west )\n'
    dest = input(ask)
    if dest == 'north':
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest == 'south':
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest == 'east':
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest == 'west':
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
        
def movement_handler(destination):
    print('\n' + 'you have moved to ' + destination + '.')
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print('Welp, Been there done that')
    elif myPlayer.location == 'a1':
       print (zonemap[myPlayer.location][EXAMINATION]) 
       shop()
    elif myPlayer.location == 'a3' and zonemap['a3'][SOLVED] == False:
        myPlayer.money = 25 + myPlayer.money
        zonemap[myPlayer.location][SOLVED] = True
    elif myPlayer.location == 'c1' or myPlayer.location == 'c2':
        fight(8,2,3,30,0,5)
    elif myPlayer.location == 'c3' or myPlayer.location == 'c4':
        fight(9,2,3,40,0,7)
    elif myPlayer.location == 'd1' or myPlayer.location == 'd2':
        fight(9,3,4,30,0,9)
    elif myPlayer.location == 'd3':
        fight(10,3,5,30,0,11) 
    elif myPlayer.location == 'd4':
        fight(11,5,6,30,1,0)
    else:
        print(zonemap[myPlayer.location][EXAMINATION])

#game functionality



def main_game_loop():
    global xp
    global lv
    while myPlayer.game_over is False:
        prompt()
        if xp == 20 and lv == 1:
            lv +=1
            xp = 0
        elif xp == 30 and lv == 2:
            lv +=1
            xp = 0
        elif xp == 50 and lv == 3:
            lv +=1
            xp = 0
        elif xp == 80 and lv == 4:
            lv +=1 
    else:
        sys.exit()

def setup_game():
    os.system('clear')
    #name collecting
    question1 = "Hello what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    player_name = input('> ')
    myPlayer.name = player_name
    #job collecting
    question2 = "Hello what role do you want to play?\n"
    question2added = "you can play as a warrior mage or priest.\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input('> ')
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job in valid_jobs:
        myPlayer.job = player_job
        print('you are now a' + player_job)
    while player_job not in valid_jobs:
       player_job = input('> ')
    myPlayer.job = player_job 
    #player stats
    if 'warrior' in myPlayer.job:
        myPlayer.hp = 9
        myPlayer.mp = 3
        myPlayer.atk = 3
        myPlayer.mpatk = 4
    if 'mage' in myPlayer.job:
        myPlayer.hp = 8
        myPlayer.mp = 4
        myPlayer.atk = 3
        myPlayer.mpatk = 4
    if 'priest' in myPlayer.job:
        myPlayer.hp = 7
        myPlayer.mp = 6
        myPlayer.atk = 3
        myPlayer.mpatk = 5
    #intro to game
    question3 = 'Welcome, ' + player_name + 'the' + myPlayer.job + '\n'
    print(question3)
    os.system('clear')
    print('######################')
    print("#  Let's Start Now!  #")
    print('######################')
    main_game_loop()

title_screen()   


print('You have Saved this world. Go on to do good. ')
    
        
        
        
    

