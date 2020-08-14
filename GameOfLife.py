from collections import namedtuple, defaultdict
import time

Cell = namedtuple("Cell", ["x","y"])
    
def neighbours(cell):
    for x in range(cell.x-1, cell.x+2):
        for y in range(cell.y-1, cell.y+2):
            if (x, y) != (cell.x, cell.y):
                yield Cell(x, y)
    
def update_neighbours(board):
    update_neighbours = defaultdict(int)
    for cell in board:
        for neighbour in neighbours(cell):
            update_neighbours[neighbour] += 1
    return update_neighbours
    
def create_board(desc):
    board = set()
    for row, line in enumerate(desc.split("\n")):
        for col, elem in enumerate(line):
            if elem == "1":
                board.add(Cell(int(col), int(row)))
    return board
        
def update_board(board):
    new_board = set()
    for cell, count in update_neighbours(board).items():
        if count == 3 or (cell in board and count == 2):
            new_board.add(cell)
    return new_board        
                
def BoardToStr(board, n=0):
    if not board:
        return "end"
    board_str = ""
    xs = [x for (x,y) in board]
    ys = [y for (x,y) in board]
    for y in range(min(ys)-n, max(ys)+1+n):
        for x in range(min(xs)-n, max(xs)+1+n):
            board_str += "1" if Cell(x,y) in board else "0"
        board_str += "\n"
    return board_str.strip()
    
if __name__ == "__main__":
    gen = create_board("0000110\n1110010\n0000100\n0001000")
    for i in range(100):
        gen = update_board(gen)
        print(BoardToStr(gen, 2))
        time.sleep(0.1)
