import random
import time
import requests, json, sys, pprint, contextlib
myResults = [] # Empty myResults list to begin
global name
global villain
global powers
villain = ['Alastor', 'Odon', 'Zilla', 'Kasdeva', 'Thamish', 'Daegal', 'Horay']
powers = ['mind-control', 'shape-shifting', 'acid/poison', 'electricity', 'flight', 'speed', 'superstrength', 'energy', 'forcefields', 'invisibility', 'gravity', 'super-intelligence', 'illusions', 'radiation']
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

def checkDoor():
    print('It\'s your job to meet with the villain..')
    time.sleep(2)
    print('They\'ve invited you to their lair...')
    time.sleep(2)
    print('And now it\'s time to earn your chance to fight..')
    time.sleep(2)

def guessJoke():
    print('Here is the joke..')
    url = f'https://official-joke-api.appspot.com/random_joke' # Random Joke API url
    response = requests.get(url) # Receiving your request from the API
    response.raise_for_status() # Check for errors

    jokeData = json.loads(response.text)
    content = jokeData['setup'] # Pulling only the setup for the joke from the result
    print(content) # Print setup
    myResults.append(content) # Adding results to myResults list

    print('Type in your guess.')
    guess = input()
    content2 = jokeData['punchline']  # Pulling only the setup for the joke from the result
    if(guess == content2):
        print('You were correct! Great guess!')
        return True
        myResults.append(content2)  # Adding results to myResults list
    else:
        print('You tried! The real answer was: ' + content2)
        return False
        myResults.append(content2)  # Adding results to myResults list


while True:
    print('''Welcome to World War 2020, an interactive game where you get to create your own
character based on one of four types of super powers: fire, air, water, and earth.
What is your name?''')
    name = input()
    print('''Thanks, ''' + name + '''. What type of character would you like to create?
Fire (f), Water (w), Earth (e) or Air (a)?''')
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
            print(''' 1.) Bondi Beach, Sydney, Australia
           2.) The Rainforest, Ranomafana, Madagascar
           3.) The Port, Dakar, Senegal
           4.) The Glacier, El Chalten, Argentina
           5.) The Eifel Tower, Paris, France
           6.) Santa Cruz Islanda, Galapagos, Ecuador
           7.) The Gobi Desert, Southern Mongolia''')
    if(choice == '1'):
        villain = villain[0]
        powers1 = powers[0]
        powers2 = powers[1]
        print('Welcome to Sydney. The beach has been destroyed by a villain, named '+ villain+ ', who\'s primary powers are ' + powers1 + ' and ' + powers2 +'.')
    elif(choice == '2'):
        villain = villain[1]
        powers1 = powers[2]
        powers2 = powers[3]
        print('Welcome to Madagascar. Most of the animals & trees in the Rainforest have died because of a villain named '+ villain+ ', for his powers include ' + powers1 + ' and ' + powers2 +'.')
    elif(choice == '3'):
        villain = villain[2]
        powers1 = powers[4]
        powers2 = powers[5]
        print('Welcome to Senegal. The port has been transformed into the villain, ' + villain+ '\'s lair, and his powers include ' + powers1 + ' and ' + powers2 +'.')
    elif(choice == '4'):
        villain = villain[3]
        powers1 = powers[6]
        powers2 = powers[7]
        print('Welcome to Argentina. The Glacier has almost melted away because of the villain, '+ villain+ ', and her powers include ' + powers1 + ' and ' + powers2 +'.')
    elif(choice == '5'):
        villain = villain[4]
        powers1 = powers[8]
        powers2 = powers[9]
        print('Welcome to Paris. The Eifel Tower is one of the last monuments left standing in Paris because of the villain, '+ villain+', and his powers include ' + powers1 + ' and ' + powers2 +'.')
    elif(choice == '6'):
        villain = villain[5]
        powers1 = powers[10]
        powers2 = powers[11]
        print('Welcome to Ecuador. The islands have almost diminished because of the villain, '+ villain+', and his powers include ' + powers1 + ' and ' + powers2 +'.')
    elif(choice == '7'):
        villain = villain[6]
        powers1 = powers[12]
        powers2 = powers[13]
        print('Welcome to the Gobi Desert. The Desert has been reaching deathly temperatures because of the villain, '+ villain+', and his powers include ' + powers1 + ' and ' + powers2 +'.')
    checkDoor()
    print('''Guess the joke correctly and you\'ll have automatically conquered ''' + villain +'''. Otherwise, you must battle. 
Would you like to continue? (y or n)''')
    answer = input()
    while(answer != 'y' and answer != 'n'):
        print('That was not an option. Please type \'y\' to proceed with the joke or \'n\'.')
        answer = input()
    if(guessJoke() == True):
        #if they get the answer right, they immediately conquer the villain
        print('You have destroyed' + villain +', without needing to use your powers.')
    else:
        #they didn't guess the answer to the joke
        print('''Oh no. Your failed attempt has angered '''+villain+'''. They take a threatening stance, directed at you.
It seems as though you will have to fight them. Your powers are ''' + player.powers[0] + '[1], ' + player.powers[1] + '[2], ' + player.powers[2]+ '[3]'''''. 
Which attack would you like to use?''')
    attack = input()
    if (attack == '1') or (attack == '3'):
        print('''Oh no! '''+villain+ ''' hit you with ''' + powers1 + '''. Remember you only have three lives..
Your power level lowered by 1. Try another attack! (1, 2, or 3)''')
        attack2 = input()
        if attack2 == '1' or '2' or '3':
            print('''Nice! ''' + villain + '''\'s power level went down by 10 points.
Would you like to choose a different attack (d) or stay with these 3 options (s)?''')
        next = input()
        if next == 'd':
            print('''What type of character would you like to create?
Fire (f), Water (w), Earth (e) or Air (a)?''')
            type = input()
            player = hero()
            createCharacter(player, choice)
        if next == 's':
            print('Your powers are ''' + player.powers[0] + '[1], ' + player.powers[1] + '[2], ' + player.powers[2]+ '[3]''''. 
Which attack would you like to use?''')
            attack3 = input()
            if attack3 == '2':
                print('Nice! You lowered' +villain+ '\'s power level. Hit them again? (y or n)')

    if (attack == '2'):
        print('Good choice.. ' + villain +' took the hit.. Try another attack to finish him off!')

    break



