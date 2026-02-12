
#2 players game

#board should be printed
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
for row in board:
    print(row[0] | row[1] | row[2])
    print(------------------------)


#accept input of players position 


player1 = input("Choose between X or O: ").strip().upper()
player2 = None
if player1 == "X":
   player2 = "O"
else:
    player2 = "X"
    
    
