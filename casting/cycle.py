import constants
from casting.actor import Actor
from shared.point import Point


class Cycle(Actor):
    """
    A cool bike.
    
    The responsibility of player is to move itself.
    """

    def __init__(self):
        super().__init__()
        self._segments = []  # segments list variable
        self._prepare_body()  # method prepare body

    def get_segments(self):
        return self._segments  # return the segments list

    def move_next(self):
        self.grow_tail(1)
        # move all segments
        for segment in self._segments:  # for each segment in segments list
            segment.move_next()  # move each segment to new (x,y)
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]  # return first element in segments list

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self):
        # x = int(constants.MAX_X / 2)
        x = int(constants.MAX_X / constants.CELL_SIZE + 100)
        # y = int(constants.MAX_Y / 2)
        y = int(constants.MAX_Y / 4)

        for i in range(constants.CYCLE_LENGTH):
            # position = Point(x - i * constants.CELL_SIZE, y)
            position = Point(x, y + i * constants.CELL_SIZE)  # changed cycle vertical
            # velocity = Point(1 * constants.CELL_SIZE, 0)
            velocity = Point(0, - 1 * constants.CELL_SIZE)

            text = "@" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
