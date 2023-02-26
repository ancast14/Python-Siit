#display table

def display_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])

test_board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
display_board(test_board)

#ask player to choose X or O

marker = ""

while marker != "X" and marker != "O":
    marker = input("Player 1, choose X or O: ")

player1 = marker

if player1 == "X":
    player2 = "O"
else:
    player2 = "X"

return(player1,player2)
