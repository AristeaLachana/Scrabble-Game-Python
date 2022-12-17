# Scrabble-Game-Python

Scrabble game with two players: the user and the computer.
In each round both players get random letters and try to make a valid greek word with them. The game checks if the word they make exists from file greek7.txt and they get points. The player with the most points wins.

Used MIN-MAX-SMART algorithm for the player Computer.

# Getting Started
An options menu appears to the screen. The user can choose:
1) Settings
2) Start game
3) Info
4) Exit game

The Settings option is for choosing the algorithm for the player computer (min / max / smart). The default settings is the min algorithm.
The start game option starts the game.
The info option appears information about the implementation of the game, which classes where used and what each of them does.
The exit game option stops the game.

# About the Game
There are greek letters and in each round 7 random letters are given to each player. The players try to make a valid greek word. 
In each round new letters are given if in the previous round none of the letters were used. If some letters were used, in the next round they get replaced randomly.
Each letter has a specific value. so the value of each word that the players make is based on the used letters.

The player with the most points wins.

# Computer Player Algorithms
Min: Creates all the possible letter permutations that the Computer Player has, starting from 2 letters and going until 7 letters. 
In each permutation the algorithm tests if the word that is created is valid and it returns the first valid word that is made.
If there is no valid word found, the screen appears "no word found".

Max: Same as min algorithm, but it starts from 7 letters words and decreases until 2 letters words.

Smart: All letters permutations are made and the word that the Computer Player chooses is the one with the best value. 
