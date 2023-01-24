## Testing 

### Manual Testing
The program was tested manually by going through all possible error validation messages for questions asked.


| Test Case | Pass? | Screenshot |
|-----------|-------|------------|
|Name & age input options: enter a space|Yes|![Successful error message](/documents/testing/name-input-error-1.png)|
|Name & age input options: enter a letter|Yes|![Successful error message](/documents/testing/name-input-error-2.png)|
|Name & age input options: enter a special character|Yes|![Successful error message](/documents/testing/name-input-error-3.png)|
|Main menu options: enter a number not between 1-3|Yes|![Successful error message](/documents/testing/main-menu-input-error.png)|
|Main menu options: enter a space |Yes|![Successful error message](/documents/testing/main-menu-input-error.2.png)|
|Main menu options: enter a special character |Yes|![Successful error message](/documents/testing/main-menu-input-error.3.png)|
|Yes or No questions: enter a special character|Yes|![Successful error message](/documents/testing/yes-no-error.png)|
|Yes or No questions: enter a number|Yes|![Successful error message](/documents/testing/yes-no-error.2.png)|
|Yes or No questions: enter a space|Yes|![Successful error message](/documents/testing/yes-no-error.3.png)|
|Crossroad direction questions: enter a number|Yes|![Successful error message](/documents/testing/crossroads-error.png)|
|Crossroad direction questions: enter a special character|Yes|![Successful error message](/documents/testing/crossroads-error.2.png)|
|Crossroad direction questions: enter a space|Yes|![Successful error message](/documents/testing/crossroads-error.2.png)|
|Update Google Sheet|Yes|![Updated spreadsheet](documentation/testing/high_score_sheet.png)



### Validator Testing 
Code was passed through the [PEP8 online linter]). On the initial run, one issue was found, a line break before a binary operator:

![PEP8 results 1]()

I adjusted the line spacing in the function, and no errors were found on a second pass:

![PEP8 results 2]()

After making some changes to the code (spacing/indentation), a third pass also came back with no issues:
![PEP8 results 3]()


### Unfixed Bugs

- Due to limitations in Code Institute's Heroku template, which was used for deployment, this site is *not* fully responsive. The terminal cannot receive input from a mobile keyboard, and does not resize based on window size. Making the application fully responsive was beyond the scope of this project. This shows responsiveness during various stages of gameplay: 

![Am I Responsive screenshot]()
