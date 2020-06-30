from tkinter import *
from PIL import ImageTk, Image
import random
import time
import requests, json, sys, pprint, contextlib
villains = ['Alastor', 'Odon', 'Zilla', 'Kasdeva', 'Thamish', 'Daegal', 'Horay' ]
powers = ['mind-control and shape-shifting', 'acid/poison and electricity', 'flight and speed',
          'superstrength and energy', 'forcefields and invisibility', 'gravity and super-intelligence',
          'illusions and radiation']

#file to be written in
file = open("jokes.txt", "w")

#global var defintions
name = ''
choice = ''
charName = ''
content2 =''
villainHealth = 100
villain = ''

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
        character.powerLevel.append(random.randint(10,30))

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
        panel1.grid(row = 4, column = 0)
    elif(type == 'w'):
        character.type = 'water'
        panel2.grid(row = 4, column = 0)
    elif(type == 'e'):
        character.type = 'earth'
        panel4.grid(row = 4, column = 0)
    else:
        character.type = 'air'
        panel3.grid(row = 4, column = 0)
    choosePowers(character, choice)

def nameEntry():
    global name
    name = e.get()
    startButton.grid_forget()
    e.delete(0, END)
    top.set('''Thanks, ''' + name + '''. What type of character would you like to create?
Fire (f), water (w), earth (e) or air (a)?''')
    nameButton.grid(column= 0, row=3)

def setType():
    global choice
    global name
    choice = e.get()
    nameButton.grid_forget()
    if choice != 'f' and choice != 'e' and choice != 'w' and choice != 'a':
        e.delete(0, END)
        top.set('That was not an option. Please enter either f, e, w, or a to select your power type')
        nameButton.grid(column=0, row=3)
    else:
        nameButton.grid_forget()
        createCharacter(player, choice)
        e.delete(0, END)
        top.set('What type of power specialty would you like? Long defence (l) or close defence (c)? ')
        typeButton.grid(column= 0, row=3)

def setName():
    global choice
    choice = e.get()
    typeButton.grid_forget()
    if choice != 'l' and choice != 'c':
        e.delete(0, END)
        top.set('That was not an option. Please enter either l or c to choose your players attack range')
        typeButton.grid(column=0, row=3)
    else:
        choosePowers(player, choice)
        e.delete(0, END)
        top.set('What would you like to name you character? Remember, they have ' + player.type + ' powers with ' + player.power + ' range abilities')
        gameBegins.grid(column= 0, row=3)

def gamePlay():
    global choice
    global charName
    choice = e.get()
    charName = choice
    e.delete(0, END)
    gameBegins.grid_forget()
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
    villainButton.grid(column= 0,row=3)

def villainChosen():
    global choice
    global villains
    global powers
    global villain
    choice = e.get()
    e.delete(0, END)
    villainButton.grid_forget()
    #get rid of images of characters
    if (player.type == 'fire'):
        panel1.grid_remove()
    elif (player.type == 'water'):
        panel2.grid_remove()
    elif (player.type == 'earth'):
        panel4.grid_remove()
    else:
        panel3.grid_remove()

    if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6' and choice != '7':
        e.delete(0, END)
        top.set('That was not an option. Please enter a number 1 through 7 to select your villain location.')
        villainButton.grid(column=0, row=3)
    else:
        if (choice == '1'):
            villain = villains[0]
            powers = powers[0]
            top.set('''Welcome to Sydney. The beach has been destroyed by a villain, named '''+ villain+
''', who\'s primary powers are ''' + powers + ''''.''')
            vil1.grid(row=4, column=0)
        elif (choice == '2'):
            villain = villains[1]
            powers = powers[1]
            top.set( '''Welcome to Madagascar. Most of the animals & trees in the Rainforest have died because of a villain 
named ''' + villain + ' for his powers include' +  powers +'.')
            vil2.grid(row=4, column=0)
        elif (choice == '3'):
            villain = villains[2]
            powers = powers[2]
            top.set('''Welcome to Senegal. The port has been transformed into the villain, ''' + villain + '''\'s lair, 
and his powers include ''' +powers + '.')
            vil3.grid(row=4, column=0)
        elif (choice == '4'):
            villain = villains[3]
            powers = powers[3]
            top.set('''Welcome to Argentina. The Glacier has almost melted away because of the villain, ''' + villain+ ''', and her
powers include ''' + powers + '.')
            vil4.grid(row = 4, column = 0)
        elif (choice == '5'):
            villain = villains[4]
            powers = powers[4]
            top.set('''Welcome to Paris. The Eifel Tower is one of the last monuments left standing in Paris because of the 
villain, ''' + villain + ''' and his powers include ''' + powers + '.')
            vil5.grid(row=4, column=0)
        elif (choice == '6'):
            villain = villains[5]
            powers = powers[5]
            top.set('''Welcome to Ecuador. The islands have almost diminished because of the villain, ''' + villain + ''', and his powers 
include ''' + powers +'''.''')
            vil6.grid(row=4, column=0)
        elif (choice == '7'):
            villain = villains[6]
            powers = powers[6]
            top.set('''Welcome to the Gobi Desert. The Desert has been reaching deathly temperatures because of the villain, ''' + villain +
''' and his powers include ''' +  powers +'''.''')
            vil7.grid(row=4, column=0)
        jokeQButton.grid(column= 0,row=3)
        e.grid_forget()

def outputToFile():
    with open('WW2020.txt', 'a') as f: # Opens file named WW2020 to store myResults
        with contextlib.redirect_stdout(f): # Redirects myResults into file (WW2020.txt)
            print(myResults) # Prints/organizes myResults output into file (WW2020.txt)
                    
def jokeQ():
    global choice
    jokeQButton.grid_forget()
    top.set('''It\'s your job to meet with the villain...
They\'ve invited you to their lair...
And now it\'s time to earn your chance to fight...
Guess the answer to this joke correctly and you\'ll have automatically conquered ''' + villain +'''. Otherwise, you must battle. 
Would you like to continue? (y or n)''')
    e.grid(column=0 ,row=2)
    jokeButton.grid(column= 0,row=3)

def jokeSetUp():
    global choice
    global content2
    choice = e.get()
    e.delete(0, END)
    jokeButton.grid_forget()
    if choice != 'y' and choice != 'n':
        e.delete(0, END)
        top.set('That was not an option. Please enter either y or n to indicate your interest in trying a joke.')
        jokeButton.grid(column=0, row=3)
    else:
        if choice == 'y':
            url = f'https://official-joke-api.appspot.com/random_joke'  # Random Joke API url
            response = requests.get(url)  # Receiving your request from the API
            response.raise_for_status()  # Check for errors

            jokeData = json.loads(response.text)

            content = jokeData['setup']
            top.set('Here is the joke, give it your best guess: ' + content) #show the joke set up
            print(content) # Print setup
            myResults.append(content) # Adding results to myResults list

            content2 = jokeData['punchline']  # Pulling only the setup for the joke from the result
            print(content2)  # Print setup
            myResults.append(content2)  # Adding results to myResults list  # Adding results to myResults list
            jokeAButton.grid(column=0, row=3)
        if choice == 'n':
            noJoke()


def jokeAnswer():
    global choice
    global villain
    choice = e.get()
    jokeAButton.grid_forget()
    e.delete(0, END)
    e.grid_forget()
    if content2 == choice:
        top.set('You have destroyed the villain without needing to use your powers')
    if content2 != choice:
        top.set('''Oh no. The answer was: ''' + content2 +'''. 
Your failed attempt has angered ''' + villain + '''. They take a threatening stance, directed at you.
It seems as though you will have to fight them. Your powers are ''' + player.powers[0] + '[1], ' + player.powers[
1] + '[2], ' + player.powers[2] + '''[3].
Which attack would you like to use?''')
    firstAttackButton.grid(column=0, padx = 50, pady = 50,  row=3)
    secondAttackButton.grid(column= 1, padx = 50, pady = 50,  row = 3)
    thirdAttackButton.grid(column= 2, padx = 50, pady = 50,  row=3)

def noJoke():
    e.grid_forget()
    top.set('''It\'s your job to meet with the villain and they\'ve invited you to their lair...
And now it\'s time to earn your chance to fight...''' + villain + ''' takes a threatening stance directed at you. 
It seems as though you will have to fight them. Your powers are ''' + player.powers[0] + '[1], ' + player.powers[
1] + '[2], ' + player.powers[2] + '''[3].
Which attack would you like to use?''')
    firstAttackButton.grid(column=0, padx=50, pady=50, row=3)
    secondAttackButton.grid(column=1, padx=50, pady=50, row=3)
    thirdAttackButton.grid(column=2, padx=50, pady=50, row=3)

def removeVillain():
    global villain
    global villains
    if villain == villains[0]:
        vil1.grid_remove()
    elif villain == villains[1]:
        vil2.grid_remove()
    elif villain == villains[2]:
        vil3.grid_remove()
    elif villain == villains[3]:
        vil4.grid_remove()
    elif villain == villains[4]:
        vil5.grid_remove()
    elif villain == villains[5]:
        vil6.grid_remove()
    elif villain == villains[6]:
        vil7.grid_remove()

def attack(level):
    global villainHealth
    e.grid_forget()
    newLevel = villainHealth - level
    villainHealth = newLevel
    if villainHealth <= 0:
        top.set('You have defeated ' + villain + '''. You are a hero in your land and will surely be called on to 
do more missions. Would you like to play again or quit?''')
        removeVillain()
        firstAttackButton.grid_forget()
        secondAttackButton.grid_forget()
        thirdAttackButton.grid_forget()
        again.grid(column=0, padx=50, pady=50, row=3)
        quitGame.grid(column=2, padx=50, pady=50, row=3)
    elif player.health <= 0:
        removeVillain()
        top.set('You were defeated by ' + villain + '''. You are sent back to HQ to heal up but will not be invited
on another mission. Would you like to play again or quit?''')
        firstAttackButton.grid_forget()
        secondAttackButton.grid_forget()
        thirdAttackButton.grid_forget()
        again.grid(column=0, padx=50, pady=50, row=3)
        quitGame.grid(column=2, padx=50, pady=50, row=3)
    else:
        villainAttack = random.randint(5,20)
        newHealth = player.health - villainAttack
        player.health = newHealth
        top.set('Nice! You\'ve hit ' + villain + ' with a power level of ' + str(level) + ' and their health is now ' + str(villainHealth) + '''.
They hit you back with an attack that deals ''' + str(villainAttack) + ''' damage. Your health is now ''' + str(player.health) + ''' 
Which attack would you like to use now?''')


def endGame():
    top.set('Congratulations, ' + charName + '! You saved the world from ' + villain + ''' with your battling skills. 
    Thank you for playing World War 2020. We\'re all forever grateful. Come back and play again!''')
    root.destroy()

def playAgain():
    global name
    global choice
    e.delete(0,END)
    e.insert(0, name)
    again.grid_forget()
    quitGame.grid_forget()
    startButton.grid(column=0,row=3)
    e.grid(column=0, row=2)
    choice = ''
    nameEntry()

#window settings
root = Tk()
root.title("Gameplay Manager")
width = root.winfo_screenwidth() -400
height = root.winfo_screenheight() -200
x = 200
#edit height and width to change size of window
root.geometry('{}x{}+{}+{}'.format(width,height, x, 0))

#this is the title
title = Label(root, text= 'World War 2020',font = 'fixedsys 20 bold', fg = 'darkblue' )
title.grid(row=0, column=0)

#this variable is the text string at the top of the screen
top = StringVar()
thing = Label(root, textvariable=top).grid(row =1, column=0, columnspan=2)
top.set(text1)

#this is the entry form for information choices
#it will be cleared each time the enter button is pressed
e = Entry(root, width=35,borderwidth=5)
e.grid(column =0, row=2)

#this is the creation of a the hero class
player = hero()

#this is the
startButton = Button(root, text ='Enter', command = nameEntry, fg = 'blue')
startButton.grid(row=3, column= 0)
nameButton = Button(root, text='Enter', command=setType, fg='blue')
typeButton = Button(root, text='Enter', command = setName, fg='blue')
gameBegins = Button(root, text='Enter', command = gamePlay, fg='blue')
villainButton = Button(root, text='Enter', command = villainChosen, fg='blue')
jokeQButton = Button(root, text='Continue', command = jokeQ, fg='blue')
jokeButton = Button(root, text='Enter', command = jokeSetUp, fg='blue')
jokeAButton =  Button(root, text='Enter', command = jokeAnswer, fg='blue')
firstAttackButton = Button(root, text= 'attack 1', command= lambda: attack(player.powerLevel[0]), fg='blue')
secondAttackButton = Button(root, text= 'attack 2', command= lambda: attack(player.powerLevel[1]), fg='blue')
thirdAttackButton = Button(root, text= 'attack 3', command= lambda: attack(player.powerLevel[2]), fg='blue')
quitGame = Button(root, text= 'Quit', command= endGame, fg = 'red')
again = Button(root, text= 'Play Again', command= playAgain, fg = 'green')

#this is the images
fireImage = ImageTk.PhotoImage(Image.open("fire.gif"))
panel1 = Label(root, image= fireImage)
#panel1.grid(row = 4, column = 0)

waterImage = ImageTk.PhotoImage(Image.open("water.gif"))
panel2 = Label(root, image= waterImage)

airImage = ImageTk.PhotoImage(Image.open("air.gif"))
panel3 = Label(root, image= airImage)

earthImage = ImageTk.PhotoImage(Image.open("earth.gif"))
panel4 = Label(root, image= earthImage)

alastorImage = ImageTk.PhotoImage(Image.open("alastor.gif"))
vil1 = Label(root, image= alastorImage)

odonImage = ImageTk.PhotoImage(Image.open("odon.gif"))
vil2 = Label(root, image= odonImage)

zillaImage = ImageTk.PhotoImage(Image.open("zilla.gif"))
vil3 = Label(root, image= zillaImage)

kasdevaImage = ImageTk.PhotoImage(Image.open("kasdeva.gif"))
vil4 = Label(root, image= kasdevaImage)

thamishImage = ImageTk.PhotoImage(Image.open("thamish.gif"))
vil5 = Label(root, image= thamishImage)

daegalImage = ImageTk.PhotoImage(Image.open("daegal.gif"))
vil6 = Label(root, image= daegalImage)

horayImage = ImageTk.PhotoImage(Image.open("horay.gif"))
vil7 = Label(root, image= horayImage)

root.mainloop()
