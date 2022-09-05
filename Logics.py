import random

def start_game():
    mat = [ [0 for i in range(4) ] for j in range(4) ]
    return mat

def add_new_2(mat):

    r = random.randint(0,3)
    c = random.randint(0,3)

    while(mat[r][c]!=0):
        r = random.randint(0,3)
        c = random.randint(0,3)

    mat[r][c] = 2
    return mat

def get_current_state(mat):
    for r in range(4):
        for c in range(4):
            if mat[r][c] == 2048:
                return "won"

    for r in range(4):
        for c in range(4):
            if mat[r][c] == 0:
                return "game not over"

    for r in range(4):
        for c in range(4):
            if r+1<4:
                if mat[r][c] == mat[r+1][c]:
                    return "game not over"
            if c+1<4:
                if mat[r][c] == mat[r][c+1]:
                    return "game not over"
    
    return "lost"

def compress(mat):
    new_mat = [ [0 for i in range(4) ] for j in range(4) ]
    change = False
    for r in range(4):
        pos = 0
        for c in range(4):
            if mat[r][c]:
                new_mat[r][pos] = mat[r][c]
                if pos != c:
                    change = True
                pos += 1
            
    return new_mat,change

def merge(mat):
    change  = False
    for r in range(4):
        for c in range(3):
            if mat[r][c] == mat[r][c+1] and mat[r][c]!=0:
                mat[r][c] = 2*mat[r][c]
                mat[r][c+1] = 0
                change = True

    return mat,change


def reverse(mat):
    for r in range(4):
        for c in range(2):
            temp = mat[r][c]
            mat[r][c] = mat[r][4-c-1]
            mat[r][4-c-1] = temp
    return mat

def transpose(mat):
    for r in range(4):
        for c in range(r):
            temp = mat[r][c] 
            mat[r][c] = mat[c][r]
            mat[c][r] = temp
    return mat 

def move_left(mat):
    mat,c1 = compress(mat)
    mat,c2  = merge(mat)
    mat,c = compress(mat)
    return mat,c1 or c2

def move_right(mat):
    mat = reverse(mat)
    mat,c = move_left(mat)
    mat = reverse(mat)
    return mat,c

def move_up(mat):
    mat = transpose(mat)
    mat,c = move_left(mat)
    mat = transpose(mat)
    return mat,c

def move_down(mat):
    mat = transpose(mat)
    mat,c = move_right(mat)
    mat = transpose(mat)
    return mat,c



    



