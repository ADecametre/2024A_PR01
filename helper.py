special_coins_pos = [(1, 1), (14, 1), (1, 13), (14, 13)]

def create_board():

    # [x] Create a board with the following structure
    # 1 -> Wall
    # 0 -> Path

    string_maze ="""
████████████████
█              █
█ ██ ██ ███ ██ █
█     █ █      █
█ █ █   █ █ ██ █
█   █ █      █ █
█ █   ██ ███ █ █
█ █ █      █   █
█ █ ██ █ █ █ █ █
█   █          █
█ █ █ ████ ███ █
█     █    █   █
█ ██ ██ ██ █ █ █
█              █
████████████████
████████████████
"""
    maze = list(map(
        lambda ligne:[0 if char==" " else 1 for char in ligne],
        string_maze.strip().split("\n")
    ))

    return maze

def create_coins(board):
    coins = []

    # [x] Ajouter la position de toutes les cases '0' à la variable coins. Pour ajouter un élément, vous pouvez utiliser l'expression suivante : coins.append((x, y))
    # [x] Retirer les coins de chaque "coin" du carré. Vous devez utiliser la variable 'special_coins_pos' # XXX et la fonction 'remove'.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 0 and (j, i) not in special_coins_pos):
                coins.append((j,i))

    return coins

def create_special_coins(board):
    # [x] Ajouter des coins aux positions spéciales, en utilisant la variable 'special_coins_pos'.
    return special_coins_pos.copy()
