import random


class Buscaminas:
    def __init__(self, rows, cols, bombs):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.board = []
        self.show = []
        self.build_board()
        self.build_show()

    def build_board(self):
        for row in range(self.rows):
            self.board.append([])
            for col in range(self.cols):
                self.board[row].append(' ')
        
        for x in range(self.bombs):
            fila = random.randint(0, self.rows - 1)
            columna = random.randint(0, self.cols -1)
            while self.board[fila][columna] == "B":
                fila = random.randint(0, self.rows - 1)
                columna = random.randint(0, self.cols -1)
            self.board[fila][columna] = "B"

    def build_show(self):
        for row in range(self.rows):
            self.show.append([])
            for col in range(self.cols):
                self.show[row].append('-')

    def show_board(self):
        for fila in range(0, self.rows):
            print(self.board[fila], " ", self.show[fila])
    
    def win(self):
        contador = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == "B" and self.show[row][col] == "F":
                    contador = contador + 1
        if contador == self.bombs:
            return True
        else:
            return False

    def lose(self):
        contador = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.show[row][col] == "F":
                    contador = contador + 1
        return contador != 10
    
    def question(self, movs):
        mov = input('Ingrese movimiento {}: '.format(movs))
        if not mov in movs:
            raise Exception
        row = int(input('Ingrese fila: '))
        col = int(input('Ingrese columna: '))
        return mov, row, col

    def play(self, mov, row, col):
        if mov == "uncover":
            self.show[row][col] = self.board[row][col]
        if mov == "flag":
            self.show[row][col] = "F"







if __name__ == '__main__':
    game = Buscaminas(8, 8, 10)
    game.show_board()
    




    





    