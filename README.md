![alt text](https://github.com/aglucky/JewelDuel/blob/master/Jewel.PNG?raw=true)

# Jewel Duel

Jewel Duel is a strategic take on the classic game Bejewled that allows two players to 'duel' in an epic, gem-filled Face off. This game is currently run through a terminal. The 'gems', in the game are represented as greek letters, which give it a bit of a STEM theme.

## How To Run
Download the [ZIP package](https://github.com/aglucky/JewelDuel/archive/master.zip) and unzip it.

Method 1: Using the python poetry library
1. Install the poerty library from the command line using `pip install --user poetry`
 * The game can be run by typing `python ` followed by the file name of the script, e.g. `poetry run python main.py`.
 * If the script is in a different directory from which you are trying to run it, you will need to provide the full path to the script’s file, e.g. `poetry run python /Users/myself/JewelDuel/main.py`.

Method 2: Using a Text editor or IDE
1. Open the downloaded project folder with any text editor/ide that supports python
2. Run `main.py`

## Rules

To play Jewel Duel, each player starts by choosing an in-game name for themselves. This name will be used prompt the turn player to move as well as to eventually congratulate the victor of the duel. Then, each player takes turns selecting 2 gems to swap. This is done through typing in the alphanumeric coordinate of each gem you would like to swap when prompted. If a player connects 3 gems in a row,  the gems disapear, causing any gems above to fall down and new gems to be spawned at the top of the board. If a player connects 4 gems in a row, the same effect will occur with the addition of a special gem spawning for the turn player. Once a player connects 3 of their special gems together, they will win the duel.

## Improvements on Initial Instructions

The main improvent I made was redesign the game to be played by two players. I persoanlly find the game Bejewled a bit bland so I wanted to try and spice it up by adding a pvp aspect to it. I also decided to allow 5 different types of non special gems into the game instead of three. This was to prevent matches from becoming too comman while also adding an aspect of skill to the game.


## Libraries Used

I used the Numpy, Pandas, Itertools, and random python libraries to help create Jewel Duel.

A Numpy Array is used to represent the game board of Jewel Duel. This was chosen as the size of the board remains constant throughout the game and Numpy's many data manipulation methods. When the board is shown to the user, Pandas is used to show the contents of the game board and their alphanumeric  coordinates'. This is done through creating a temporary Pandas dataframe that has the labels A-Z as its X coordinates, and 1-6 as its Y coordinates. I chose Pandas to present the board to the user due to its synergy with Numpy. I also used Itertools to cycle through the players for each turn and Random to 
spawn gems randomly at the top of the board as well as to spawn the initial board.

## Things I'm proud of

In order to detect and clear gem matches, I created an algorithim to return whether there was a match, and clear it at the same time. Though doing these at the 
same time, I was able to call the method in an if statement. This allowed me to reduce the length of my code and make my program run more effeciently than if I were to create 2 methods. I'm also proud of how I detected matches in the algorithim, which utilized both iteration and recursion. I used iteration  horizontally and vertically to figure out whether a match existed, and if there was, I used a variant of the flood fill algorithim to change all the matches to '0', or empty. A few other things that I though was cool in my program was how I used unicode characters as my gem design and some of my logic from the board's coordinate system.

## To Do

The obvious next step for this game is to create a GUI for it, likely through PyGame. There are also a few minor bugs in the game logic, though nothing game breaking. These include a few cases where the valid move checker won't catch an invalid move and the gravity method occasionally acting strangely in certain scenarios.
