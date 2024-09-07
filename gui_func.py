import random

def new_grid(empty=False):
    new = []
    if empty:
        for i in range(0,4):
            new.append([])
    else:
        for i in range(0,4):
            new.append([0]*4)
    return new
    

def add_new(sqr):
    get = False
    while not get:
        row , col = random.randrange(0,4) , random.randrange(0,4)
        if sqr[row][col] == 0:
            sqr[row][col] = 2
            get = True

   
def move(sqr):
    new = new_grid()
    for u in range(0,4):
        count = 0
        for v in range(0,4):
            if sqr[u][v] != 0:
                new[u][count] = sqr[u][v]
                count += 1
    return new
    
def reverse(sqr):
    new = new_grid(True)
    for u in range(0,4):
        for v in range(0,4):
            new[u].append(sqr[u][3-v])
    return new


def transverse(sqr):
    new = new_grid(True)
    for u in range(0,4):
        for v in range(0,4):
            new[u].append(sqr[v][u])
    return new

def merge(sqr):
    for u in range(0,4):
        for v in range(0,3):
            if sqr[u][v] == sqr[u][v+1]:
                sqr[u][v] *= 2
                sqr[u][v+1] = 0

def merging(sqr):
    for u in range(0,4):
        for v in range(0,3):
            if sqr[u][v] == sqr[u][v+1]:
                return True

def is_any_empty(sqr):
    for u in range(0,4):
        for v in range(0,4):
            if sqr[u][v] == 0:
                return True

def game_over_check(sqr):
    if not is_any_empty(sqr):
        if merging(sqr):
            return False
        else:
            return True
    else:
        return False

def win_check(sqr):
    for u in range(0,4):
        for v in range(0,4):
            if sqr[u][v] == 2048:
                return True

