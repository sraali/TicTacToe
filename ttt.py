from board import SmallBoard

b = SmallBoard()
while True:
    print('Welcome to Tic Tac Toe!')
    b.print_board()
    while True:
        x = int(input("Active player: {} \nPlease enter the x coordinate of the position you want to place in: ".format(b.mark)))
        y = int(input("Please enter the y coordinate of the position you want to place in: "))
        b.mark_board(x,y)
        if b.is_game_won(x,y):
            print("{} has won!".format(b.mark))
            b.clear_board()
            break

if __name__ == '__main__':
    t = ttt()

