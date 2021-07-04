import time

def gen_world(board):
    world = ""
    for i in board:
        if i == "/":
            world += "\n"
        else:
            world += i 
    return world 
    
def make_world(board):
    world = ""
    for i in range(0,len(board)):
        if not(i == 0) and i%8==0:
            world += "/"
        world += board[i]
    return world
    
def neighbours(board, elem):
    num=0 
    #n = pos[i-9]+pos[i-8]+pos[i-7]+pos[i-1]+pos[i+1]+pos[i+7]+pos[i+8]+pos[i+9]
    for j in range(7,10):
        if elem<=len(board)-1-j:
            if board[elem+j] == "1":
                num+=1 
        if elem>=0+j:
            if board[elem-j] == "1":
                num+=1 
    if elem>0:
        if board[elem-1] == "1":
            num+=1 
    if elem<len(board)-1:
        if board[elem+1] == "1":
            num+=1
    return num
    
    
def update_world(board):
    world = board
    for i in range(0,len(board)):
        n=neighbours(board,i)
        if board[i] == "0":
            if n==3:
                try:
                    world = world[:i] + "1" + world[i+1:]
                except:
                    world = "1" + world[i+1:]
        elif board[i] == "1":
            if n<2 or n>3:
                try:
                    world = world[:i] + "0" + world[i+1:]
                except:
                    world = "0" + world[i+1:]
    return world

start = input()
while True:
    res = update_world(start)
    world = make_world(res)
    gen = gen_world(world)
    print("")
    print(gen)
    start = res
    time.sleep(1)
