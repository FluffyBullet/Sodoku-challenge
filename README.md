# Python's Sudoku Application Game

### <u>Index</u>
1. [Introduction](#uintroductionu)
2. [Focus](#uuse-of-the-websiteu)
3. [Development](#udevelopment-progressionu)
4. [Testing](#utestingu)
5. [Bugs Encountered](#ubugs-encounteredu)
6. [Acknowledgements](#uacknowledgementsu)


Link to live website: [Here](https://sudoku-game-play.herokuapp.com/)
Link to respository Site: [Here](https://github.com/FluffyBullet/Sodoku-challenge)

## <u>Introduction</u>
For practice of and display my understanding of coding language <strong>Python</strong>, this application is created as a submission of my Third project to Code Institute's "Full Stack Developers" course. 
Based off the puzzle game sudoku, this app allows the user(s) to test their knowledge and problem solving skills.

### <u>Approach</u>
At first, my view was to create a grid of 3 x 3 blocks, 3 stacked horizontally, 3 stacked vertically. For generating the field, python was to list values 1 - 9, then randomize. Branching vertically too, completing the sudoku puzzle, then hiding blocks from the user.

A more simpler method and to use another function, I have pre-determined the sudoku puzzles from website mentioned in [acknowledgements](#acknowledgements). Python will pull the intial code from the display text document.<br>
On entry submission, a grid reference will instruct Python which values to compare and update.<br>
"If" statement can determin whether the game has been completed or not, placing into a continuous loop.

### <u>Use of the website</u>
As Python is based on Command Line Interface (CLI), not graphical interface the website is to display a small docking station with a text prompt for the user focus on the application is based off it's functions rather than display.

Methods used within the python code include:
<u>Users Input</u>
- Before starting the sudoku game, the user will be prompted to enter their name (for use at the end of the game)
- Selection of difficulty 
- Entry of grid reference and their valued guess.

<u>Responsive feedback</u>
- on users submission, this will give feedback depending on status of their entry
    - If True - updating list above and congratulations
    - If False - commiserations and prompting to try again
    - If Error - advising of incorrect entry, please try again.

<u> Validation Checking</u>
- on users command, their entry will be validated if within an expected result. 
    - this will feature feedback similar with the above - catching errors.

<u>Reading of external documents</u>
- sudoku puzzle will depend on the user(s) selection, which will direct the program to it's correct path.
    - code with variables inserted
- *potential* creating of leaderboard for username and time to completion, top 5 for each difficulty.

<u>Updating list of values</u>
- users correct entries will be added onto the sudoku table using the .update value.

<u>creating and storing of dictionary</u>
- *potential* Leaderboard will be stored as a dictionary, using the user(s) name as key and time to completion as value.
    - Value to be wrote on text document

### <u>Development progression</u>

**31/8/22**


At first attempt, the intro section would request for the user to select the mode - the progressing into difficulty setting. Similar to all games and approaches, there needs to be an expectation that the user has not experienced the game/event before.


Edited to be included in the flow chart, the intro section now includes option to explain the rules, or start the game.


**01/09/22**


As the display is presented, no guide was presented for the user.


To correct this, axis lables were added within the code, but presented difficulty with alignment and blending with the rest of the presentation.


Coloring of text allowes me to make the labels to stand out from the display, giving a clear understanding to the user.


**05/09/22**


Using references to check and update entries and correct results was difficult as initial recall from the text file enters as strong with /n at the end of each array.


To correct this, the string needs "\n" removing and splitting after each commar. However, you cannot concatenate a list and a string together causing another issue for display of the puzzle.


Combatting this is to use the conversion method in the testing function rather than display. On completion this will be converted back to string then returned for display.


In addition, "_" was originally entered to show guesses required but not recognised as an integer. This was displayed as "0" instead - to be updated in rules.


**09/09/22**

After displaying the puzzle or Sudoku mapping into PrettyTables, correct guesses were not being updated. Looking into this, I found the add rows was being added as a tuple rather than list. With the data being unable to be manipulated I needed to find a way to change the data.


I found a function within the PrettyTables library, allowing me to remove previous rows. With this, I can then re-type the data to the rows showing an update.


For demonstration purposes, Test setting has been entered with all but 1 field entered. Difficulty setting == 99. Answer at B1 is 1.


**12/09/22**

Comment lines were pushed to the start of code block to allow condensing of codes and easy view between functions and purposes.
I used this method as updating "_puzzle" variable was not working correctly but required to reference between 3 functions. On completion, this was pushed back to it's correct place.


Whilst global variables should be avoided to be used, the introduction of global variables at the end of my project is to allow exporting of data to a leaderboard.

### Library's used

**PrettyTable**
```
This library allows me to use the list of rows into a presentable format whilst also spacing columns into groups of 3's with alignments.

Unfortunately this is not applicable for rows

Whilst this was introduced for display of the puzzle, I found this also benefited the use of presenting a leaderboard. Rather than creating an API and connecting to google datasheets, this could be presented in PrettyTable, also using Sort and only priting specific rows.
```

**Colorama**
```
For the display to the user for headers, entries.
With each elements being in different colors:
- Yellow for headers/Questions
- Green for Correct answers on the Python Display
- Blue to provide feedback statements
```

**datetime**
```
Breaking down the system date to miliseconds, allowing the system to record time started and time completing the quiz.
This is being used for the final result, eventually to create a leaderboard based off time and guesses to completion.
```

### Application behaviour

To map the expected use of the application/game, I have created the following charts using [Lucid Charts](#lucid-charts):
<img src = assets\images\readme_images\sudoku_flowchart.png>

### <u>Testing</u>
<table>
<th>Logic</th>
<th>Event</th>
<th>Testing Method</th>
<th>Expected Behaviour</th>
<th>Pass ?</th>
<tr>
<td rowspan = 3>Data Entry</td>
<td>Name Entry</td>
<td>Enter name as "1234" or blank</td>
<td>Error alert to display, non-valid input.</td>
<td>[]</td>
</tr>
<tr>
<td>Difficulty Selector</td>
<td>Difficulty labelled as 1(easy) 2 (medium) or 3 (hard)<br>
enter data as a, b or c</td>
<td>Error alert to display, non-valid input.</td>
<td>[x]</td>
</tr>
<tr>
<td>Grid reference</td>
<td>Typing a string or part reference of grid layout</td>
<td>Error alert - request for re-entry. non-valid field.</td>
<td>Pass ?</td>
</tr>
</table>

### My Test Run

To create the validation checks on the above table, I used the [live website](https://sudoku-game-play.herokuapp.com/) with possible entries at each point of entry. Whilst I've logged my findings above, I found it useful to log the results and entries below:

**Name validation**


`Entries of non-name values, i.e digits or just entering through`


<img src = assets/images/readme_images/p3_name_validated.png>



**Rules and Play Validation**

`Entering anything other than what is specified - rules or play`


<img src = assets/images/readme_images/p3_rules_validated.png>


**Rules then Play**

`Proceeding through to rules and play - with random capital's to check if characters are correct`


<img src = assets/images/readme_images/p3_rules_and_casing_validate.png>


**Difficulty validation**

`Enter either text or double digits, anything other than specified`


<img src = assets/images/readme_images/p3_difficulty_validate.png>


**Grid Entry**

`Type in an incorrect grid reference, i.e AA or 1234 or A10`


<img src = assets/images/readme_images/p3_grid_entry_validate.png>


**Guess entry**

`Incorrect values to be entered into guess field, i.e 11, or EE`


<img src = assets/images/readme_images/p3_grid_guess_validate.png>

**Incorrect Entry**


`Type in wrong value to display the guess is incorrect`


<img src = assets/images/readme_images/p3_incorrect_guess_validate.png>

**Correct Entry**

`Type in the correct value, for table to update`

<img src = assets/images/readme_images/p3_correct_entry.png>


**Complete Game loop**

`On completion of the table, to proceed to next stage`


<img src = assets/images/readme_images/p3_complete_validate.png>

**Leaderboard to be displayed**

`Display request if they wish to view the leaderboard - if yes, table to be displayed`


<img src = assets/images/readme_images/p3_leaderboard_test.png>


`Note - the leaderboard is only to grab the top 5 entries of, which is sorted by "Guesses" column`


**End of game**

`On option to display leaderboard, if select no the final message to be displayed`


<img src = assets/images/readme_images/p3_end_game_alternative.png>


### <u>Bugs Encountered</u>
1. When creating the selection of game or rules, the try statement iterates through twice, causing duplication of text displayed. Unable to fix at present, but will store in logs for later date.
2. After creating check_answers function, validation checks appear to only be valid for a1 entry, with all other entries proceeding. - this was due to order of functions which is now corrected - 5/9/22
3. Validation of grid and guess entry were being skipped, allowing users to enter incorrect reference and breaking the game.<br>
This was corrected by wrapping the check answer function within a If statement based on the validation.<br>
The code is displaying as an error with being too long for the window terminal, but as this is only code for background calculations, this is not edited. - 9/9/22

### <u>Acknowledgements</u>

sudoku puzzles:<br>
    - www.123rf.com, mtmmarek (https://www.123rf.com/photo_94232283_sudoku-puzzle-game-with-answers-vector-illustration.html)<br>
Flowchart Layout:<br>
    - Lucid Charts(#lucid-charts): [www.lucid.app](www.lucid.app)<br>
Formatting of Code:<br>
    - wwww.ozzmaker.com, adding color to text of code (https://ozzmaker.com/add-colour-to-text-in-python/)<br>
    - https://www.pythonchecker.com/, formatting code to readable code.<br>
    - PyPi<br>
        - Information on PrettyTable and how to format correctly - https://pypi.org/project/prettytable/<br>
        - Display of formatting for Colorama - https://pypi.org/project/colorama/<br>
        - Getting time and seconds for timer - https://pypi.org/project/DateTime/<br>
Help on creating code:<br>
    - Code Institute learning platform over Python Module with continuous returning.

Influencers - <br>
    - Brother, Jason Reynolds<br>
    ```
    Continuous conversation with mentions on flow of code and expected behaviour.
    ```<br>
    - Mentor - Marcel Mulders<br>
    ```
    Guidance on functions being created, internal variables and possitive support throughout the course.
    ```<br>
    - ClassMate - Jamie King<br>
    ```
    Comparison of projects, understanding and general conversation. With this, I was able to reflect on my project and adapt some lines to other examples available and change for requirements.
    ```