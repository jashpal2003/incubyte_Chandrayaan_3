class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.position = (x, y, z)
        self.direction = direction

    def move_forward(self):
        x, y, z = self.position
        if self.direction == 'N':
            self.position = (x, y + 1, z)
        elif self.direction == 'S':
            self.position = (x, y - 1, z)
        elif self.direction == 'E':
            self.position = (x + 1, y, z)
        elif self.direction == 'W':
            self.position = (x - 1, y, z)
        elif self.direction == 'Up':
            self.position = (x, y, z + 1)
        elif self.direction == 'Down':
            self.position = (x, y, z - 1)

    def move_backward(self):
        x, y, z = self.position
        if self.direction == 'N':
            self.position = (x, y - 1, z)
        elif self.direction == 'S':
            self.position = (x, y + 1, z)
        elif self.direction == 'E':
            self.position = (x - 1, y, z)
        elif self.direction == 'W':
            self.position = (x + 1, y, z)
        elif self.direction == 'Up':
            self.position = (x, y, z - 1)
        elif self.direction == 'Down':
            self.position = (x, y, z + 1)

    def turn_left(self):
        directions = ['N', 'W', 'S', 'E', 'Up', 'Down']
        current_index = directions.index(self.direction)
        new_index = (current_index + 1) % len(directions)
        self.direction = directions[new_index]

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W', 'Up', 'Down']
        current_index = directions.index(self.direction)
        new_index = (current_index + 1) % len(directions)
        self.direction = directions[new_index]

    def turn_up(self):
        if self.direction in ['N', 'S', 'E', 'W']:
            self.direction = 'Up'

    def turn_down(self):
        if self.direction in ['N', 'S', 'E', 'W']:
            self.direction = 'Down'

    def execute_commands(self, commands):
        for command in commands:
            if command == 'f':
                self.move_forward()
            elif command == 'b':
                self.move_backward()
            elif command == 'l':
                self.turn_left()
            elif command == 'r':
                self.turn_right()
            elif command == 'u':
                self.turn_up()
            elif command == 'd':
                self.turn_down()
