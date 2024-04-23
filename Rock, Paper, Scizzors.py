import os, random
def draw(choice):
  if choice == "rc":
    return("""
        _______
    ---'    ____)
           (_____)
           (_____)
           (____)
    ---.___(___)
    """)
  elif choice == "pc":
    return("""
         _________
    ---'    ______)___
              ________)_
              __________)
             _________)
    ---.___________)
    """)
  elif choice == "sc":
    return("""
        _______
    ---'   ______)____
              ________)
              |
              |_________
           _____________)
          (________)
    ---.__(_____)
    """)
choices = ["rc", "pc", "sc"]
def determine_winner(player, op):
  if player == op:
    return("It's a tie game!")
  elif ((player == "rc" and op == "sc") or 
        (player == "pc" and op == "rc") or
        (player == "sc" and op == "pc") ):
    return ("You won, congratulations!")
  else:
    return("You lost, sorry!")
playing, invalid = True, False
while playing:
  if not invalid:
    print("Choose rc, pc or sc")
  else:
    print("Invalid input, please type rc, pc or sc")
    invalid = False
  print("Or enter q to quit")
  player_choice = input().lower()
  op_choice = random.choice(choices)
  if player_choice in choices:
    print("You chose: "+ player_choice +  ""  + draw(player_choice))
    print("The oponent chose: " + op_choice +  ""  + draw(op_choice))
    print(determine_winner(player_choice, op_choice))
  elif player_choice == "q":
    playing = False
  else:
    invalid = True
  if playing and not invalid:
    replay = input("Wanna play again? Type yes to replay \n or enter anything else to end the game \n").lower()
    print()
    playing = replay == "yes"
  os.system('cls' if os.name == 'nt' else 'clear')  
print("Thanks for playing!")
