import copy
import time
def dfs(b, unfilled):
    if len(unfilled) == 0:
        return b
    un = sorted(unfilled.items(), key=lambda d:len(d[1]))
    # print(un)
    (x, y) = un[0][0]
    val = unfilled[(x,y)]
    print(x, y, val)
    if len(val) == 0:
        print("yes")
        return None
    u = copy.deepcopy(unfilled)
    del u[(x, y)]
    for a in val:
        c = copy.deepcopy(b)
        c[x][y] = a
        u = updateunfilled((x, y),c, u)
        d = dfs(c, u)
        if d != None:
            print("no")
            print(d)
            return d

        
def updateunfilled(coor, b, unfilled):
    (i, j) = coor
    block = []
    for m in range(i//3*3,(i//3+1)*3):
        for n in range(j//3*3,(j//3+1)*3):
            block.append((m,n))
    for (x, y) in unfilled.keys():
        if x == i or y == j or (x, y) in block:
            unfilled[(x, y)] = findval(b, x, y)
    return unfilled

def solveSudoku(board):
    uf = {}
    for x in range(9):
        for y in range(9):
            if board[x][y] == '.':
                uf[(x, y)] = findval(board, x, y)
    x = dfs(board, uf)
    for i in range(9):
        for j in range(9):
            board[i][j] = x[i][j]

def findval(b, i, j):
    result = set([str(x) for x in range(1,10)])
    for x in range(9):
        if b[i][x] != '.':
            if b[i][x] in result:
                result.remove(b[i][x])
        if b[x][j] != '.':
            if b[x][j] in result: 
                result.remove(b[x][j])
    m, n =i//3,j//3
    for x in range(3):
        for y in range(3):
            if b[m*3+x][n*3+y] != '.':
                if b[m*3+x][n*3+y] in result:
                    result.remove(b[m*3+x][n*3+y])
    return result


def main():
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    t = time.time()
    solveSudoku(board)
    print(time.time() - t)
    print(board)

if __name__ == "__main__":
    main()