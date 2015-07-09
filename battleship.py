import random
from random import randint

board = []
for x in range(10):#should make this skip over zero, so 1-10 not 0-9
    board.append(["O"] * 10)
player_name_board = []
for x in range(10):
    board.append(["O"] * 10)
second_player_name_board = []
for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)
num_turns = 5

#one player helper functions
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)
#/one player helper functions

def one_player():
    player_name = raw_input("What is the name of your fleet?")

    ship_row = random_row(board)
    ship_col = random_col(board)
    print "I have positioned my ship. You may fire when ready!"

    turn = 1
    while turn < num_turns+1:
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
        
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations, %s! You sunk my battleship!" %player_name
            break
        else:
            print "Turn ", turn
            if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
                print_board(board)
                print "Oops, that's not even in the ocean. Try again!"
                continue    
            elif(board[guess_row][guess_col] == "X"):
                print_board(board)
                print "Come on, %s, you guessed that one already. Try again."%player_name #uses up a turn, if on 4th turn doesn't even tell you you lost, just exits program 
                continue
            else:
                jeer = ["You missed my battleship! Haha, you stink, %s!"%player_name, "Better luck next time, %s."%player_name, "Not this time, %s!"%player_name, "You really are a %s, aren't you?"%player_name]
                board[guess_row][guess_col] = "X"
                print_board(board)                
                print jeer[int(round(random.random()*2))]
        if turn == num_turns:
            print "Game over, I win! Play again?"
            print "(^v^)"
            print "<( )>"
            print  "W W"
        turn += 1

#two-player helper functions
def first_turn_order(player_name, second_player_name):
        random_num = randint(0,9)
        if random_num <= 4:
            print "%s, you set sail first!" %player_name
            player_name_choice(player_name)
            myIterator = 1
            cont_turn_order(player_name, second_player_name)           
        else:
            print "%s, you set sail first!" %second_player_name
            second_player_name_choice(second_player_name)
            myIterator = 2
            cont_turn_order(player_name, second_player_name)

def player_name_choice(player_name):
    player_name_guess_row = int(raw_input("%s Guess Row:"%player_name))
    player_name_guess_col = int(raw_input("%s Guess Col:"%player_name))
def second_player_name_choice(second_player_name):
    second_player_name_guess_row = int(raw_input("%s Guess Row:"%second_player_name))
    second_player_name_guess_col = int(raw_input("%s Guess Col:"%second_player_name))

def interate():

def cont_turn_order(player_name, second_player_name):
    if myIterator == 1:
        player_name_choice()
        second_player_name_choice()
    if myIterator == 2:
        second_player_name_choice()
        player_name_choice()
    return

#/two-player helper functions

def two_player():
    player_name = raw_input("Player 1, what is the name of your fleet?")
    second_player_name = raw_input("Player 2, what is the name of your fleet?")

    turn = 1
    while turn == 1:
        first_turn_order(player_name, second_player_name)

    while turn < num_turns+1:
        if **** 1:
            player = player_name
        if **** 2:
            player = second_player_name
        cont_turn_order(player_name, second_player_name)
        if player_name_guess_row == second_player_name_guess_row and player_name_guess_col == second_player_name_guess_col:
            print "Congratulations, %s! You sunk your opponent's battleship!" %player_name #how to get this to toggle with turns
            break
        else:
            print "Turn ", turn
            guess_row = player_name_guess_row = second_player_name_guess_row
            guess_col = player_name_guess_col = second_player_name_guess_col
            if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
                print_board(board)
                print "Oops, that's not even in the ocean. Try again!"
                continue    
            elif(board[guess_row][guess_col] == "X"):
                print_board(board)
                 #   pass
                print "Come on, %s, you guessed that one already. Try again."%player
                continue
            else:
                jeer = ["You missed! Haha, you stink, %s!"%player, "Better luck next time, %s."%player, "Not this time, %s!"%player, "You really are a %s, aren't you?"%player]
                if myIterator == 1:
                    player_name_board[guess_row][guess_col] = "X" 
                    print_board(player_name_board)
                if myIterator == 2:
                    second_player_name_board[guess_row][guess_col] = "X" 
                    print_board(second_player_name_board)                
                print jeer[int(round(random.random()*2))]
        if turn == num_turns:
            print "Game over, I win! Play again?"
            print "(^v^)"
            print "<( )>"
            print  "W W"
        turn += 1

print "Let's play Battleship!"
#print_board(board)
num_players = raw_input("One player or two?") #make raw_input lowercase
if num_players == "one" or num_players == 1:
    one_player()
else:
    two_player()