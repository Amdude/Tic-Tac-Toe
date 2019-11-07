from random import randint

# create our tiles
tiles = {
    1: ['-', '-', '-'],
    2: ['-', '-', '-'],
    3: ['-', '-', '-']
}

game_over = False

chars = ['x', 'o']  # array to hold available characters
pc_char = ''  # the pc ( opponent)
user_char: str = ''  # the user

# set up our variables ( values are arbitrary )
row = 1
column = 0

matches = 0


def display_greeting():  # welcome the user
    print("Welcome to Tic-Tac-Toe!")


def assign_characters():  # assign characters (x,o) to the user and pc
    global user_char
    global pc_char

    user_char = input("\nWill you play as X or O?")
    user_char = user_char.lower()

    while True:
        if user_char == 'x' or user_char == 'o':
            chars.remove(user_char)  # remove the user's character from the characters array
            pc_char = chars[0]  # assign the remain character to the pc
            print("You are playing as " + user_char.title() + ".")
            break
        else:
            print("Not a valid choice, please choose X or O.")
            user_char = input("\nWill you play as X or O?")


def choose_first_move():
    first_move = input("\nWould you like to go first? Y/N.")
    first_move = first_move.lower()

    while True:
        if first_move == 'y':
            print("You will go first.")
            user_move()
            break
        elif first_move == 'n':
            print("The computer will go first.")
            pc_move()
            break
        else:
            print("Invalid input!")
            first_move = input("\nWould you like to go first? Y/N.")
            first_move = first_move.lower()


def user_move():
    global user_char
    print("\nYour turn: ")
    select_tile()


def select_tile():
    global row
    global column

    print_tile()
    row = input("Which row (1,2,3) do you choose?")
    print("You chose row " + row + ".")
    column = input("Which column (1,2,3) do you choose?")
    print("You chose column " + column + ".")
    row = int(row)
    column = int(column)
    check_tile()


def check_tile():
    while True:
        if tiles[row][column - 1] != '-':  # if the space is occupied by anything other than a dash
            print("\nThat tile is occupied, please choose another tile.")
            select_tile()
        else:
            tiles[row][column - 1] = user_char
            print_tile()
            game_state_checker(user_char, row)
            break

    if game_over:
        print("Game has ended.")
        return
    else:
        pc_move()


def pc_move():
    print("\nComputer's turn ... ")
    global pc_char

    while True:
        # select random values for the pc
        row = randint(1, 3)
        column = randint(0, 2)
        if tiles[row][column] != '-':  # if the space is occupied
            continue
        else:
            tiles[row][column] = pc_char
            break
    print_tile()
    game_state_checker(user_char, row)
    if game_over:
        print("Game has ended.")
        return
    else:
        user_move()


def game_state_checker(char, row):  # function to check for three in a row
    global game_over
    global matches

    matches = 0
    check_char = char

    if check_char == user_char:
        player = "You"
    else:
        player = "Computer"

    # horizontal match check
    for col in tiles[row]:
        if col == check_char:
            matches += 1
        else:
            break
    win_checker(player)

    # vertical match check
    column = 0
    while column < 3:
        matches = 0
        for row in tiles:
            if tiles[row][column] == user_char:
                matches += 1
            else:
                continue
        win_checker(player)
        column += 1

    # diagonal check left to right
    column = 0
    for row in tiles:
        if tiles[row][column] == check_char:
            matches += 1
        else:
            pass
        column += 1
    win_checker(player)

    # diagonal check right to left
    column = 2
    for row in tiles:
        if tiles[row][column] == check_char:
            matches += 1
        else:
            pass
        column -= 1
    win_checker(player)  # check to see if anyone won, passing the current player and number of matches


def win_checker(player):  # check if the user or the pc is the winner
    global game_over
    global matches

    if matches == 3:
        print(player + " won!")
        game_over = True
        return
    else:
        matches = 0


def print_tile():
    print("\nPlaying Area: ")
    for row in tiles.values():
        print('  ' + ' '.join(row))


display_greeting()
assign_characters()
choose_first_move()
