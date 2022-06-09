table = [
  [0, 0, 0,],
  [0, 0, 0,],
  [0, 0, 0,],
]
player1 = 1
player2 = 2
winner = 0
j = 0

def display_table(table):
  for line in table:
    print(line)

display_table(table)
    
def play(player, table):
  i = 0
  while i == 0:
    j = 0
    k = 0
    while j == 0:
      line = int(input(f"player{player}, pick a line: "))
      if line > 3 or line < 1:
        print("invalid line.")
      
      else:
        line = line
        j += 1
        
    while k == 0:
      column = int(input(f"player{player}, pick a column: "))
      if column > 3 or column < 1:
        print("invalid column.")
      
      else:
        column = column
        k += 1
    if table[line-1][column-1] == 0:
      table[line-1][column-1] = player
      i += 1
    else:
      print("\ninvalid play.\n")
  
while j < 8:
  play(player1, table)
  display_table(table)
  print("\n")

  if player1 == table[0][0] == table[0][1] == table[0][2]:
    winner = player1
    j += 5
    break

  elif player1 == table[1][0] == table[1][1] == table[1][2]:
    winner = player1
    j += 5
    break

  elif player1 == table[2][0] == table[2][1] == table[2][2]:
    winner = player1
    j += 5
    break

  elif player1 == table[0][0] == table[1][0] == table[2][0]:
    winner = player1
    j += 5
    break

  elif player1 == table[0][1] == table[1][1] == table[2][1]:
    winner = player1
    j += 5
    break

  elif player1 == table[0][2] == table[1][2] == table[2][2]:
    winner = player1
    j += 5
    break

  elif player1 == table[0][0] == table[1][1] == table[2][2]:
    winner = player1
    j += 5
    break

  elif player1 == table[2][0] == table[1][1] == table[0][2]:
    winner = player1
    j += 5
    break
  j += 1

  play(player2, table)
  display_table(table)
  print("\n")

  if player2 == table[0][0] == table[0][1] == table[0][2]:
    winner = player2
    j += 5
    break
  
  elif player2 == table[1][0] == table[1][1] == table[1][2]:
    winner = player2
    j += 5
    break
    
  elif player2 == table[2][0] == table[2][1] == table[2][2]:
    winner = player2
    j += 5
    break
    
  elif player2 == table[0][0] == table[1][0] == table[2][0]:
    winner = player2
    j += 5
    break
    
  elif player2 == table[0][1] == table[1][1] == table[2][1]:
    winner = player2
    j += 5
    break

  elif player2 == table[0][2] == table[1][2] == table[2][2]:
    winner = player2
    j += 5
    break
    
  elif player2 == table[0][0] == table[1][1] == table[2][2]:
    winner = player2
    j += 5
    break
    
  elif player2 == table[2][0] == table[1][1] == table[0][2]:
    winner = player2
    j += 5
    break
  j += 1
  
if winner == 0:
  print("draw.")

else:
  print(f"player{winner} won!\n")
  display_table(table)
  print("\n")