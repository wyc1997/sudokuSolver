import copy
import time
def helper(b, unfilled):
    if len(unfilled) == 0:
        return b
    (i, j) = unfilled[0]
    
    val = [str(x) for x in range(1,10)]
    for x in range(9):
        if b[i][x] != '.':
            if b[i][x] in val:
                val.remove(b[i][x])
        if b[x][j] != '.':
            if b[x][j] in val:
                val.remove(b[x][j])
    m,n = int(i/3), int(j/3)
    for x in range(3):
        for y in range(3):
            if b[m*3+x][n*3+y] != '.':
                if b[m*3+x][n*3+y] in val:
                    val.remove(b[m*3+x][n*3+y])
    
    print(i, j, val)
    if len(val) == 0:
        print("yes")
        return None
    result = []
    for x in val:
        c = copy.deepcopy(b)
        c[i][j] = x
        u = copy.deepcopy(unfilled)
        u = u[1:]
        result.append(helper(c, u))
    for x in result:
        if x != None:
            print("NONONONONOOONNOONONOONON")
            # print(x)
            return x
    return None

def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    uf = []
    for x in range(9):
        for y in range(9):
            if board[x][y] == '.':
                uf.append((x,y))

    board = helper(board, uf)
    print(board)

def main():
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    t = time.time()
    solveSudoku(board)
    print(time.time() - t)
    print(board)

if __name__ == "__main__":
    main()