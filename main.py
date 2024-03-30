class Snake(object):
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, position):
        self.body = self.body[1:] + [position]

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]

class Game(object):

    DIR_UP = (-1, 0)
    DIR_DOWN = (1, 0)
    DIR_LEFT = (0, -1)
    DIR_RIGHT = (0, 1)

    INPUT_CHAR_UP = "W"
    INPUT_CHAR_DOWN = "S"
    INPUT_CHAR_LEFT = "A"
    INPUT_CHAR_RIGHT = "D"

    def __init__(self, height, width):
        self.height = height
        self.width = width

        init_body = [
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
        ]

        self.snake = Snake(init_body, self.DIR_RIGHT)

    def board_matrix(self):
        board = []
        for i in range(self.height):
            row = [None] * self.width
            board.append(row)
        return board
    
    
    def render(self):
        new_matrix = []
        matrix = self.board_matrix()
        print('+' + '-' * (self.width) + '+')
        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                row.append(matrix[y][x])
            new_matrix.append(row)
        
        for coord in self.snake.body:
            row, col = coord
            new_matrix[row][col] = 'O'
            
        for x, row in enumerate(new_matrix):
            print('|', end = '')
            for y, item in enumerate(row):
                if new_matrix[x][y] == None:
                    new_matrix[x][y] = ' '
                print(str(new_matrix[x][y]), end = "")
            print('|')
        print('+' + '-' * (self.width) + '+')

    def next_position(self, head_position, snake_direction):
        return (
            (head_position[0] + snake_direction[0]) % self.width,
            (head_position[1] + snake_direction[1]) % self.height
        )

    def play(self):

        self.render()

        while True:
            ch = input("").upper()

            if ch == self.INPUT_CHAR_UP and self.snake.direction != self.DIR_DOWN:
                self.snake.set_direction(self.DIR_UP)
            elif ch == self.INPUT_CHAR_DOWN and self.snake.direction != self.DIR_UP:
                self.snake.set_direction(self.DIR_DOWN)
            elif ch == self.INPUT_CHAR_LEFT and self.snake.direction != self.DIR_RIGHT:
                self.snake.set_direction(self.DIR_LEFT)
            elif ch == self.INPUT_CHAR_RIGHT and self.snake.direction != self.DIR_LEFT:
                self.snake.set_direction(self.DIR_RIGHT)
            
            next_position = self.next_position(self.snake.head(), self.snake.direction)

            print(next_position)
            print(self.snake.body)

            if next_position in self.snake.body and next_position != self.snake.body[0]:
                return False
            else:
                self.snake.take_step(next_position)

            self.render()
            


game = Game(10, 10)

#snake = Snake(snakebody, snakedirection)
#print(game.render())
game.play()