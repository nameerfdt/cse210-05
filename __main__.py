import constants

from casting.cast import Cast
from casting.cycle import Cycle
from casting.cycle2 import Cycle2
from scripting.script import Script
from scripting.control_actors_action import ControlActorsAction
from scripting.control_actors_action2 import ControlActorsAction2
from scripting.move_actors_action import MoveActorsAction
from scripting.handle_collisions_action import HandleCollisionsAction
from scripting.draw_actors_action import DrawActorsAction
from directing.director import Director
from services.keyboard_service import KeyboardService
from services.video_service import VideoService


def main():
    # create the cast
    cast = Cast()

    cycle = Cycle()
    cycle.set_color(constants.GREEN)
    cast.add_actor("cycles", cycle)

    cycle2 = Cycle2()
    cycle2.set_color(constants.PINK)
    cast.add_actor("cycles2", cycle2)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()  # adds action to dictionary group, action name
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", ControlActorsAction2(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
