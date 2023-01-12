#Controls 
yes_no = ["yes","no"]
directions = ["left","right","forward","backwards"]
answers = [1,2,3]

#Gamestart & Intro 

def introGame():
    """
    Starts game and intoduces user to the game
    """
    print("You stand in front of an old stone passageway.")
    print("You push on the wall and it slowly slides open. You step inside.")
    print("It is a huge cave.") 
    print("However, open fields & trees stretch far into the distance")
    print("To your right is a small building made of timber and straw.") 
    print("Smoke is billowing from the chimney & the lights are on")
    print("Suddenly a strange but very handsome man in dark robes appears.\n")
    print("Jon: Welcome traveller!")
    print("Jon: You look weary? Long Uber?")
    print("Jon: My name is Jon and I will be your guide through this Tomb!")
    print("Jon: Now, what is your name?\n")
    name = input()
    print("Jon: Nice to meet you "+name+".")

    response = ""
    while response not in yes_no: 
        response = input("Jon: Have you visted here before?\n")
        if response == "yes":
            print("Jon: Ah excellent! I knew I recognized your ugly mug.\n No need for instructions then! Off you pop now.")
        elif response == "no":
            print("Jon: Ah a newbie! Well, let me impart some wisdom")
            print("Jon: You are here to collect the 3 HLL keys.")
            print("Jon: There is no other way out of the Tomb.\n Except that fire exit door over there.")
            print("Jon: You will meet 3 strangers.\n Each will pose you a riddle.")
            print("Jon: Answering a riddle correctly will earn you a key and make you feel all smug and fuzzy.")
            print("Jon: Once you've collected all 3 keys, you will be able to venture to....")
            print("Jon: THE TEMPLE OF THE PODS!!!")
            print("Some smoke went off behind him and dramatic music played from an old cd player behind a tree.")
            print("Jon: Ahem, anyway. On you pop now.")
        else:
            print("Jon: Sorry, I didn't understand that.")

    print("The shadowy (and very handsome) stranger disappears.")
    print("There is a crossroads at the inn.")
    print("Each road leading to a different tomb.")

    while response not in directions: 
        response = input("Which way will you go?\n left, right, forward, backwards")








def owenLeft():
    """
    The room to the left with the stranger named Owen
    """


def liamRight():
    """
    The room to the right with the stranger named Liam
    """


def kevinForward():
    """
    The room straight ahead with the stranger named Kevin
    """




def main(): 
    """
    Run all program functions
    """
    introGame()


print("Welcome to The Secret of the HLL Tomb!")
print("The Secret of the HLL Tomb is a text adventure videogame.")
print("Your goal is to collect 3 keys to open the door at the end of the Tomb.")
print("You will meet 3 strangers along the way, each posing a riddle for you to answer")
print("Good luck!\n")
main()