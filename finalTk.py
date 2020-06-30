from tkinter import *
import random
import time
import requests, json, sys, pprint, contextlib
villain = ['Alastor', 'Odon', 'Zilla', 'Kasdeva', 'Thamish', 'Daegal', 'Horay' ]
powers = ['mind-control and shape-shifting', 'acid/poison and electricity', 'flight and speed',
          'superstrength and energy', 'forcefields and invisibility', 'gravity and super-intelligence',
          'illusions and radiation']

#file to be written in
file = open("jokes.txt", "w")

#global var defintions
counter = 1
name = ''
choice = ''
charName = ''
content2 =''
villainHealth = 100

#class definition for hero
class hero:
    def __init__(self):
        self.health = 100
        self.type = ''
        self.power = ''
        self.powers = []
        self.powerLevel = []


#text Definitions
text1 = '''Welcome to World War 2020, an interactive game where you get to create your own
character based on one of four types of super powers: fire, air, water, and earth.
What is your name?'''
text2 = '''It\'s your job to meet with the villain...
They\'ve invited you to their lair...
And now it\'s time to earn your chance to fight...
Guess the answer to this joke correctly and you\'ll have automatically conqured the villain. Otherwise, you must battle. 
Would you like to continue? (y or n)'''

#function definitions
def powerLevels(character):
    for x in range (0, 3):
        character.powerLevel.append(random.randint(40,80))

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
    choosePowers(character, choice)

def nameEntry():
    global name
    name = e.get()
    startButton.grid_remove()
    e.delete(0, END)
    top.set('''Thanks, ''' + name + '''. What type of character would you like to create?
Fire (f), water (w), earth (e) or air (a)?''')
    nameButton.grid(column= 3, columnspan = 1,row=5)

def setType():
    global choice
    choice = e.get()
    nameButton.grid_remove()
    createCharacter(player, choice)
    e.delete(0, END)
    top.set('What type of power specialty would you like? Long defence (l) or close defence (c)? ')
    typeButton.grid(column= 3, columnspan = 1,row=5)

def setName():
    global choice
    choice = e.get()
    typeButton.grid_remove()
    choosePowers(player, choice)
    e.delete(0, END)
    top.set('What would you like to name you character? Remember, they have ' + player.type + ' powers with ' + player.power + ' range abilities')
    gameBegins.grid(column= 3, columnspan = 1,row=5)

def gamePlay():
    global choice
    global charName
    choice = e.get()
    charName = choice
    e.delete(0, END)
    gameBegins.grid_remove()
    top.set('Now the game will begin.')
    top.set('''Your name is ''' + charName + ''' and you are a super hero with ''' + player.type +
''' powers. These powers include ''' + player.powers[0] + ', ' + player.powers[1] + ', ' + player.powers[2] +
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
    villainButton.grid(column= 3, columnspan = 1,row=5)

def villainChosen():
    global choice
    global villain
    global powers
    choice = e.get()
    e.delete(0, END)
    villainButton.grid_remove()
    if (choice == '1'):
        villain = villain[0]
        powers = powers[0]
        top.set('''Welcome to Sydney. The beach has been destroyed by a villain, named '''+ villain+
                ''', who\'s primary powers are ''' + powers + ''''.''')
    elif (choice == '2'):
        villain = villain[1]
        powers = powers[1]
        top.set( '''Welcome to Madagascar. Most of the animals & trees in the Rainforest have died because of a villain 
named ''' + villain + ' for his powers include' +  powers +'.')
    elif (choice == '3'):
        villain = villain[2]
        powers = powers[2]
        top.set('''Welcome to Senegal. The port has been transformed into the villain, ''' + villain + '''\'s lair, 
        and his powers include ''' +powers + '.')
    elif (choice == '4'):
        villain = villain[3]
        powers = powers[3]
        top.set('''Welcome to Argentina. The Glacier has almost melted away because of the villain,''' + villain+ ''', and her
powers include ''' + powers + '.')
    elif (choice == '5'):
        villain = villain[4]
        powers = powers[4]
        top.set('''Welcome to Paris. The Eifel Tower is one of the last monuments left standing in Paris because of the 
villain,''' + villain + ''' and his powers include ''' + powers + '.')
    elif (choice == '6'):
        villain = villain[5]
        powers = powers[5]
        top.set('''Welcome to Ecuador. The islands have almost diminished because of the villain,''' + villain + ''', and his powers 
include ''' + powers +'''.''')
    elif (choice == '7'):
        villain = villain[6]
        powers = powers[6]
        top.set('''Welcome to the Gobi Desert. The Desert has been reaching deathly temperatures because of the villain,''' + villain +
''' and his powers include ''' +  powers +'''.''')
    jokeQButton.grid(column= 3, columnspan = 1,row=5)
    e.grid_remove()

def jokeQ():
    global choice
    jokeQButton.grid_remove()
    top.set('''It\'s your job to meet with the villain...
They\'ve invited you to their lair...
And now it\'s time to earn your chance to fight...
Guess the answer to this joke correctly and you\'ll have automatically conqured ''' + villain +'''. Otherwise, you must battle. 
Would you like to continue? (y or n)''')
    e.grid(column=2, columnspan=2, row=4)
    jokeButton.grid(column= 3, columnspan = 1,row=5)

def jokeSetUp():
    global choice
    global content2
    choice = e.get()
    e.delete(0, END)
    jokeButton.grid_remove()
    if choice == 'y':
        url = f'https://official-joke-api.appspot.com/random_joke'  # Random Joke API url
        response = requests.get(url)  # Receiving your request from the API
        response.raise_for_status()  # Check for errors

        jokeData = json.loads(response.text)

        content = jokeData['setup']
        top.set('Here is the joke, give it your best guess: ' + content) #show the joke set up
        file.write('The joke is: ' + content)  # Adding results to myResults list

        content2 = jokeData['punchline']  # Pulling only the setup for the joke from the result
        file.write('The punchline is: ' + content2)  # Adding results to myResults list
        jokeAButton.grid(column=3, columnspan=1, row=5)
    if choice == 'n':
        noJoke()


def jokeAnswer():
    global choice
    choice = e.get()
    jokeAButton.grid_remove()
    e.delete(0, END)
    e.grid_remove()
    if content2 == choice:
        top.set('You have destroyed the villain without needing to use your powers')
    if content2 != choice:
        top.set('''Oh no. The answer was: ''' + content2 +'''. 
Your failed attempt has angered ''' + villain + '''. They take a threatening stance, directed at you.
It seems as though you will have to fight them. Your powers are ''' + player.powers[0] + '[1], ' + player.powers[
1] + '[2], ' + player.powers[2] + '''[3].
Which attack would you like to use?''')
    firstAttackButton.grid(column=2, padx = 50, pady = 50, columnspan=1, row=5)
    secondAttackButton.grid(column= 3, padx = 50, pady = 50, columnspan = 1, row = 5)
    thirdAttackButton.grid(column= 4, padx = 50, pady = 50, columnspan=1, row=5)

def noJoke():
    e.grid_remove()
    top.set('''It\'s your job to meet with the villain and they\'ve invited you to their lair...
And now it\'s time to earn your chance to fight...''' + villain + ''' takes a threatening stance directed at you. 
It seems as though you will have to fight them. Your powers are ''' + player.powers[0] + '[1], ' + player.powers[
1] + '[2], ' + player.powers[2] + '''[3].
Which attack would you like to use?''')
    firstAttackButton.grid(column=2, padx=50, pady=50, columnspan=1, row=5)
    secondAttackButton.grid(column=3, padx=50, pady=50, columnspan=1, row=5)
    thirdAttackButton.grid(column=4, padx=50, pady=50, columnspan=1, row=5)

def attack(level):
    global villainHealth
    e.grid_remove()
    newLevel = villainHealth - level
    villainHealth = newLevel
    if villainHealth <= 0:
        top.set('You have defeated ' + villain + '''. You are a hero in your land and will surely be called on to 
do more missions. Would you like to play again or quit?''')
        firstAttackButton.grid_remove()
        secondAttackButton.grid_remove()
        thirdAttackButton.grid_remove()
        again.grid(column=2, padx=50, pady=50, columnspan=1, row=5)
        quitGame.grid(column=4, padx=50, pady=50, columnspan=1, row=5)
    else:
        top.set('Nice! You\'ve hit ' + villain + 'with a power level of ' + str(level) + ' and their health is now ' + str(villainHealth) + '''.
They hit you back with their strongest attack. You are only able to take 3 hits, so only two more. 
Which attack would you like to use now?''')

def endGame():
    top.set('Congratulations, ' + charName + '! You saved the world from ' + villain + ''' with your battling skills. 
    Thank you for playing World War 2020. We\'re all forever grateful. Come back and play again!''')
    root.destroy()

def playAgain():
    global name
    e.delete(0,END)
    e.insert(0, name)
    again.grid_remove()
    quitGame.grid_remove()
    typeButton.grid(column=3, columnspan=1, row=5)

    nameEntry()

#window settings
root = Tk()
root.title("World War 2020")
width = root.winfo_screenwidth() // 2
height = root.winfo_screenheight() // 2
x = width - (height // 2)
y = height - (width // 2)
#edit height and width to change size of window
root.geometry('{}x{}+{}+{}'.format(width,height, x, y))

#this variable is the text string at the top of the screen
top = StringVar()
thing = Label(root, textvariable=top).grid(row =0, column=0, columnspan=4)
top.set(text1)

#this is the entry form for information choices
#it will be cleared each time the enter button is pressed
e = Entry(root, width=35,borderwidth=5)
e.grid(column =2, columnspan= 2, row=4)

#this is the creation of a the hero class
player = hero()

#this is the
#buttonLabel = StringVar()
#Button(root, textvariable = buttonLabel, command = nameEntry).pack()
startButton = Button(root, text ='Enter', command = nameEntry, fg = 'blue', bg = 'red')
startButton.grid(row=5, column= 3, columnspan = 1)
nameButton = Button(root, text='Enter', command=setType, fg='blue', bg='red')
typeButton = Button(root, text='Enter', command = setName, fg='blue', bg='red')
gameBegins = Button(root, text='Enter', command = gamePlay, fg='blue', bg='red')
villainButton = Button(root, text='Enter', command = villainChosen, fg='blue', bg='red')
jokeQButton = Button(root, text='Continue', command = jokeQ, fg='blue', bg='red')
jokeButton = Button(root, text='Enter', command = jokeSetUp, fg='blue', bg='red')
jokeAButton =  Button(root, text='Enter', command = jokeAnswer, fg='blue', bg='red')
firstAttackButton = Button(root, text= 'fire', command= lambda: attack(player.powerLevel[0]))
secondAttackButton = Button(root, text= 'fire2', command= lambda: attack(player.powerLevel[1]))
thirdAttackButton = Button(root, text= 'fire3', command= lambda: attack(player.powerLevel[2]))
quitGame = Button(root, text= 'Quit', command= endGame)
again = Button(root, text= 'Play Again', command= playAgain)


root.mainloop()


