from random import randint


class Buscaminas:
    def __init__(self, rows=8, cols=8, bombs=10):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.board = []
        self.show = []
        self.board_empty()
        self.board_bombs()
        self.board_numbers()

    def board_empty(self):
        for row in range(0, self.rows):
            self.board.append([' '] * self.cols)
            self.show.append(['-'] * self.cols)

    def board_bombs(self):
        bombs = 1
        while bombs <= self.bombs:
            row = randint(0, self.rows - 1)
            col = randint(0, self.cols - 1)
            if self.board[row][col] != 'B':
                self.board[row][col] = 'B'
                bombs += 1

    def board_numbers(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if self.board[row][col] != 'B':
                    number = 0
                    if row > 0 and col > 0 and self.board[row - 1][col - 1] == 'B':
                        number += 1
                    if col > 0 and self.board[row][col - 1] == 'B':
                        number += 1
                    if row < self.rows - 1 and col > 0 and self.board[row + 1][col - 1] == 'B':
                        number += 1
                    if row > 0 and self.board[row - 1][col] == 'B':
                        number += 1
                    if row < self.rows - 1 and self.board[row + 1][col] == 'B':
                        number += 1
                    if row > 0 and col < self.cols - 1 and self.board[row - 1][col + 1] == 'B':
                        number += 1
                    if col < self.cols - 1 and self.board[row][col + 1] == 'B':
                        number += 1
                    if row < self.rows - 1 and col < self.cols - 1 and self.board[row + 1][col + 1] == 'B':
                        number += 1
                    if number > 0:
                        self.board[row][col] = str(number)

    def show_board(self):
        for row in range(0, self.rows):
            print(self.board[row], self.show[row])

    def win(self):
        bombs = 0
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if self.show[row][col] == 'F' and self.board[row][col] == 'B':
                    bombs += 1
        return bombs == self.bombs

    def lose(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if self.show[row][col] == 'B':
                    return True
        return False

    def play(self, mov, row, col):
        if mov == 'uncover':
            self.show[row][col] = self.board[row][col]
        if mov == 'flag':
            self.show[row][col] = 'F'
        self.show_board()

    def question(self, movs):
        mov = input('Ingrese movimiento {}: '.format(movs))
        if not mov in movs:
            raise Exception
        row = int(input('Ingrese fila: '))
        col = int(input('Ingrese columna: '))
        return mov, row, col
