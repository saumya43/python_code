# count the unique path from top left to the bottom right. A single path may 
# only move along 0s and cant visit the same cell more than onceß 
def dfs_matrix(grid, r, c, visit):

    ROWS, COLS = len(grid) , len(grid[0])
    if ( min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r,c))
    count = 0
    count += dfs_matrix(grid, r+1, c, visit)
    count += dfs_matrix(grid, r-1, c, visit)
    count += dfs_matrix(grid, r, c+1, visit)
    count += dfs_matrix(grid, r, c-1, visit)
    visit.remove((r,c))
    return count

    
print(dfs_matrix([[0,0,0,0],[1,1,0,0],[0,0,0,1],[0,1,0,0]], 0, 0, set()))

    
