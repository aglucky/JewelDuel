# Jewel Duel

Jewel Duel is a strategic take on the classic game Bejewled that allows two players to 'duel' in an epic, gem-filled Face off. This game is currently
run in a terminal,with the gems represented as greek letters.

## Rules

To play Jewel Duel, each player starts by choosing an in game name for themselves. This name will be used prompt the turn player to move 
as well as congratulate the victor. Then, each player takes turns selecting 2 gems to swap. If a player connects 3 gems in a row, the gems disapear,
causing any gems above to fall down and new gems to be spawned at the top of the board. If a player connects 4 gems in a row, the same effect will occur with
the exception of a special gem to occur. Once a player connects 3 of their special gems together, they will win the duel.

## Libraries Used

A Numpy Array is used to represent the game board of Jewel Duel. This was chosen as the size of the board remains constant throughout the game and
Numpy's many data manipulation methods. When the board is shown to the user, Pandas is used to show the contents of the game board and their alphanumeric 
coordinates'. This is done through creating a temporary Pandas dataframe that has the labels A-Z as its X coordinate, and 1-6 as its y coordinate. I chose
Pandas to present the board to the user due to its synergy with Numpy. I also used Itertools to cycle through the users for player turn changes and Random to 
spawn gems randomly.

## Things I'm proud of

In order to detect and clear gem matches, I created an algorithim to return whether there was a match, and clear it at the same time. Though doing these at the same
time, I was able to call the method in an if statement. This allowed me to reduce the length of my code and make my program run more effeciently than if I create 2 
methods. I'm also proud of how I detected matches in the algorithim, which utilized both iteration and recursion. I used iteration horizontally and vertically to figure
out whether a match existed, and if there was, I used a variant of the flood fill algorithim to change all the matches to '0', or empty. A few other things that I though 
was cool in my program was how I used unicode characters as my gem design and some of my logic from the board's coordinate system.

## To Do

The obvious next step for this game is to create a GUI for it, likely through PyGame. There are also a few minor bugs in the game logic, though nothing game breaking.
These include a few cases where the valid move checker won't catch an invalid move and the gravity method occasionally acting strangely.
