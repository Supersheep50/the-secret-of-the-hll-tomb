#Controls 
yes_no = ["yes","no"]
directions = ["left","right","forward","backward"]
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
    print("Suddenly a strange but very handsome man in dark robes appears.")
    print("Jon: Welcome traveller!")
    print("Jon: You look weary? Long Uber?")
    print("Jon: My name is Jon and I will be your guide through this Tomb!")
    print("Jon: Now, what is your name?")
    name = input()
    print("Jon: Nice to meet you "+name+". Have you visited us before?")




#def main(): 
    """
    Run all program functions
    """



print("Welcome to The Secret of the HLL Tomb!")
print("The Secret of the HLL Tomb is a text adventure videogame.")
print("Your goal is to collect 3 keys to open the door at the end of the Tomb.")
print("You will meet 3 strangers along the way, each posing a riddle for you to answer")
print("Good luck!")
