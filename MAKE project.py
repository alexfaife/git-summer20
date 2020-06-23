import random
import time

class hero:
    def __init__(self):
        self.health = 100
        self.type = ''
        self.power = ''
        self.powers = []
        self.powerLevel = []


def powerLevels(character):
    for x in range (0, 3):
        character.powerLevel.append(random.randint(1,101))

def choosePowers(character, style):
    if(style == 'l'):
        character.power = 'long'
        character.powers.append(character.type + 'throw')
        character.powers.append(character.type + 'wall')
        character.powers.append(character.type + 'bomb')
    else:
        character.power = 'close'
        character.powers.append(character.type + 'punch')
        character.powers.append(character.type + 'jab')
        character.powers.append(character.type + 'flip')

    powerLevels(character)

def createCharacter(character, type):
    if(type == 'f'):
        character.type = 'fire'
    elif(type == 'w'):
        character.type = 'water'
    elif(type == 'e'):
        character.type = 'earth'
    else:
        character.type = 'air'
    print('What type of power specialty would you like? Long defence (l) or close defence (c)? ')
    choice = input()
    while(choice != 'l' and choice != 'c'):
        print('That was not an option. Please type long defence (l) or close defence (c).')
        choice = input()
    choosePowers(character, choice)

while True:
    print('''Welcome to Heroes Online, an interactive game where you get to create your own
character based on one of four types of super powers: fire, air, water, and earth.
What is your name?''')
    name = input()
    print('''Thanks, ''' + name + '''. What type of character would you like to create?
Fire (f), water (w), earth (e) or air (a)?''')
    player = hero()
    choice = input()
    while((choice != 'f' and choice != 'w') and (choice != 'e' and choice != 'a')):
        print('That was not an option. Please type fire (f), water (w), earth (e) or air (a)')
        choice = input()

    createCharacter(player, choice)
    print('What would you like to name you character? Remember, they have ' + player.type + ' powers with ' + player.power + ' range'
            ' abilities')
    charName = input()
    print('Now the game will begin.')
    time.sleep(2)
    print('''Your name is ''' + charName + ''' and you are a super hero with ''' + player.type +
          ''' powers. These powers include ''' + player.powers[0] + ', ' +  player.powers[1] + ', ' + player.powers[2] +
          '''. 
You live in what used to be Boca Raton, Florida. But now, it is overtaken with distress and demolition. The source is
villains who have taken over 7 various environmental locations around the world. It is up to
you to decide where to strike first. Here are the options:
1.) Bondi Beach, Sydney, Australia
2.) The Rainforest, Ranomafana, Madagascar
3.) The Port, Dakar, Senegal
4.) The Glacier, El Chalten, Argentina
5.) The Eifel Tower, Paris, France
6.) Santa Cruz Islanda, Galapagos, Ecuador
7.) The Gobi Desert, Southern Mongolia''')
    choice = input()
    while(choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6' and choice != '7'):
        print("That was not an option. Please indicate your choice with a number 1-7 or type 'i' to repeat the options")
        choice = input()
        if(choice == 'i'):
            print(''' 1.) The Beach, Sydney, Australia
           2.) The Rainforest, Ranomafana, Madagascar
           3.) The Port, Dakar, Senegal
           4.) The Glacier, El Chalten, Argentina
           5.) The Eifel Tower, Paris, France
           6.) Santa Cruz Islanda, Galapagos, Ecuador
           7.) The Gobi Desert, Southern Mongolia''')
    if(choice == '1'):
        print('The beach has been destroyed by a villain, named Alastor, who\'s primary powers are mind-control and shapeshifting.')
    if(choice == '2'):
        print('Most of the animals & trees in the Rainforest have died because of a villain named Odon, for his powers include acid/poison and electricity')
    if(choice == '3'):
        print('The port has been transformed into the villain, Zilla\'s lair, and his powers include flight and speed.')
    if(choice == '4'):
        print('The Glacier has almost melted away because of the villain, Kasdeya, and her powers include superstrength and energy.')
    if(choice == '5'):
        print('The Eifel Tower is one of the last monuments left standing in Paris because of the villain, Thamish, and his powers include forcefields and invisibility.')
    if(choice == '6'):
        print('The islands have almost diminished because of the villain, Daegal, and his powers include gravity and super-intelligence,')
    if(choice == '7'):
        print('The Desert has been reaching deathly temperatures becaue of the villain, Horay, and his powers include illusions and radiation.')
    if(choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7'):
        break

