# cse210-05

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