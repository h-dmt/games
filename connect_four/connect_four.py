#########################################################
#     • A player wins when he/she connects four slots.  #
#     • The winning connected slots must be consecutive #
#     • A connection can be                             #
#         ◦ Horizontal                                  #
#         ◦ Vertical                                    #
#         ◦ Diagonal                                    #
#########################################################
rows = 6
cols = 7
n_players = int(input("Select number of players:\n"))
M = [[0 for _ in range(cols)] for _ in range(rows)]
winning_directions = {'L': lambda r, c: [r, c - 1],  # move left
                      'R': lambda r, c: [r, c + 1],  # move right
                      'D': lambda r, c: [r + 1, c],  # move down
                      'DLD': lambda r, c: [r + 1, c - 1],  # move down-left-diagonal
                      'DRD': lambda r, c: [r + 1, c + 1],  # move down-right-diagonal
                      'URD': lambda r, c: [r - 1, c + 1],  # move up-right-diagonal
                      'ULD': lambda r, c: [r - 1, c - 1],  # move up-left-diagonal
                      }
winner = False
free_space = True


def valid_move(r_next, c_next):
    if 0 <= r_next <= rows - 1 and 0 <= c_next <= cols - 1:
        return True
    else:
        return False


def check_win(pos):
    play_n = M[pos[0]][pos[1]]
    count = 0
    for direction in winning_directions:
        count = 0
        p_r, p_c = pos  # current position
        for _ in range(3):
            r_next, c_next = winning_directions[direction](p_r, p_c)
            if valid_move(r_next, c_next):  # validate positions around current one
                if M[r_next][c_next] == play_n:
                    count += 1
                    p_r, p_c = r_next, c_next
                else:
                    break
            else:
                break

        if count == 3:          # if 4 consecutive equal positions are found we have a winner
            return True
    return False


def full_column(c):
    for r in range(rows):
        if M[r][c] == 0:
            return False
        else:
            return True


def choose_column(p, col):
    for row in range(rows-1, -1, -1):
        if M[row][col] == 0:
            M[row][col] = p
            p_position = [row, col]
            break
    return check_win(p_position)


while not winner and free_space:
    for n in range(1, n_players+1):
        [print(*m) for m in M]
        column = int(input(f"Player {n}, please choose a column\n")) - 1  # check if column is valid
        while column >= cols or column < 0 or full_column(column):      # while not a valid column
            print("Invalid column, try again!")                         # ask for input again
            int(input(f"Player {n}, please choose a column\n")) - 1
        winner = choose_column(n, column)                               # Player chooses column
        if winner:
            [print(*m) for m in M]
            print(f"The winner is player {n}\n")
            break
    for r in range(rows):                                               # Check if any free columns to play
        if 0 in M[r]:
            free_space = True
        else:
            free_space = False

if not free_space:
    print("DRAW!\n")
    [print(*m) for m in M]
