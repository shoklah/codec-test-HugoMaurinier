class robot:
    directions = ['North', 'East', 'South', 'West']
    direction_move = {
        'North': (0, 1),
        'East': (1, 0),
        'South': (0, -1),
        'West': (-1, 0)
    }

    def __init__(self, map_width: int, map_height: int, x: int = 1, y: int = 1, direction: str = "North"):
        self.map_width = map_width
        self.map_height = map_height
        self.x = x
        self.y = y
        self.direction_index = self.directions.index(direction)
        self.move_functions = {
            'L': self.turn_left,
            'R': self.turn_right,
            'F': self.move_forward
        }

    def turn_left(self):
        self.direction_index -= 1
        if self.direction_index < 0:
            self.direction_index = 3
    
    def turn_right(self):
        self.direction_index += 1
        if self.direction_index > 3:
            self.direction_index = 0

    def move_forward(self):
        move = self.direction_move[self.directions[self.direction_index]]
        self.x += move[0]
        self.y += move[1]
        if self.x < 1:
            self.x = 1
        elif self.x > self.map_width:
            self.x = self.map_width
        if self.y < 1:
            self.y = 1
        elif self.y > self.map_height:
            self.y = self.map_height

    def move(self, command: str):
        for c in command:
            self.move_functions[c]()
        return self.get_position()

    def get_position(self):
        return (self.x, self.y, self.directions[self.direction_index])
    
    def print_position(self):
        print(f'{self.x},{self.y},{self.directions[self.direction_index]}')