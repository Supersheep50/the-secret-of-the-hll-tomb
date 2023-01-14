import emoji
import sys,time
def delprint(text="Type a string in",delay_time=.00): 
  for character in text:      
    sys.stdout.write(character) 
    sys.stdout.flush()
    time.sleep(delay_time)

"""
Color definitions - credit to StackoverFlow.
"""
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple


yes_no = ["yes","no"]
directions = ["left","right","forward"]
answers = ["1","2","3"]

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
            delprint("Jon: Except for that fire exit door over there.\n")
            delprint("Jon: You will meet 3 strangers.\n")
            delprint("Jon: Each will pose you a riddle.\n")
            delprint("Jon: Answering a riddle correctly will earn you a key.\n")
            delprint("Jon:...and make you feel all smug and fuzzy inside.\n")
            delprint("Jon: Once you've collected all 3 keys.\n")
            delprint("Jon: you will be able to venture to....\n")
            delprint("Jon: THE TEMPLE OF THE PODS!!!\n")
            delprint("Smoke billowed & dramatic music played \U0001F3B6 \n")
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
    delprint("A figure suddenly appears from the door, it is.....\n")
    delprint(R+"O W E N ! ! ! \n")
    delprint("Owen: Well hello there eh. You lost eh?\n")
    
    response = ""
    while response not in yes_no: 
        response = input("Owen: Wait, I know you. Are you ""?\n")
        if response == "yes":
            delprint("Owen: I have heard much about you. I am Owen eh.\n")
            delprint("He sits down on a chair outside of the melting house.\n")
            delprint("It appears to be entirely made of Tim Hortons cups.\n")
            delprint("A key in the shape of an H hangs around his neck.\n")
            delprint("Owen: Time for your riddle. I hope you are ready eh.\n")
        elif response == "no":
            delprint("Owen: Oh? I thought you were ""eh.\n")
            delprint("Owen: Then I can not help you eh.\n")
            delprint("Owen: Please leave via that escalator over there. \n")
            delprint("He laughs a huge laugh and asks the question anyway.\n")
        else:
            delprint("Owen: Eh?\n")
    
    response = ""
    while response not in answers: 
        print("Owen: What work can one never finish?\n")
        response = input("1 )A rubix cube | 2) An autobiography |3) Hoovering \n")
        if response == "2":
            delprint("Owen: Very good traveller. You're wiser than you look.\n")
            delprint("Owen: Here take this key. You are one step closer eh.\n")
        elif response == "1":
            delprint("Owen: Not quite. Try again.\n")
        elif response == "3":
            delprint("Owen: Not quite. Try again.\n")
        else:
            delprint("Owen: Not quite. Try again.\n")

     

def liamRight():
    """
    The room to the right with the stranger named Liam
    """
    directions = ["right"]
    delprint("You decide to take the path to the right.\n")
    delprint("It is a long stone path with Lilt trees on either side.\n")
    delprint("In the distance, you see a small cart blocking the path.\n")
    delprint("The cart appears to be missing a wheel. A man stands nearby.\n")
    delprint("He is cursing the cart and kicking the fallen wheel.\n")
    delprint("He mumbles something about a man named Pa.\n")
    delprint("Suddenly, he spins around to look at you, it is....\n")
    delprint(G+"L I A M !!!\n")
    delprint("He has a long ragged beard with a scar across his face.\n")
    delprint("Liam: Ha a traveller! Neeep!\n")
    delprint("His voice is so high and shrill it hurts your ears.\n")
    delprint("Liam: You scared me. You must be the traveller I heard about.\n")
    
    
    response = ""
    while response not in yes_no: 
        response = input("Liam: Do you love Lilt like I? Neeep!")
        if response == "yes":
            delprint("Liam: Excellent. I am Liam the Vagabond. Neeep!\n")
            delprint("He does a small jig that takes several minutes.\n")
            delprint("Liam: Lilt gives me the energy to dance like this.\n")
            delprint("He dances for at least another 15 minutes.\n")
            delprint("Liam: I grow weary. Neep. Hmmm... \n")
            delprint('He starts to eye you suspiciously.')
        elif response == "no":
            delprint("Suddenyl, Jon reappears behind.\n")
            delprint("He begins to whisper i your ear.\n")
            delprint("Jon: Look pal, just say you love the Lilt okay?\n")
            delprint("Jon: Otherwise he'll never let you leave.\n")
            delprint("As quick as he appeared, Jon is gone.\n")
            delprint("Liam stares at you.\n")
        else:
            delprint("Liam: WHAT? I can't hear you, speak up.\n")
    

    response = ""
    while response not in answers: 
        delprint("Liam: I DO NOT BELIEVE YOU!! NEEEEEP!\n")
        delprint("Liam: Do you luv Lilt?? \n")
        response = input("1 )I LOVE LILT | 2) LILT IS THE BEST |3) I LUV LILT \n")
        if response == "3":
            delprint("Liam: Hmmm FINE. I believe you. Take this.\n")
            delprint("He hands you an empty can of the beverage known as Lilt.\n")
            delprint("You look at me patiently.\n")
            delprint("Liam: Oh fine. Take this too.\n")
            delprint("It is a key in the shape of an L  \U0001F5DD.\n")
        elif response == "1":
            delprint("Liam: WRONG. Neep. Try again.\n")
        elif response == "3":
            delprint("Liam: WRONG. Neep. Try again.\n")
        else:
            delprint("Liam: WRONG. Neep. Try again.\n")

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