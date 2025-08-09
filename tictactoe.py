import random

board = [' '] * 9

def print_board():
    print()
    for i in range(3):
        print(' ' + ' | '.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('---+---+---')
    print()

def winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,c,d in wins:
        if b[a]==b[c]==b[d] and b[a] != ' ':
            return b[a]
    return None

def full(b):
    return all(s!=' ' for s in b)

def human_move(sym):
    while True:
        try:
            m = int(input(f"Player {sym}, enter position (1-9): ")) - 1
            if 0 <= m <= 8 and board[m] == ' ':
                board[m] = sym
                break
            print("Invalid move")
        except:
            print("Enter a number 1-9")

def available(b):
    return [i for i,x in enumerate(b) if x==' ']

def minimax(b, depth, is_max, ai_sym, hu_sym):
    w = winner(b)
    if w == ai_sym:
        return 10 - depth
    if w == hu_sym:
        return depth - 10
    if full(b):
        return 0
    if is_max:
        best = -999
        for mv in available(b):
            b[mv] = ai_sym
            val = minimax(b, depth+1, False, ai_sym, hu_sym)
            b[mv] = ' '
            best = max(best, val)
        return best
    else:
        best = 999
        for mv in available(b):
            b[mv] = hu_sym
            val = minimax(b, depth+1, True, ai_sym, hu_sym)
            b[mv] = ' '
            best = min(best, val)
        return best

def ai_move(sym, level):
    hu = 'O' if sym=='X' else 'X'
    if level == 'easy':
        mv = random.choice(available(board))
        board[mv] = sym
        return
    best = -999
    best_moves = []
    for mv in available(board):
        board[mv] = sym
        val = minimax(board, 0, False, sym, hu)
        board[mv] = ' '
        if val > best:
            best = val
            best_moves = [mv]
        elif val == best:
            best_moves.append(mv)
    board[random.choice(best_moves)] = sym

def play():
    print("Tic Tac Toe")
    mode = ''
    while mode not in ('1','2'):
        mode = input("Choose mode: 1) Human vs Human  2) Human vs Computer : ")
    level = 'hard'
    if mode == '2':
        l = ''
        while l not in ('easy','hard'):
            l = input("Choose AI difficulty (easy/hard): ").strip().lower()
        level = l
        human_sym = ''
        while human_sym not in ('X','O'):
            human_sym = input("Choose your symbol (X goes first) X/O: ").strip().upper()
        ai_sym = 'O' if human_sym=='X' else 'X'
    turn = 'X'
    print_board()
    while True:
        if mode == '1':
            human_move(turn)
        else:
            if turn == human_sym:
                human_move(turn)
            else:
                ai_move(turn, level)
        print_board()
        w = winner(board)
        if w:
            print(f"{w} wins!")
            break
        if full(board):
            print("Draw!")
            break
        turn = 'O' if turn=='X' else 'X'

if __name__ == "__main__":
    play()
