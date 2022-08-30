# Python's Sudoku Application Game

### <u>Index</u>
1. [Introduction](#uintroductionu)
2. [Focus](#uuse-of-the-websiteu)
3. [Testing](#utestingu)
4. [Acknowledgements](#uacknowledgementsu)


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

<u>Reading of external documents</u>
- sudoku puzzle will depend on the user(s) selection, which will direct the program to it's correct path.
    - code with variables inserted
- *potential* creating of leaderboard for username and time to completion, top 5 for each difficulty.

<u>Updating list of values</u>
- users correct entries will be added onto the sudoku table using the .update value.

<u>creating and storing of dictionary</u>
- *potential* Leaderboard will be stored as a dictionary, using the user(s) name as key and time to completion as value.
    - Value to be wrote on text document

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
Invalid entries<br>
    - name entries (no value, numbers)<br>
    - difficulty selector<br>
    - grid references <br>
reading of data<br>
timestamps and end result<br>
logging of leaderboard
<br>
<strong><u>Validators</u></strong>

### <u>Acknowledgements</u>

sudoku puzzles:
    - www.123rf.com, mtmmarek (https://www.123rf.com/photo_94232283_sudoku-puzzle-game-with-answers-vector-illustration.html)<br>
Flowchart Layout:<br>
    - Lucid Charts(#lucid-charts): [www.lucid.app](www.lucid.app)<br>
 