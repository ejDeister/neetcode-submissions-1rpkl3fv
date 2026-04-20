class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        dpth = 0
        maxdpth = 0
        def dfs(x,y):
            nonlocal dpth 
            if (x,y) in seen:
                return
            if y < 0 or y >= len(grid):
                return
            if x < 0 or x >= len(grid[0]):
                return
            if grid[y][x] == 0:
                return          
            seen.add((x,y))
            dpth += 1
            dfs(x,y-1)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x+1,y)

        
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                dpth = -1
                dfs(x,y)
                maxdpth = max(maxdpth,dpth+1)
        return maxdpth