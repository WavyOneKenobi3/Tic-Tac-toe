print("Player 1 will be X and Player 2 will be O")

#2 players game
player1 = "Player 1"
player2 = "Player 2"


#board should be printed

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    
    
board = ["1","2","3","4","5","6","7","8","9"]
    
#accept input of players position 
def main_game():
    while True: 
        print_board(board)
        position = int(input("Select a position between 1-9"))

    
    

print_board(board)