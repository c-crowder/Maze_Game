# Maze_Game

#### This is a game made in Pygame inspired by the final project for the 2022 MOOC Python Programming course for the Univervisity of Helsinki.
#### This was both an exercise in utilizing pygame and enabling class based architecture for potentially easier changes in the future.
#### The game takes advantage of python dictionary data structures to load the various maps in the game.
#### This allows the easy addition of new maps by simply adjusting/adding a dictionary.

#### The purpose of the game is to make the robot get to the coin. It is a turn based game, and each move is a turn both for the robot and the monster. If the monster touches the robot, you have to restart the level. The robot technically moves first so if the robot and monster are one tile apart, the robot will be safe so long as it never moves towards the monster. The levels each test different skills and they provide puzzles which require you to understand how the tracking of the monster works in the game. If you get stuck, feel free to analyze the code and then try again. 

#### Also, any doors in the game act as teleports to another door. Beware, the logic can break down quite dramatically if you have more than one door in a game due to the way that doors are treated. You can have more than one monster, but the monsters will not move all at once, only one at a time and the one that is closest to the top left of the board will move first. I encourage you to try and understand why.
