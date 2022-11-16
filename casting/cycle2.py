import constants
from casting.actor import Actor
from shared.point import Point


class Cycle2(Actor):
    """
    A cool bike.
    
    The responsibility of player is to move itself.
    """

    def __init__(self):
        super().__init__()
        self._segments2 = []
        self._prepare_body()

    def get_segments(self):
        return self._segments2

    def move_next(self):
        self.grow_tail(1)
        # move all segments
        for segment in self._segments2:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments2) - 1, 0, -1):
            trailing = self._segments2[i]
            previous = self._segments2[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments2[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments2[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._color)
            self._segments2.append(segment)

    def turn_head(self, velocity):
        self._segments2[0].set_velocity(velocity)

    def _prepare_body(self):
        # x = int(constants.MAX_X / 2)
        x = int(constants.MAX_X * constants.CELL_SIZE - 200)
        # y = int(constants.MAX_Y / 2)
        y = int(constants.MAX_Y / 4)

        for i in range(constants.CYCLE_LENGTH):
            # position = Point(x - i * constants.CELL_SIZE, y)
            position = Point(x, y + i * constants.CELL_SIZE)  # changed cycle vertical
            # velocity = Point(1 * constants.CELL_SIZE, 0)
            velocity = Point(0, -1 * constants.CELL_SIZE)

            text = "@" if i == 0 else "#"
            color = constants.CYAN if i == 0 else constants.PINK

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments2.append(segment)
