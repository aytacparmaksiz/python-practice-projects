gameBoard = {'top-left': ' ', 'top-middle': ' ', 'top-right': ' ',
            'mid-left': ' ', 'mid-middle': ' ', 'mid-right': ' ',
            'bot-left': ' ', 'bot-middle': ' ', 'bot-right': ' '
            }
topSide = 'top-left, top-middle, top-right'
midSide = 'mid-left, mid-middle, mid-right'
bottomSide = 'bot-left, bot-middle, bot-right'

print('Key combinations to select spaces are:')
print(topSide , midSide , bottomSide, sep= '\n', end = '\n')


def printBoard(board):
    print('')
    print(board['top-left'] + '|' + board['top-middle'] + '|' + board['top-right'])
    print('-+-+-')
    print(board['mid-left'] + '|' + board['mid-middle'] + '|' + board['mid-right'])
    print('-+-+-')
    print(board['bot-left'] + '|' + board['bot-middle'] + '|' + board['bot-right'])

turn = 'X'

for i in range(9):
    printBoard((gameBoard))
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    gameBoard[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'

printBoard(gameBoard)

#since it's a not complete tic tac toe game, it does not check if the player has won or not.
