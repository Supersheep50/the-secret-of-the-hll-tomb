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
|Yes or No questions: enter a special character |Yes|![Successful error message](/documents/testing/yes-no-error.png)|
|Yes or No questions: enter a number |Yes|![Successful error message](/documents/testing/yes-no-error.2.png)|
|Yes or No questions: enter a space |Yes|![Successful error message](/documents/testing/yes-no-error.3.png)|
|Crossroad direction questions: enter a number |Yes|![Successful error message](/documents/testing/crossroads-error.png)|
|Crossroad direction questions: enter a special character |Yes|![Successful error message](/documents/testing/crossroads-error.2.png)|
|Crossroad direction questions: enter a space |Yes|![Successful error message](/documents/testing/crossroads-error.3.png)|
|Riddle questions: enter a number outside of 1-3 |Yes|![Successful error message](/documents/testing/riddle-question.1.png)|
|Riddle questions: enter a space |Yes|![Successful error message](/documents/testing/riddle-question.2.png)|
|Riddle questions: enter a special character |Yes|![Successful error message](/documents/testing/riddle-question.3.png)|
|Try Again statement: enter a special character |Yes|![Successful error message](/documents/testing/try-again-error.png)|
|Try Again statement: enter a space |Yes|![Successful error message](/documents/testing/try-again-error.2.png)|
|Try Again statement: enter a number |Yes|![Successful error message](/documents/testing/try-again-error.3.png)|
|Inventory check: enter a number |Yes|![Successful error message](/documents/testing/inventory-check.png)|
|Inventory check: enter a space |Yes|![Successful error message](/documents/testing/inventory-check.2.png)|
|Inventory check: enter a special character |Yes|![Successful error message](/documents/testing/inventory-check.3.png)|
|Key check: enter a special character |Yes|![Successful error message](/documents/testing/key-check.png)|
|Key check: enter a space |Yes|![Successful error message](/documents/testing/key-check.2.png)|
|Key check: enter a number |Yes|![Successful error message](/documents/testing/key-check.3.png)|
|Key use: enter a number |Yes|![Successful error message](/documents/testing/key-use.png)|
|Key use: enter a space |Yes|![Successful error message](/documents/testing/key-use.2.png)|
|Key use: enter a special character |Yes|![Successful error message](/documents/testing/key-use.3.png)|
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
