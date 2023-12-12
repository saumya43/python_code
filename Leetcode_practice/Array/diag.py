ROWS = 4
COLS = 4


for r in range(ROWS):
    for c in range(COLS):
        if r==c:
            print('diag')
            print(r,c)
       
        if r+c == ROWS -1:
            print('counter diag')
            print(r,c)
