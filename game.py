
#2 players game

#board should be printed
board = []
for _ in range(9):
    print(board)


#accept input of players position 


player1 = input("Choose between X or O: ").strip().upper()
player2 = None
if player1 == "X":
   player2 = "O"
else:
    player2 = "X"
    
    
