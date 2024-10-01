#Find the length of the shortest path from top left of the grid to the bottom right.
from collections import deque
def bfs(grid):
    ROWS, COLS = len(grid) , len(grid[0])
    visit = set()
    q = deque()
    q.append((0,0))
    visit.add((0,0))
    length = 0
    while q:
        for i in range(len(q)):
            r, c =  q.popleft()
            if r == ROWS - 1 and c == COLS - 1:
               return length
            neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbours:
                if ( min(r+dr, c+dc) < 0 or r + dr == ROWS or c+dc == COLS or (r+dr, c+dc) in visit or grid[r+dr][c+dc] == 1 ):
                    continue
                visit.add((dr+r,dc+c))
                q.append((dr+r, dc+c))
        length += 1

print (bfs([[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]))
