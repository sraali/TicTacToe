class SmallBoard(object):
    rows = 3
    cols = 3
    board = []

    def __init__(self):
        self.mark = 'X'
        for row in range(self.rows):
            self.board.append([])
            for col in range(self.cols):
                self.board[row].append(' ')

    def print_board(self):
        for row in self.board:
            print('\n', row)
        print("--------------------")

    def mark_board(self,row_num,col_num):
        if self.board[row_num][col_num] is ' ':
            self.board[row_num][col_num] = self.mark
            if self.mark is 'X':
                self.mark = 'O'
            else:
                self.mark = 'X'
            self.print_board()
        else:
            print('That space has already been taken')

    def clear_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col] = ' '
        self.mark = 'X'

    def is_game_won(self,row_num,col_num):
        winner = self.board[row_num][col_num]
        #Horizontally
        for col in range(self.cols):
            if col is 0:
                count = 0
            if self.board[row_num][col] is winner:
                count += 1
            if count is 3:
                print("Horizontal")
                return True
        #Vertically
        for row in range(self.rows):
            if row is 0:
                count = 0
            if self.board[row][col_num] is winner:
                count += 1
            if count is 3:
                print('Vertical')
                return True
        #Negatively Diagonally
        for index in range(self.rows):
            if index is 0:
                count = 0
            if self.board[index][index] is winner:
                count += 1
            if count is 3:
                print('Negative')
                return True
        #Positively Diagoally
        for row in reversed(range(self.rows)):
            if row is 2:
                count = 0
            if self.board[row][count] is winner:
                count += 1
            if count is 3:
                print('DiagonallyPositive')
                return True
        return False

