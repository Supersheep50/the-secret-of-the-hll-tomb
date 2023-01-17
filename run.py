import webbrowser
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

inventory = ["WATER BOTTLE", "COMPASS", "WEIRD PHOTOS OF THAT GUY JON"]
yes_no = ["yes","no"]
answers = ["1","2","3"]

def addToInventory(item):
    inventory.append(item)

def printInventory():
    for i in inventory:
        print(i)

def startGame():
    """
    Starts game and intoduces user to the game
    """
    global inventory
    global itemAdd
    delprint("You stand in front of an old stone passageway.\n")
    delprint("You push on the wall and it slowly slides open. You step inside.\n")
    delprint("It is a huge cave.\n") 
    delprint("However, open fields & trees stretch far into the distance.\n")
    delprint("To your right is a small building made of timber and straw.\n") 
    delprint("Smoke is billowing from the chimney & the lights are on.\n")
    delprint("Suddenly a strange but very handsome man in dark robes appears.\n")
    delprint("Jon: Welcome Traveller!\n")
    delprint("Jon: You look weary? Long Uber?\n")
    delprint("Jon: My name is Jon and I will be your guide through this Tomb!\n")
    delprint("Jon: "+name+" right? What a lovely name.\n")
    delprint("Jon: I knew a "+name+" once. A Traveller. Died in this very tomb\n")
    delprint("Jon: I see you brought a bag of inventory with you. No sword?\n")
    delprint("Jon: Eh....I'm sure you'll be fine.\n")

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
    delprint("You see a path to your left.\n")
    owenTomb()
   

def owenTomb():
    """
    The room to the left with the stranger named Owen
    """
    delprint("It is a long dirt path with bare trees on either side.\n")
    delprint("Up ahead, you see a small house made entirely of maple syrup.\n")
    delprint("It appears to be melting and reforming all at once.\n")
    delprint("A figure suddenly appears from the door, it is.....\n")
    delprint(R+"O W E N ! ! ! \n")
    delprint("Owen: Well hello there eh. You lost eh?\n")
    
    response = ""
    while response not in yes_no: 
        response = input("Owen: Wait, I know you. Are you "+name+" ?\n")
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
            delprint("Owen: Time for your riddle. I hope you are ready eh.\n")
        else:
            delprint("Owen: Eh?\n")
    
    response = ""
    while response not in answers: 
        print("Owen: What work can one never finish?\n")
        response = input("1 )A rubix cube | 2) An autobiography |3) Hoovering \n")
        if response == "2":
            delprint("Owen: Very good "+name+". You're wiser than you look.\n")
            delprint("Owen: Here take this key. You are one step closer eh.\n")
            addToInventory("OWENS KEY")
            delprint("You hold a key in your hands \U0001F5DD. \n")   
            delprint("You suddenly start to feel warm and fuzzy.\n")
            delprint("You look at your hands as they disappear.\n")
            delprint("YOU'RE TELEPORTING!\n")
            delprint("Owen: You didn't even say goodbye, how rude.\n")
            delprint("The inn starts to materialize in front of you.\n")
            jonInnOwen()
        elif response == "1":
            delprint("Owen: Not quite I am afraid eh.\n")
            delprint("G A M E - O V E R \n")
            tryAgain()
             
        elif response == "3":
            delprint("Owen: Not quite I am afraid eh.\n")
            delprint("G A M E - O V E R \n")
            tryAgain()
            
        else:
            delprint("Owen: Not quite. Try again.\n")

    

def liamTomb():
    """
    The room to the right with the stranger named Liam
    """
    delprint("You decide to take the path to the right.\n")
    delprint("It is a long stone path with Lilt trees on either side.\n")
    delprint("In the distance, you see a small cart blocking the path.\n")
    delprint("The cart appears to be missing a wheel. A man stands nearby.\n")
    delprint("He is cursing the cart and kicking the fallen wheel.\n")
    delprint("He mumbles something about a man named Pa.\n")
    delprint("Suddenly, he spins around to look at you, it is....\n")
    delprint(G+"L I A M !!!\n")
    delprint("He has a long ragged beard with a scar across his face.\n")
    delprint("Liam: Ha! A Traveller! Neeep!\n")
    delprint("His voice is so high and shrill it hurts your ears.\n")
    delprint("Liam: You scared me. You must be "+name+" I heard all about.\n")
    
    
    response = ""
    while response not in yes_no: 
        response = input("Liam: Do you love Lilt like I? Neeep!\n")
        if response == "yes":
            delprint("Liam: Excellent. I am Liam the Vagabond. Neeep!\n")
            delprint("He does a small jig that takes several minutes.\n")
            delprint("Liam: Lilt gives me the energy to dance like this.\n")
            delprint("He dances for at least another 15 minutes.\n")
            delprint("Liam: I grow weary. Neep. Hmmm... \n")
            delprint('He starts to eye you suspiciously.\n')
        elif response == "no":
            delprint("Suddenly, Jon reappears behind you.\n")
            delprint("He begins to whisper in your ear.\n")
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
            delprint("You look at him impatiently.\n")
            delprint("Liam: Oh fine. Take this too.\n")
            delprint("It is a key in the shape of an L  \U0001F5DD.\n")
            addToInventory("LIAMS KEY")
            addToInventory("MORE WEIRD PHOTOS OF JON")
            delprint("All of a sudden a huge bird grabs you by the shoulders \n")
            delprint("You are carried off and see the inn in the distance.\n")
            delprint("The bird drops you with a thud.\n")
            jonInnLiam()
        elif response == "1":
            delprint("Liam: Oh dear thats not right. \n")
            delprint("G A M E - O V E R \n")
            tryAgain()
            
        elif response == "2":
            delprint("Liam: Oh dear thats not right. \n")
            delprint("G A M E - O V E R \n")
            tryAgain()
            
        else:
            delprint("Liam: WHAT?!. Neep. Try again.\n")

   

def kevinTomb():
    """
    The room straight ahead with the stranger named Kevin
    """
    directions = ["forward"]
    delprint("You decide to take the path forwards.\n")
    delprint("It is a long golden path made out of bricks.\n")
    delprint("You feel eyes watching you from the trees.\n")
    delprint("Suddenly, without warning you fall through a trapdoor.\n")
    delprint("It feels like you are falling through space & time itself.\n")
    delprint("You hear a disembodied voice surrounding you. It says...\n")
    delprint("'Open world games are rubbish and don't respect your time.'\n")
    delprint("You block your ears and shake your head. It isn't true.\n")
    delprint("It can't be true you say.\n")
    delprint("You hit the floor with a thump.\n")
    delprint("You are in a completely gold room.\n")
    delprint("In front of you, a man sits on a golden throne.\n")
   
    response = ""
    while response not in yes_no: 
        response = input("Mystery man: WELCOME!! Are you Henry the plumber?\n")
        if response == "no":
            delprint("Mystery man: Oh. Well, I am....\n")
            delprint(O+"K E V I N!!!!\n")
            delprint("Some of the gold wallpaper starts to peel from the walls.\n")
            delprint("He continues to stand with his arms aloft for some time.\n")
            delprint("Kevin: Hmm if you're not the plumber....\n")
            delprint("Kevin: You must be this "+name+" I hear about.\n")
            
        elif response == "yes":
            delprint(O+"Kevin: Oh thank god. I've been waiting for days! \n")
            delprint("Kevin: The guest bedroom toilet is terribly clogged.\n")
            delprint("Kevin: That strange girl Steph stayed here last night... \n")
            delprint("Kevin: ...everytime she stays this happens.\n")
            delprint("Kevin: Wait...you don't look lika a plumber.\n")
        else:
            delprint("Kevin: What? That makes no sense.\n")
    
    response = ""
    while response not in answers: 
        delprint("Kevin: It is time for your riddle.\n")
        delprint("Kevin: It won't be easy you know. I'm very good at riddles.\n")
        delprint("Kevin: Just ask Liam or Owen. Or that weird Jon guy.\n")
        delprint("Kevin: You know he doesn't even live or work here?\n")
        delprint("Kevin: Plus that inn has had so many healthcode violations.\n")
        delprint("Kevin: Ahem, yes the riddle.\n")
        delprint("Kevin: It is time for your riddle....again\n")
        delprint("Kevin: What can you serve, but never eat?\n")
        response = input("1 )A tennis ball | 2) Looks |3) Soup \n")
        if response == "1":
            delprint("Kevin: What?! How did you know? Most people say soup.\n")
            delprint("Kevin: You may be strange looking but you are smart.\n")
            delprint("He lifts up his wig and pulls out a key \U0001F5DD. \n")
            delprint("Kevin: You've earned this I suppose.\n")
            delprint("Kevin: Even though my toilet is still clogged.\n")
            delprint("You hold the third and final key in your hands.\n")
            addToInventory("KEVINS KEY")
            delprint("You fall through another trapdoor.\n")
            delprint("You feel like you're falling upwards.\n")
            delprint("You land with a oof directly on Jon.\n")
            jonInnKevin()
        elif response == "2":
            delprint("Kevin: Nope, that ain't it. \n")
            delprint("G A M E - O V E R \n")
            tryAgain()
            
        elif response == "3":
            delprint("Kevin: Nope, that ain't it. \n")
            delprint("G A M E - O V E R \n")
            tryAgain()
            
        else:
            delprint("Kevin: What? Try again.\n")

   

def jonInnOwen():
    response = ""
    delprint(W+"Jon: Ah welcome back young "+name+". Sorry thats ageist of me.\n")
    delprint("Jon: It looks like you survived Owen's Tomb. I'm surprised.\n")
    delprint("Jon: Why? Oh eh...you just don't seem too...nevermind.\n")
    while response not in yes_no: 
        response = input("Jon: Lets take a look at your inventory, shall we?\n")
        if response == "yes":
            printInventory()
            delprint("Jon: Oh wow! You got Owens key! Well done!\n")
            delprint("Jon: You're certainly on your way now traveller.\n")
            delprint("Jon: We should definitely celebrate....wait a minute...\n")
            delprint("He stares confused at the photo album you have of him.\n")
            delprint("You have absolutely no idea how it got in your bag.\n")
            delprint("Jon: WHERE ON EARTH DID THESE COME FROM?! \n")
            delprint("He looks embarassed and begins to turn red. As do you.\n")
        elif response == "no":
            delprint("Jon: Ooooh someones hiding something aren't they?\n")
            delprint("Jon: Nevermind! I shall respect your privacy. \n")
            delprint("He eyes your bag keenly.\n")
        else:
            delprint("Jon: What? I SAID DO YOU WANT TO CHECK YOUR INVENTORY?\n")

    delprint("Jon: Anyway no more babbling. Time for your next tomb.\n")
    delprint("Jon: You're really in for a treat.\n")
    liamTomb()
    

def jonInnLiam():
    response = ""
    delprint(W+"Jon: Ah hello again "+name+". You're not dead!\n")
    while response not in yes_no: 
        response = input("Jon: Have you the second key?\n")
        if response == "yes":
            printInventory()
            delprint("Jon: Ah wonderful stuff. Two out of 3 now!\n")
            delprint("Jon: Oh. You still have those photos and....MORE?\n")
            delprint("Jon: You are quite an odd person "+name+".\n")
            delprint("Jon: Anyway. You met Liam the Vagabond.\n")
            delprint("Jon: He's an interesting chap that Liam. Loves a diet Coke. \n")
            delprint("Jon: Anyway, you must continue on your journey.\n")
            kevinTomb()
    


def jonInnKevin():
    response = ""
    delprint(W+"Jon: Good lord "+name+". You nearly killed me.\n")
    delprint("Jon: Looks like you got Kevin's key and ruined my hat.\n")
    delprint("Jon: Hows his toilet? \n")
    delprint("Jon: How do I know about it?...nevermind.\n")
    delprint("Jon: Enough about bowel movements, you are ready!\n")
    temple_of_pods()
    
   
def tryAgain():
    response = ""
    while response not in yes_no: 
        response = input(W+"Try again?\n")
        if response == "yes":
            introGame()
        elif response == "no":
            exit()
        else:
            delprint("That is not a valid option")


def temple_of_pods(): 
    response = ""
    delprint("Jon: Well, well, well. You did it.\n")
    delprint("Jon: You have found all 3 keys. Plus lost some weight it seems.\n")
    delprint("Jon: It is now time for you to enter...\n")
    delprint("Jon: THE TEMPLE OF THE.....\n")
    delprint("You hear a low humming noise coming from Jons robe.\n")
    delprint("It appears to be his cell phone. He looks embarassed.\n")
    delprint("Jon: Excuse me a moment.\n")
    delprint("He answers the phone \n")
    delprint("Jon: Yes they're here now.\n")
    delprint("Jon: NO I AM NOT DOING THE SMOKE & MUSIC THING \n")
    delprint("Jon glances at you sheepishly and puts away the phone \n")
    delprint("Jon: Right. Time for you to go then. Good luck! \n")
    
def main(): 
    """
    Run all program functions
    """
    """
    tombs = {
        'Owens Tomb':{'item':'Owens key'},
        'Liams Tomb':{'item':'Liams key'},
        'Kevins Tomb':{'item':'Kevins key'}
    }
    """
    startGame()
   



delprint("Welcome to The Secret of the HLL Tomb!\n")
delprint("The Secret of the HLL Tomb is a text adventure videogame.\n")
delprint("Your goal is to collect the 3 HLL keys \U0001F5DD.\n")	
delprint("Together, they will open a door at the end of the tomb.\n")
delprint("You will meet 3 strangers along the way, each posing a riddle.\n")
name = input("Now, what is your name, traveller?\n")
print("Good luck "+name+"!\n")
main()




