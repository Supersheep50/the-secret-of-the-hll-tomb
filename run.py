# imports
import sys
import time
import os
import gspread
from google.oauth2.service_account import Credentials
import emoji


def delprint(text="Type a string in", delay_time=.05):
    # Code to print slower than default (Credit in Readme)
    for character in text:
        sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(delay_time)


# Google apis
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# creds & gspread
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the-secret-of-the-hll-tomb')


# Color definitions - credit to StackoverFlow in Readme.
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
Or = '\033[33m'  # noqa  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[96m'  # cyan


# User input controls & inventory
directions = ["left", "right", "forwards"]
inventory = ["WATER BOTTLE", "COMPASS", "WEIRD PHOTOS OF THAT GUY JON"]
yes_no = ["yes", "no"]
use_dont_use = ["use", "dont use"]
final_question = ["Continue", "Salvation"]
answers = ["1", "2", "3"]
responses = ["", " "]


class newUser:
    # Code for class object to create a User Profile
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_input(cls):
        name = input("What is your name? ")
        age = input("What is your age? ")
        if name.isalpha() and age.isnumeric():
            return cls(name, age)
        else:
            return None


def addToInventory(item):
    # Add inventory function (credit in readme)
    inventory.append(item)


def printInventory():
    # Show items in inventory to the user
    for i in inventory:
        print(i)


def startGame():
    # Function to start game after entering your name
    """
    Starts game and intoduces user to the game
    """
    global inventory
    global itemAdd
    print(C+r"""
 _   _                                   _            __   _   _  # noqa 
| | | |                                 | |          / _| | | | |       
| |_| |__   ___   ___  ___  ___ _ __ ___| |_    ___ | |_  | |_| |__   ___  
| __| '_ \ / _ \ / __|/ _ \/ __| '__/ _ \ __|  / _ \|  _| | __| '_ \ / _ \  # noqa 
| |_| | | |  __/ \__ \  __/ (__| | |  __/ |_  | (_) | |   | |_| | | |  __/ 
 \__|_|_|_|\___| |___/\___|\___|_|  \___|\__|  \___/|_|    \__|_| |_|\___| 
| |   | | | | |                | |                                         
| |__ | | | | |_ ___  _ __ ___ | |__                                       
| '_ \| | | | __/ _ \| '_ ` _ \| '_ \                                      
| | | | | | | || (_) | | | | | | |_) |                                     
|_| |_|_|_|  \__\___/|_| |_| |_|_.__/                                                                                                                                                                    
""")

    print("(c) Jonathan Morrissey - Developer 2023")
    delprint(W+"You stand in front of an old stone passageway.\n")
    delprint("You push on the wall and it slowly slides open.\n")
    delprint("You step inside. It is a huge cave.\n")
    delprint("However, open fields & trees stretch far into the distance.\n")
    delprint("To your right is a small building made of timber and straw.\n")
    delprint("Smoke is billowing from the chimney & the lights are on.\n")
    delprint("Suddenly a strange & very handsome man in dark robes appears.\n")
    delprint("Jon: Welcome Traveller!\n")
    delprint("Jon: You look weary? Long Uber?\n")
    delprint("Jon: My name is Jon and I will be your guide today!\n")
    delprint(f"Jon: {user.name} right? What a lovely name.\n")
    delprint(f"Jon: I knew a {user.name} once. Died in this very tomb.\n")
    delprint("Jon: I see you brought a bag of inventory with you. No sword?\n")
    delprint("Jon: Eh....I'm sure you'll be fine.\n")

    response = ""
    while response not in yes_no:
        delprint("Jon: Have you visted here before?\n")
        response = input("(yes / no)\n").lower()
        if response == "yes":
            delprint("Jon: Ah excellent! I knew I recognized your ugly mug.\n")
            delprint("Jon: No need for instructions then! Off you pop now.\n")
            delprint("The shadowy (and very handsome) stranger disappears.\n")
        elif response == "no":
            delprint("Jon: Ah a newbie! Well, let me impart some wisdom.\n")
            delprint("Jon: You are here to collect the 3 HLL keys.\n")
            delprint("Jon: There is no other way out of the Tomb.\n")
            delprint("Jon: Except for that fire exit door over there.\n")
            delprint("Jon: You will meet 3 strangers.\n")
            delprint("Jon: Each will pose you a riddle.\n")
            delprint("Jon: Answering a riddle correctly will earn you a key\n")
            delprint("Jon:...and make you feel all smug and fuzzy inside.\n")
            delprint("Jon: Once you've collected all 3 keys.\n")
            delprint("Jon: you will be able to venture to....\n")
            delprint("Jon: THE TEMPLE OF THE PODS!!!\n")
            delprint("Smoke billowed & dramatic music played \U0001F3B6 \n")
            delprint("Jon: Ahem, anyway. Off you pop now.\n")
            delprint("The shadowy (and very handsome) stranger disappears.\n")
        else:
            delprint("Jon: Sorry, I didn't understand that.\n")
    innCrossroads()


def innCrossroads():
    # Crossroads function where user meert guide to go different directions.
    response = ""
    directions = ["left", "right", "forwards"]
    delprint("You are at a crossroads beside the inn.\n")
    while response not in directions:
        delprint("Which way will you go?\n")
        response = input("(left / right / forwards)\n").lower()
        if response == "right":
            delprint("You decide to go right.\n")
            owenTomb()
        elif response == "left":
            delprint("You decide to go left.\n")
            delprint("Your path is quickly blocked by some goths dancing.\n")
            delprint("You faintly hear Thomas the Tank Engine music...\n")
            delprint("You turn around.\n")
            innCrossroads()
        elif response == "forwards":
            delprint("You decide to go forwards.\n")
            delprint("You suddenly come across Jon crying under a tree.\n")
            delprint("He sees you. Its really awkward. You turn around.\n")
            innCrossroads()
        else:
            delprint("Thats not a direction there pal. Try again.\n")


def owenTomb():
    # The first tomb with the character Owen.
    delprint("It is a long dirt path with bare trees on either side.\n")
    delprint("Up ahead, you see a small house made entirely of maple syrup.\n")
    delprint("It appears to be melting and reforming all at once.\n")
    delprint("A figure suddenly appears from the door, it is.....\n")
    delprint(R+"O W E N ! ! ! \n")
    delprint("Owen: Well hello there eh. You lost eh?\n")

    response = ""
    while response not in yes_no:
        delprint(f"Owen: Wait, I know you. Are you {user.name} ?\n")
        response = input("(yes / no)\n").lower()
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
        response = input("1)A rubix cube |2)An autobiography |3)Hoovering \n")
        if response == "2":
            delprint(f"Owen: Very good {user.name}.\n")
            delprint("Owen: You're wiser than you look.\n")
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
    # The second tomb with the character Liam.
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
    delprint(f"Liam: You must be {user.name} I heard all about.\n")

    response = ""
    while response not in yes_no:
        delprint("Liam: Do you love Lilt like I? Neeep!\n")
        response = input("(yes / no)\n").lower()
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
        response = input("1) I LOVE COKE |2) I LOVE MILK |3) I LOVE LILT \n")
        if response == "3":
            delprint("Liam: Hmmm FINE. I believe you. Take this.\n")
            delprint("He hands you an empty can of Lilt.\n")
            delprint("You look at him impatiently.\n")
            delprint("Liam: Oh fine. Take this too.\n")
            delprint("It is a key in the shape of an L  \U0001F5DD.\n")
            addToInventory("LIAMS KEY")
            addToInventory("MORE WEIRD PHOTOS OF JON")
            delprint("All of a sudden a huge bird grabs you.\n")
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
    # The third tomb with character Kevin.
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
        delprint("Mystery man: WELCOME!! Are you Henry the plumber?\n")
        response = input("(yes / no)\n").lower()
        if response == "no":
            delprint("Mystery man: Oh. Well, I am....\n")
            delprint(Or+"K E V I N!!!!\n")
            delprint("Some of the wallpaper starts to peel from the walls.\n")
            delprint("He continues to stand with his arms aloft.\n")
            delprint("Kevin: Hmm if you're not the plumber....\n")
            delprint(f"Kevin: You must be this {user.name} I hear about.\n")

        elif response == "yes":
            delprint(Or+"Kevin: Oh thank god. I've been waiting for days! \n")
            delprint("Kevin: The guest bedroom toilet is terribly clogged.\n")
            delprint("Kevin: That strange girl Steph stayed here last night\n")
            delprint("Kevin: ...everytime she stays this happens.\n")
            delprint("Kevin: Wait...you don't look lika a plumber.\n")
        else:
            delprint("Kevin: What? That makes no sense.\n")

    response = ""
    while response not in answers:
        delprint("Kevin: It is time for your riddle.\n")
        delprint("Kevin: It won't be easy you know.I'm very good at riddles\n")
        delprint("Kevin: Just ask Liam or Owen. Or that weird Jon guy.\n")
        delprint("Kevin: You know he doesn't even live or work here?\n")
        delprint("Kevin: Plus that inn has had many healthcode violations\n")
        delprint("Kevin: Ahem, yes the riddle.\n")
        delprint("Kevin: It is time for your riddle....again\n")
        delprint("Kevin: What can you serve, but never eat?\n")
        response = input("1)A tennis ball |2) Burgers |3) Soup \n").lower()
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
    # Function for heading to the inn after leaving Owens tomb.
    response = ""
    delprint(W+f"Jon: Ah welcome back young {user.name}.\n")
    delprint("Jon: Sorry thats ageist of me.\n")
    delprint(f"Wait...you're only {user.age}?!\n")
    delprint("Jon: It looks like you survived Owen's Tomb. I'm surprised.\n")
    delprint("Jon: Why? Oh eh...you just don't seem too...nevermind.\n")
    while response not in yes_no:
        delprint("Jon: Lets take a look at your inventory, shall we?\n")
        response = input("(yes / no)\n").lower()
        if response == "yes":
            printInventory()
            delprint("Jon: Oh wow! You got Owens key! Well done!\n")
            delprint("Jon: You're certainly on your way now traveller.\n")
            delprint("Jon: We should definitely celebrate..wait a minute..\n")
            delprint("He stares confused at the photo album you have of him\n")
            delprint("You have absolutely no idea how it got in your bag.\n")
            delprint("Jon: WHERE ON EARTH DID THESE COME FROM?! \n")
            delprint("He looks embarassed and begins to turn red. As do you\n")
        elif response == "no":
            delprint("Jon: Ooooh someones hiding something aren't they?\n")
            delprint("Jon: Nevermind! I shall respect your privacy. \n")
            delprint("He eyes your bag keenly.\n")
        else:
            delprint("Jon: What?I SAID DO YOU WANT TO CHECK YOUR INVENTORY?\n")

    delprint("Jon: Anyway no more babbling. Time for your next tomb.\n")
    delprint("Jon: You're really in for a treat.\n")
    jonInnOwenCrossroads()


def jonInnOwenCrossroads():
    # Function for leaving the inn and heading to the next tomb.
    response = ""
    delprint("You are back at a crossroads beside the inn.\n")
    delprint("It looks different. Almost reversed?\n")
    while response not in directions:
        delprint("Which way will you go?\n")
        response = input("(left / right / forwards)\n").lower()
        if response == "left":
            delprint("You decide to go left.\n")
            liamTomb()
        elif response == "right":
            delprint("You decide to go right.\n")
            delprint("A massive Snorlax blocks your path.\n")
            delprint("Its watching a Jordan Peterson YouTube video.\n")
            delprint("It wants to talk to you about it.\n")
            delprint("You turn around.\n")
            jonInnOwenCrossroads()
        elif response == "forwards":
            delprint("You decide to go forward.\n")
            delprint("Jon is crying again but this time behind a rock.\n")
            delprint("He seems to be holding a photo of Owen.\n")
            delprint("You turn around.\n")
            jonInnOwenCrossroads()
        else:
            delprint("Thats not a direction there pal. Try again.\n")


def jonInnLiam():
    # Function for heading to the inn after leaving Liams tomb.
    response = ""
    delprint(W+f"Jon: Ah hello again {user.name}. You're not dead!\n")
    while response not in yes_no:
        delprint("Jon: Lets look at that inventory again yes?\n")
        response = input("(yes / no)\n").lower()
        if response == "yes":
            printInventory()
            delprint("Jon: Ah wonderful stuff. Two out of 3 now!\n")
            delprint("Jon: Oh. You still have those photos and....MORE?\n")
            delprint(f"Jon: You are quite an odd person {user.name}.\n")
        elif response == "no":
            delprint("Jon: What?! Why not?!\n")
            delprint(f"Jon: If you're hiding something {user.name}\n")
            delprint("Jon: I'll find out!\n")
            delprint("He seems to pout and kick at a loose stone.\n")
        else:
            delprint("Jon:What? SAID DO YOU WANT TO CHECK YOUR INVENTORY?\n")

    delprint("Jon: Anyway. You met Liam the Vagabond.\n")
    delprint("Jon: He's an interesting chap that Liam. Loves a diet Coke. \n")
    delprint("Jon: Anyway, you must continue on your journey.\n")
    jonInnLiamCrossroads()


def jonInnLiamCrossroads():
    # Function for leaving the innn and heading to the next tomb.
    response = ""
    delprint("You are back at a crossroads beside the inn.\n")
    delprint("It looks different again. The inn is now...upside down?\n")
    while response not in directions:
        delprint("Which way will you go?\n")
        response = input("(left / right / forwards)\n").lower()
        if response == "left":
            delprint("You decide to go left.\n")
            delprint("A man named Pa blocks your path.\n")
            delprint("He tries to rob you but you break free and run.\n")
            jonInnLiamCrossroads()
        elif response == "right":
            delprint("You decide to go right.\n")
            delprint("2 charity workers with clipboards are in front of you\n")
            delprint("You pretend to get a phonecall and turn around \n")
            delprint("They look disappointed.\n")
            jonInnLiamCrossroads()
        elif response == "forwards":
            delprint("You deicde to go forwards.\n")
            kevinTomb()
        else:
            delprint("Thats not a direction there pal. Try again.\n")


def jonInnKevin():
    # Function for heading to the inn after leaving Kevins tomb.
    response = ""
    delprint(W+f"Jon: Good lord {user.name}. You nearly killed me.\n")
    delprint("Jon: You've ruined my hat and crushed my vape.\n")
    while response not in yes_no:
        delprint("Jon: Can I see inside your bag?\n")
        response = input("(yes / no)\n").lower()
        if response == "yes":
            printInventory()
            delprint(f"Jon: My goodness {user.name} you've done it!\n")
            delprint("Jon: I underestimated you\n")
            delprint("Jon: I wish you'd get rid of those photos though\n")
            get_visitor_data()
        elif response == "no":
            delprint("Jon: FINE. I dont even want to look. \n")
            delprint("Jon: I bet its just full of weird photos anyway.\n")
            delprint("He storms into the inn and shuts the door behind him.\n")
            delprint("After a couple minutes of sulking he comes back out.\n")
            get_visitor_data()
        else:
            delprint("Jon:What? I SAID DO YOU WANT TO CHECK YOUR INVENTORY?\n")


def get_visitor_data():
    # Function to grab a user signature for the logbook (credit in readme)
    delprint("Jon: Hows his toilet by the way? \n")
    delprint("Jon: How do I know about it?...nevermind.\n")
    delprint("Jon: Enough about bowel movements.\n")
    delprint("Jon: Before you go on ahead. You must do one thing.\n")
    delprint("He takes out a dusty old book and blows the dust off.\n")
    delprint("Jon: This is our visitor logbook...its quite empty.\n")
    delprint("Jon: Because of all the death and that....\n")
    delprint("Jon: But please, sign your name or make a comment\n")
    delprint("Jon: Leave your mark on the tomb.\n")
    visitor_str = input("Sign your name here:")
    visitor_data = visitor_str.lower()
    print(f"You entered {visitor_str}\n")
    update_logbook(visitor_data)
    temple_of_pods()


def update_logbook(data):
    # Updates the logbook.
    delprint("Updating logbook.\n")
    logbook_worksheet = SHEET.worksheet("logbook")
    logbook_worksheet.append_row([str(data)])
    delprint("Update successful. \n")


def tryAgain():
    # Try again function after getting a question wrong.
    response = ""
    while response not in yes_no:
        delprint(W+"Try again?\n")
        response = input("(yes / no)\n").lower()
        if response == "yes":
            os.system('clear')
            mainMenu()
        elif response == "no":
            os.system('clear')
            mainMenu()
        else:
            delprint("That is not a valid option.\n")


def temple_of_pods():
    # Function to begin the final third of the game.
    response = ""
    delprint("Jon: Well, well, well. You did it.\n")
    delprint("Jon: You have found all 3 keys and you're still alive.\n")
    delprint("Jon: It is now time for you to enter...\n")
    delprint("Jon: THE TEMPLE OF THE.....\n")
    delprint("You hear a low humming noise coming from Jons robe.\n")
    delprint("It appears to be his cell phone. He looks embarassed.\n")
    delprint("Jon: Excuse me a moment.\n")
    delprint("He answers the phone \n")
    delprint("Jon: Yes they're here now.\n")
    delprint("Jon: NO I AM NOT DOING THE SMOKE & MUSIC THING \n")
    delprint("Jon glances at you sheepishly and puts away the phone \n")
    delprint(f"Jon: It is time {user.name} \n")
    while response not in yes_no:
        delprint("Are you ready?\n")
        response = input("(yes / no)\n").lower()
        if response == "yes":
            delprint("Before your very eyes the inn begins to transform.\n")
            delprint("A large grey castle in the shape of HLL appears. \n")
            delprint("You walk to it gripping the straps of your bag tight\n")
            delprint("In front of the door, stands a woman in armour.\n")
            stephGuard()
        elif response == "no":
            delprint("Jon: Pfft. Suit yourself so. \n")
            tryAgain()
        else:
            delprint("Jon: Well that makes no sense.\n")


def stephGuard():
    # Function for meeting the guard outside the Temple of the Pods.
    response = ""
    delprint("She moves her sword to block the door as you walk up.\n")
    delprint(C+"Steph: I am Stephanie. The Protector of the Pods.\n")
    delprint("You remember this is the woman who blocked Kevin's toilet.\n")
    delprint("Steph: To enter, you must have the 3 keys in your posession.\n")
    delprint("Steph: Otherwise your adventure is over.\n")
    delprint("Steph: Do you have the 3 keys? (yes / no)\n")
    check = input()
    if check == "yes":
        printInventory()
        delprint("Stephanie steps aside.\n")
        delprint("You see space for 3 keys in the door.\n")
        finalScene()
    elif response == "no":
        delprint("Steph: Your journey ends here.\n")
        tryAgain()
    else:
        delprint("Steph: Say what? Try again pal.\n")
        stephGuard()


def finalScene():
    # Final scene of the game.
    response = ""
    while response not in use_dont_use:
        delprint("Use keys?\n")
        response = input("(use / dont use)\n").lower()
        if response == "use":
            delprint("The door slowly rumbles open and shows a grand hall.\n")
            delprint("At the altar, 3 large paintings hang on the wall.\n")
            delprint("Each painting depicts 1 of the 3 strangers.\n")
            delprint("Suddenly....\n")
            delprint("....ghostly apparitions emerge from each painting\n")
        elif response == "dont use":
            delprint("Stephanie scoffs at you.\n")
            delprint("Steph: Your jounrey ends here.\n")
            tryAgain()
        else:
            delprint("Steph: Choose again.\n")

    delprint(G+f"Liam: It is time for your final choice {user.name}.\n")
    delprint(R+"Owen: You must choose between a further test of your might.\n")
    delprint(Or+"Kevin: ...or salvation at last.\n")
    delprint(W+"Jon appears from behind a pillar. Steph runs off behind him\n")

    answer = ""
    while answer not in final_question:
        delprint(f"Jon: So what will it be {user.name}?\n")
        answer = input("(continue / salvation)\n").lower()
        if answer == "continue":
            delprint(f"Jon: Good luck on your travels {user.name}\n")
            delprint("Jon: Goodbye.\n")
            delprint("On the floor in front of you appears a url.\n")
            delprint("https://supersheep50.github.io/hey-look-listen-quiz/ \n")
            delprint("Copy & paste the link to enjoy more HLL fun.\n")
            delprint("THE END. CONGRATULATIONS!\n")
            mainMenu()
        elif answer == "salvation":
            delprint(f"Jon: You have earned this rest {user.name}\n")
            delprint("Jon: Your ears and heart will thank you.\n")
            delprint(f"Jon: Good luck on your travels {user.name}\n")
            delprint("Jon: Goodbye.\n")
            delprint("On the floor in front of you appears a url.\n")
            delprint("https://open.spotify.com/show/1qWCjKkHILrRLscI33N0v7 \n")
            delprint("Copy & paste the link to enjoy more HLL fun.\n")
            delprint("THE END. CONGRATULATIONS! \n")
            mainMenu()
        else:
            delprint("Jon: Try typing better. Sigh.\n")


# Opening game header and intro.
print(C+r"""
  _   _                                  _            __   _   _
| | | |                                 | |          / _| | | | |
| |_| |__   ___   ___  ___  ___ _ __ ___| |_    ___ | |_  | |_| |__   ___
| __| '_ \ / _ \ / __|/ _ \/ __| '__/ _ \ __|  / _ \|  _| | __| '_ \ / _ \
| |_| | | |  __/ \__ \  __/ (__| | |  __/ |_  | (_) | |   | |_| | | |  __/
 \__|_|_|_|\___| |___/\___|\___|_|  \___|\__|  \___/|_|    \__|_| |_|\___|
| |   | | | | |                | |
| |__ | | | | |_ ___  _ __ ___ | |
| '_ \| | | | __/ _ \| '_ ` _ \| '_ \
| | | | | | | || (_) | | | | | | |_) |
|_| |_|_|_|  \__\___/|_| |_| |_|_.__/
""")
print("(c) Jonathan Morrissey - Developer 2023")


def mainMenu():
    # Main menu for game.
    response = ""
    while response not in answers:
        response = input("1)Start New Game |2)Instructions 3)HLL Podcast \n")
        if response == "1":
            startGame()
        elif response == "2":
            print("The Secret of the HLL Tomb is a text based video game.\n")
            print("This game can only be played on PC or Laptop.\n")
            print("You will be asked to input answers throughout the game.\n")
            print("You can answer questions via your computer keyboard.\n")
            print("The game takes about 15 minutes to complete.\n")
            print("And also has several different paths to its ending.\n")
            print("Getting a riddle question wrong is Game Over!\n")
            print("But dont fret you can Try Again!\n")
            mainMenu()
        elif response == "3":
            print("The HLL Podcast is a gaming podcast with 4 Irish lads!\n")
            print("We cover a different videogame topic every 2nd Wednesday\n")
            print("We cover games old and new! From RPGS to  Platformers!\n")
            print("It would be awesome if you gave us a listen.\n")
            print("Check out the Hey Look Listen Podcast on....\n")
            print("Apple Music, Spotify and any major streaming platform.\n")
            print("Thank you!\n")
            print("https://open.spotify.com/show/1qWCjKkHILrRLscI33N0v7 \n")
            mainMenu()
        else:
            print("Not a valid option. Choose again.\n")


# Intro Text & User validation
delprint(W+"Welcome to The Secret of the HLL Tomb!\n")
delprint("The Secret of the HLL Tomb is a text adventure videogame.\n")
delprint("Your goal is to collect the 3 HLL keys \U0001F5DD.\n")
delprint("Together, they will open a door at the end of the tomb.\n")
delprint("You will meet 3 strangers along the way, each posing a riddle.\n")
delprint("Make sure to check out the instructions before you play!\n")
delprint("Now, what is your first name and age, traveller?\n")
validated = False
while validated == False:
    user = newUser.from_input()
    if user is None:
        print("Invalid input, please enter a valid name and age.")
        continue
    else:
        validated = True
        mainMenu()
