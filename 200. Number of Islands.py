class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        w, h = len(grid), len(grid[0])
        
        def bfs(grid, i, j):
            if i<0 or i>=w or j<0 or j>=h or grid[i][j] != '1':
                return
            
            grid[i][j] = '2'
            
            bfs(grid, i+1, j)
            bfs(grid, i, j+1)
            bfs(grid, i-1, j)
            bfs(grid, i, j-1)
            
        
        def traversal(grid):
            nonlocal count
            for i in range(w):
                for j in range(h):
                    if grid[i][j] == '1':
                        count += 1
                        bfs(grid, i, j)
        
        traversal(grid)
        
        return count
