print("----------------------TIC-TAC-TOE - 2 Player----------------------")
matrix = [[' ' for i in range(3)] for j in range(3)]


def print_matrix():
    print("\n")
    for i in range(3):
        print(f'{matrix[i][0]} | {matrix[i][1]} | {matrix[i][2]}')
        print('-' * 10)


def is_choice_valid(choice: int) -> str:
    if not (0 <= choice <= 8):
        print("Invalid choice. Enter the right coordinates : ")
        return False
    if not matrix[choice // 3][choice % 3] == ' ':
        print("Space already occupied select free space. Enter the right coordinates : ")
        return False
    return True


def enter_choice():
    choice = int(input('=>'))
    while not is_choice_valid(choice):
        choice = int(input("=>"))
    return choice

def is_win(choice: int, mark: str):
    win_row = [mark for i in range(3)]
    if matrix[choice // 3][:] == win_row:  # check the current row
        return True
    elif matrix[:][choice % 3] == win_row:  # check the current col
        return True
    prim_dia = [matrix[i][i] for i in range(3)]
    if prim_dia == win_row:  # check primary diagonal
        return True
    sec_dia = [matrix[i][2 - i] for i in range(3)]
    if sec_dia == win_row:  # check secondary diagonal
        return True
    else:
        return False


print("Rules:\n"
      "1. First one to make line of 3 wins\n"
      "2. Player 1 moves first(uses crosses to mark)\n"
      "3. Player 2 moves use noughts to mark\n"
      "4. When player's turn input the coordinates in single digit (0-8) to mark the desired box\n")

print("Starting the Game ....\n")
print_matrix()

for i in range(1, 10, 1):

    mark = "O" if i % 2 == 0 else 'X'
    no = 2 if i % 2 == 0 else 1
    print(f"Player {no} moves. Enter your choice:")
    choice = enter_choice()

    matrix[choice // 3][choice % 3] = mark
    print_matrix()
    if is_win(choice, mark):
        print(f"\nPlayer {no} wins")
        break

if i == 9:
    print("Its a Draw")
print("GAME OVER !!!")
print('--------------------------------------------')
