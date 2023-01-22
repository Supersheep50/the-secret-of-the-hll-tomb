# The-Secret-of-the-HLL-Tomb

- The Secret of the HLL-Tomb is a text adventure video game based off of a Podcast I co-host with some friends. Players are required to navigate 3 seperate tombs and acquire 3 keys. These 3 keys are required to open a door at the end of the adventure and complete the game. In each tomb you will meet a stranger who will pose you a riddle, you must answer the riddle correctly to win the key or it's Game Over. 

- The player has an inventory to carry the keys and there is also a logbook for users to enter in their names. This is then recorded in a connected Google Worksheet. The main menu lets users start a game, read the instructions or check out our podcast.

[Play the deployed version here!](https://the-secret-of-the-hll-tomb.herokuapp.com/)

## Flowchart

- I created a Flowchart to help plan out the basic journey of the game. This helped massively when designing the tombs and the route the player would take to get to the end of the game. It also helped with regards to user input validation. 

- I also found the flowchart helped with initially working out the functions I would be using and how many would be needed.

- I did end up moving away from the original layout slightly. Adding in more decisions for the user, a logbook and the ability to explore each path without a Game Over.  

![Flowchart](/documents/flowchart/Python%20Project%20.png)

## User Stories

  -   #### First Time Visitor Goals

      1. 

  -   #### Returning Visitor Goals

      1. 

  -   #### Frequent User Goals
      1. 

## Features

### Existing Features

- __Header__

- When the program first boots up you are greeted with a cyan coloured header that presents the name of the game. I chose a font that gave it a slightly creepy vibe. Below the header I have also included some brief text about the basics of the game. 

   ![Header](/documents/testing/header.png)

- __User creation__

    - Below the header and just after the game loads, the user is asked for their name and age. This creates a user profile for the game and is regularly mentioned throughout the game. 
    
    ![User creation](/documents/testing/user-creation.png)

- __Main Menu__

    - The main menu includes 3 options for the user to choose from. Entering 1 will start a new game for the player. Entering 2 will bring up the instructions for how to play the game and what to expect. Entering 3 will bring up information about the podcast the game is based off of. 
    
    ![Main menu](/documents/testing/main-menu.png)

- __Inventory__

    - The player has a bag with them that contains their inventory. This is where the 3 are stored as the game progresses.
    
    ![Inventory](/documents/testing/inventory.png)

- __Error Messages__

    - Any time a user inputs a blank answer or an answer outside of the question parameters an error will show, and then repeat the question for the user. This validation is in place throughout the entire game regardless of the question or input asked.

    ![Error Messages](/documents/testing/error-messages.png)



### Data Structures

__Board Class__


### Refactoring

## Testing 

Please see the 

## Deployment
​

​
### Local Deployment
​

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

- website for header

### Content 


