def get_coconstraints(solve):
    x = 0
    constraints = []
    for i in solve+[0]:
        if i == 1:
            x += 1
        elif x != 0:
            constraints.append(x)
            x = 0
    return constraints

def ok_list(row, blocks, value, solve, full_solve):
    if (sum(blocks) < full_solve.count(1)) or (sum(blocks) - solve.count(1)) > (len(row) - len(solve)):
        return False
    constraints = get_coconstraints(solve)
    if len(constraints)> len(blocks):
        return False
    if len(constraints) > 0 :
        if value == 0:
            if constraints[-1] != blocks[len(constraints)-1]:
                return False
        elif value == 1:
            if constraints[-1] > blocks[len(constraints)-1]:
                return False
        elif len(row) == len(solve):
            if constraints[-1] != blocks[-1]:
                return False
    return True



def get_row_variations(row,blocks):
    options =[]
    get_row_variations_helper(row, row, blocks, 0,options)
    return options

def get_row_variations_helper(row, solve, blocks, ind,options):
    if ind== len(row):
        options.append(solve[:])
        return
    if row[ind] != -1:
        if ok_list(row, blocks, row[ind] , solve[:ind + 1], solve):
            get_row_variations_helper(row, solve, blocks, ind + 1,options)
        return
    for value in [1,0]:
        solve[ind]=value
        if ok_list(row, blocks, value, solve[:ind + 1], solve):
            get_row_variations_helper(row, solve, blocks, ind + 1,options)
    solve[ind] =-1

def get_coloum(board):
    coloums = []
    for i in range(len(board[0])):
        coloums.append([board[j][i] for j in range(len(board))])
    return coloums

def get_intersection_row(rows):
    if not rows or not rows[0]:
        return []
    list_helper=get_coloum(rows)
    new_row=[]
    for i in list_helper:
        if i.count(i[0])==len(i):
            new_row.append(i[0])
        else:
            new_row.append(-1)
    return new_row


def get_new_board(board,constraints):
    for row_index in range(len(board)):
        new_row = get_row_variations(board[row_index], constraints[row_index])
        board[row_index] = get_intersection_row(new_row)
    return board


def conclude_from_constraints(board,constraints):
    if not board or not board[0]:
        return
    board_copy=[]
    while board != board_copy:
        board_copy = board[:]
        get_new_board(board, constraints[0])
        coloums=get_coloum(board)
        if coloums:
            coloums= get_new_board(coloums, constraints[1])
            for i in range(len(coloums[0])):
                for j in range(len(coloums)):
                    board[i][j]= coloums[j][i]
    return

def solve_easy_nonogram(constraints):
    board=[[-1]*len(constraints[1]) for i in range(len(constraints[0]))]
    conclude_from_constraints(board, constraints)
    return board