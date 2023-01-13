"""
Credit to replit
"""
import sys,time
def delprint(text="Type a string in",delay_time=.05): 
  for character in text:      
    sys.stdout.write(character) 
    sys.stdout.flush()
    time.sleep(delay_time)

import emoji

#Controls 
yes_no = ["yes","no"]
directions = ["left","right","forward"]
answers = [1,2,3]

#Gamestart & Intro 

def introGame():
    """
    Starts game and intoduces user to the game
    """
    delprint("You stand in front of an old stone passageway.\n")
    delprint("You push on the wall and it slowly slides open. You step inside.\n")
    delprint("It is a huge cave.\n") 
    delprint("However, open fields & trees stretch far into the distance.\n")
    delprint("To your right is a small building made of timber and straw.\n") 
    delprint("Smoke is billowing from the chimney & the lights are on.\n")
    delprint("Suddenly a strange but very handsome man in dark robes appears.\n")
    delprint("Jon: Welcome traveller!\n")
    delprint("Jon: You look weary? Long Uber?\n")
    delprint("Jon: My name is Jon and I will be your guide through this Tomb!\n")
    delprint("Jon: Now, what is your name?\n")
    name = input()
    delprint("Jon: Nice to meet you "+name+".\n")

    response = ""
    while response not in yes_no: 
        response = input("Jon: Have you visted here before?\n")
        if response == "yes":
            delprint("Jon: Ah excellent! I knew I recognized your ugly mug.\n")
            delprint("Jon: No need for instructions then! Off you pop now.\n")
        elif response == "no":
            delprint("Jon: Ah a newbie! Well, let me impart some wisdom.\n")
            delprint("Jon: You are here to collect the 3 HLL keys.\n")
            delprint("Jon: There is no other way out of the Tomb.\n")
            delprint("Jon: Except that fire exit door over there.\n")
            delprint("Jon: You will meet 3 strangers.\n")
            delprint("Jon: Each will pose you a riddle.\n")
            delprint("Jon: Answering a riddle correctly will earn you a key.\n")
            delprint("Jon:...and make you feel all smug and fuzzy inside.\n")
            delprint("Jon: Once you've collected all 3 keys.\n")
            delprint("Jon: you will be able to venture to....\n")
            delprint("Jon: THE TEMPLE OF THE PODS!!!\n")
            delprint("Some smoke went off behind him & dramatic music played \U0001F3B6 \n")
            delprint("Jon: Ahem, anyway. Off you pop now.\n")
        else:
            delprint("Jon: Sorry, I didn't understand that.\n")

    delprint("The shadowy (and very handsome) stranger disappears.\n")
    delprint("There is a crossroads at the inn.\n")
    delprint("Each road leading to a different tomb.\n")
    delprint("Which way will you go?\n")

    while response not in directions: 
        response = input("left, right, forward \n")
        if response == "left":
            owenLeft()
        elif response == "right":
            liamRight()
        elif response == "forward":
            kevinForward()
        else:
            delprint("I'm sorry that is not a valid path.\n")


def owenLeft():
    """
    The room to the left with the stranger named Owen
    """
    directions = ["left"]
    delprint("You decide to take the path to the left.\n")
    delprint("It is a long dirt path with bare trees on either side.\n")
    delprint("Up ahead, you see a small house made entirely of maple syrup.\n")
    delprint("It appears to be melting and reforming all at once.\n")
    delprint("A figure suddenly appears from the door, it is Owen.\n")
    delprint("Owen: Well hello there eh. You lost eh?\n")

def liamRight():
    """
    The room to the right with the stranger named Liam
    """


def kevinForward():
    """
    The room straight ahead with the stranger named Kevin
    """

def jonInn():
    """
    Going backwards brings you back to the inn"
    """
    delprint("Jon: What are you doing back here? Onwards traveller!")
    


def main(): 
    """
    Run all program functions
    """
    introGame()


delprint("Welcome to The Secret of the HLL Tomb!\n")
delprint("The Secret of the HLL Tomb is a text adventure videogame.\n")
delprint("Your goal is to collect the 3 HLL keys \U0001F5DD.\n")	
delprint("Together, they will open a door at the end of the tomb.\n")
delprint("You will meet 3 strangers along the way, each posing a riddle.\n")
print("Good luck!\n")
main()