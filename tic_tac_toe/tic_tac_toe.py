# The classic two-player game on a 3x3 board

def start_game():
    global players, B
    player_1 = input("Player one name:\n")
    player_2 = input("Player two name:\n")
    p1_sym = p1_sym = input(f"{player_1} would you like to play with 'X' or 'O'?").upper()
    while p1_sym not in ['X', 'O']:
        p1_sym = input(f"{player_1} incorrect choice, choose 'X' or 'O'!").upper()
    p2_sym = 'O' if p1_sym == 'X' else 'X'
    players = [[player_1, p1_sym], [player_2, p2_sym]]
    B = [[str(n+i) for i in range(3)]for n in range(1, 8, 3)]
    print("This is the numeration of the board:\n")
    [print('| ' + ' | '.join(b) + ' |', sep='\n') for b in B]
    print(f"{player_1} starts first!")
    for row in range(3):
        for col in range(3):
            B[row][col] = ' '


def play(name, symbol):
    n = 10
    free_cell = False
    while not free_cell:
        n = int(input(f"{name} choose a free position [1-9]\n"))
        if n in range(1, 10):
            row = (n-1) // 3
            col = (n-1) % 3
            if B[row][col] == ' ':
                B[row][col] = symbol
                free_cell = True
                [print('| ' + ' | '.join(b) + ' |', sep='\n') for b in B]


def check_winner(player, symb):
    # Check rows
    for row in B:
        if all([el == symb for el in row]):
            return True

    # check columns
    for c in range(3):
        if all([B[r][c] == symb for r in range(3)]):
            return True

    # check main diagonal
    if all([B[r][r] == symb for r in range(3)]):
        return True

    # check secondary diagonal
    if all([B[r][2-r] == symb for r in range(3)]):
        return True

    return False


def check_draw():
    for row in B:
        for el in row:
            if el == ' ':
                return False
    return True


players = []
winner = False
draw = False
B = []
start_game()
while True:
    for i in range(2):  # Alternating between player 1 and player 2
        player_name, play_symbol = players[i][:]
        play(player_name, play_symbol)  # Pass player name and symbol to play function

        if check_winner(player_name, play_symbol):
            print(f"{player_name} won!\n")
            exit()

        elif check_draw():
            print("Draw...\nGame Over!")
            exit()
