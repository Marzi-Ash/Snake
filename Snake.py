from PyQt4 import QtCore, QtGui

class SnakeGame(object):
    def __init__(self, snake_length, board_width, board_height):
    # TODO initialize snake position
        self.board_width = board_width
        self.board_height = board_height
        self.snake_length = snake_length
        self.score = 0
        self.snake = []
        self.dir = 'r'

        count = 0
        if snake_length <= board_width: #initial snake will be horizantal
            self.snake_start = (int(self.board_height/2), self.snake_length)
            while count < self.snake_length:
                self.snake.append((self.snake_start[0],count))
                count = count + 1

        elif snake_length <= board_height: # initial snake will be vertical
            self.snake_start = (self.snake_length, int(self.board_width/2))
            while count < self.snake_length:
                self.snake.append((count, self.snake_start[1]))
                count = count + 1

        import random
        self.fruit = (random.randint(0, board_height-1), random.randint(0, board_width-1))
        while self.fruit in self.snake:
            self.fruit = (random.randint(0, board_height-1), random.randint(0, board_width-1))

    def move_snake(self):
    # TODO get user input to move snake
        x, y = self.snake[-1]
        flag = False
        if self.dir == "u":
            print("up")
            self.snake.append((x-1,y))
        elif self.dir == "d":
            print("down")
            self.snake.append((x+1,y))
        elif self.dir == "r":
            print("right")
            self.snake.append((x,y+1))
        elif self.dir == "l":
            print("left")
            self.snake.append((x,y-1))
        else:
            flag = True

        if (self.check_for_score() == False) and (flag == False):
            self.snake.remove(self.snake[0])

    def draw_screen(self):
    # TODO draw screen
        self.board = [[0]*self.board_width for i in range(self.board_height)]
        # set the place of snake
        for x, y in self.snake:
            self.board[x][y] = 1

        # set the place of goal
        self.board[self.fruit[0]][self.fruit[1]] = 2

    def check_for_game_over(self):
    # TODO if game over, then raise Exception
        err = 0
        x, y = self.snake[-1]
        if x <= -1 or x >=self.board_height or y <= -1 or y >= self.board_width:
            err = ("You Hit the Board edges! You Lost! Play again?")
            print("You Hit the Board edges! You Lost!")
            print(self.score)
        if (x,y) in self.snake[0:-1]:
            err = ("You Hit your self! You Lost! Play again?")
            print("You Hit your self! You Lost!")
            print(self.score)
        return err

    def check_for_score(self):
        if self.fruit == self.snake[-1]:
            self.score = self.score + 1
            self.snake_length = self.snake_length + 1

            import random
            self.fruit = (random.randint(0, self.board_height-1), random.randint(0, self.board_width-1))
            while self.fruit in self.snake:
                self.fruit = (random.randint(0, self.board_height-1), random.randint(0, self.board_width-1))
            return True
        return False

def play(snake_length, board_width, board_height):
    game = SnakeGame(snake_length, board_width, board_height)
    game.draw_screen()
    return game
