# The-Secret-of-the-HLL-Tomb

- The Secret of the HLL-Tomb is a text adventure video game based off of a Podcast I co-host with some friends. Players are required to navigate 3 seperate tombs and acquire 3 keys. These 3 keys are required to open a door at the end of the adventure and complete the game. In each tomb you will meet a stranger who will pose you a riddle, you must answer the riddle correctly to win the key or it's Game Over. 

- The player has an inventory to carry the keys and there is also a logbook for users to enter in their names. This is then recorded in a connected Google Worksheet. The main menu lets users start a game, read the instructions or check out our podcast.

- For many years now I have wanted to build a text adventure video game and I am absolutely delightied I got the chance to put my idea into action. I hope you enjoy!

- *Be advised I originally had the text scroll speed to a much slower speed, to replicate someone typing. On advice of my mentor I have made it faster to make things easier for the assesor. 

[Play the deployed version here!](https://the-secret-of-the-hll-tomb.herokuapp.com/)

## Flowchart

- I created a Flowchart to help plan out the basic journey of the game. This helped massively when designing the tombs and the route the player would take to get to the end of the game. It also helped with regards to user input validation. 

- I also found the flowchart helped with initially working out the functions I would be using and how many would be needed.

- I did end up moving away from the original layout slightly. Adding in more decisions for the user, a logbook and the ability to explore each path without a Game Over.  

![Flowchart](/documents/flowchart/Python%20Project%20.png)

## User Stories

  -   #### First Time Visitor Goals

      1. As a first time user I want to understand what is The Secret of the HLL Tomb. 
      2. As a first time visitor I want to understand how to play The Secret of the HLL Tomb. 
      3. As a first time user I want to understand how to start the game, check the instructions and also read up on the podcast.
      4. As a first time visitor I want to try to beat the game and enter my name into the logbook.

  -   #### Returning Visitor Goals

      1. As a returning visitor I want to explore the other directions of the game. 
      2. As a returning visitor I want to try the other ending of the game. 
      3. As a returning visitor I want to beat the game quicker than before.

  -   #### Frequent User Goals
      1. As a frequent user I want to experience every multiple choice answer and direction in the game. 
      2. As a frequent user I want to have my name in the logbook multiple times. 

## Features

### Existing Features

- __Header__

    - When the program first boots up you are greeted with a cyan coloured header that presents the name of the game. I chose a font that gave it a slightly creepy vibe. Below the header I have also included some brief text about the basics of the game. 

   ![Header](/documents/images/header.png)

- __User creation__

    - Below the header and just after the game loads, the user is asked for their name and age. This creates a user profile for the game and is regularly mentioned throughout the game. 
    
    ![User creation](/documents/images/user-creation.png)

- __Main Menu__

    - The main menu includes 3 options for the user to choose from. Entering 1 will start a new game for the player. Entering 2 will bring up the instructions for how to play the game and what to expect. Entering 3 will bring up information about the podcast the game is based off of. 
    
    ![Main menu](/documents/images/main-menu.png)

- __Inventory__

    - The player has a bag with them that contains their inventory. This is where the 3 keys are stored as the game progresses.
    
    ![Inventory](/documents/images/inventory.png)

- __Error Messages__

    - Any time a user inputs a blank answer or an answer outside of the question parameters an error will show, and then repeat the question for the user. This validation is in place throughout the entire game regardless of the question or input asked.

    ![Error Messages](/documents/images/error-messages.png)

- __Logbook__

    - I have included a logbook for users to sign their name as they near the end of the game. I connected the sheet to my code via a Google API.

    ![Logbook](/documents/images/logbook.png)

- __Google Sheet__

    - Screenshot of Google Sheet for the logbook
   
    ![Logbook](/documents/images/google-sheet.png)

- __Emojis__

    - Several different types of emojis are scattered throughout the game to add some visual style.

    ![Emojis](/documents/images/emojis.png)

 - __Coloured Text__

    - Each character in the story has a different colour for the text they use. I did this by importing several different types of colour. All are accessible.

     ![Coloured Text](/documents/images/coloured-text.png)

- __Multiple choice Questions__

    - For each of the riddles players have 3 possible answers they can give. Giving a right answer lets them progress while getting a wrong answer is Game Over. If something else other than one of the 3 answers is entered, the game will validate and ask the question again.
    
    ![Multiple choice Questions](/documents/images/multiple-choice.png)

- __Game Over__

    - If a user gets one of the riddles wrong, it will be Game Over. Like text adventures of the past, I included this to boost replayability. Players will be given the option to Try Again or return to the Main Menu.
    
    ![Game Over](/documents/images/game-over.png)

- __Try Again__

    - When a player gets a riddle wrong, they will be offered the chance to Try Again. Saying Yes will cause the game to restart while saying No will go back to the main menu.
    
    ![Try Again](/documents/images/try-again.png) 

- __Features left to implement__

    - I would love to add some music to the game to add to the atmosphere. Right now there is no music of any kind in the game. 
    - Sadly due to time constraints I was not able to add a weapon system to the game. In the future I would like to add the ability to fight monsters. 
    - For repeat playthroughs I would like to add the ability to gain xp. 
    - I do hope to work on the game again at a later stage and add it to the HLL website. 

### Refactoring

- __Refactored User Profile code__

    - Originally the user would enter their name at the beginning of the game but it would not create a user profile to store the data for the entirety of the game. I decided to make use of some OOP and add the ability to create a user and then also validate the users name and age. Validating that there was no blank spaces proved particualrly tricky. 

    ![Refactored Code](/documents/images/user-refactored.png) 

## Testing 

- Please see the [Testing file](testing.md) for manual & validator testing.

## Deployment

### Local Deployment
​
*Gitpod* IDE was used to write the code for this project.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://supersheep5-thesecretof-31lde9cg21c.ws-eu83.gitpod.io`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://supersheep5-thesecretof-31lde9cg21c.ws-eu83.gitpod.io)
​
### Heroku Deployment
​
This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
​
Deployment steps are as follows, after account setup:
​
- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Enter a name for your app. The app name must be unique, so you need to adjust the name until you find a name that hasn't been used.
- From the dropdown, choose the region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Now, add a seecond Config Var for the `creds.json`file, which contains the API Key from Google Sheets. Set the value of KEY to `CREDS` and paste the entire contents of `creds.json` in the VALUE box. Select *add*.
- Further down, to support dependencies, select *Add buildpack*.
- The order of the buildpacks is important. Select `Python` first, then *Save changes*. Click *Add buildpack* again, and select `Node.js`, then *Save changes*. If they are not in this order, you can drag them to rearrange them

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs to be updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:
​
- At the top of the screen on Heroku, select *Deploy*.
- Next to *Deployment method* select *GitHub*, then scroll down and click *Connect to GitHub* to confirm you want to connect.
- In the *repo-name* field, search for the name of the GitHub repository to deploy, and click *Search*.
- Click *Connect* to link the GitHub repository with Heroku. 
- Scroll down to the *Manual deploy* section, and click *Deploy Branch*.
- If you like, click *Enable Automatic Deploys* in the *Automatic deploys* section to have Heroku rebuild your app every time you push a new change to GitHub.

The frontend terminal should now be connected and deployed to Heroku.

## Credits 

### Media
- [Patorjk.com](https://patorjk.com/) was used to create the heading.

- Emojis used from [Unicode.com](https://unicode.org/emoji/charts/full-emoji-list.html)

### Content 
- I used Code Institute's Love Sandwiches Walkthrough ([repo here](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1)) for guidance with code structure, linking my program to Google Sheets using an API, and deployment steps.

- For slower printing to the terminal I used Stackoverflow. The page is [here](https://stackoverflow.com/questions/510348/how-do-i-make-a-time-delay) 

- To change the color of the text I used ANSI color. Page from Stackoverflow helping it explain it to me found [here](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences)

- For the add inventory function I used this video to help me form the basics of what I needed [here](https://www.youtube.com/watch?v=rvKxC-p6kbg)

- Code to help validate the user input [here](https://initialcommit.com/blog/python-isalpha-string-method) and two seperate sessions with Tutor Support.

- To create the ability to move from tomb to tomb I referenced this page [here](https://www.makeuseof.com/python-text-adventure-game-create/)

- Used Love Sandwiches walkthrough to build out collecting data for the logbook.

- To clear the screen after the user selects Try Again, I referenced this page [here](https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python)


## Acknowledgements 

- Big shout out to my partner Stephanie for all her help and wisdom! Thanks to tutor support for helping on a couple of issues and to my mentor AJ for the guidance.