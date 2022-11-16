# cse210-05
# Cycle Overview
___
Cycle is a game where two players try to cut each other off using cycles that leave a trail behind them. 
    Player one controls cycle1 using W,S,A and D keys.
    Player two controls cycle2 using I,K,J AND L keys.
Each player's trail grows as they move. 
Players try to maneuver so the opponet collided with their trail. 
If a player collides with their opponent's trail...
    A "game over" message is displayed in the middle of the screen. 
    The cycles turn white. 
    Players keep moving and turning but don't run into each other.  

## Getting Started
___

Make sure you have Python 3.10 or newer installed and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
``` 
Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
__main__.py
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the puzzle folder and click the "run" button.

## Project Structure
___

__main__

### Constants
- A file that contains constants for the program

## Casting

### Actor
- Visible and movable parts of the game

### Cast
- A collection of Actors with related groups

### Cycle 1
- A special Actor that a player controls

### Cycle 2
- A special Actor that a player 

## Directing
### Director
- Directs the game while in operation

## Scripting

### action
- A template that defines how actions should work
### control_actors_action 1
- Converts keyboard input into movement for player 1
### control_actors_action 2
- Converts keyboard input into movement for player 2
### draw_actors_action
- Draw the actors onto the screen
### handle_collisions_action
- Handle when two objects collide
### move_actors_action
- Handles moving the players on the screen
### script
- Keeps track of a collection of actions

## Services

### keyboard_service
- Handles keyboard inout
### video_service
- Output the games state to the screen

## Shared

### color
- A helper class for defining colors
### point
- A helper class to define a point (x, y)

## Required Technologies
---
* Python 3.10
* Raylib Python CFFI 3.7

## Authors
---
* Alex Dahl (alexdahl@byui.edu)
* Tracy Freeman (nameerfdt@byui.edu)
* Joshua Herman (her21095@byui.edu)
