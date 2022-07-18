class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        globalMax = 0;
        curMax = 0;
        maxI = len(grid)
        maxJ = len(grid[0])
        def bfs(i:int, j:int) -> None:
            nonlocal curMax 
            if(grid[i][j] == 1):
                curMax += 1
            else:
                return
            
            grid[i][j] = -1
            if(j + 1 < maxJ and grid[i][j + 1] == 1):
                bfs(i, j + 1)
            if(i + 1 < maxI and grid[i+1][j] == 1):
                bfs(i + 1, j)
            if(j - 1 >= 0 and grid[i][j - 1] == 1):
                bfs(i, j - 1)
            if(i - 1 >= 0 and grid[i - 1][j] == 1):
                bfs(i - 1, j)
            return
        for i in range(maxI):
            for j in range(maxJ):
                if(grid[i][j] == 1):
                    bfs(i, j)
                    globalMax = max(globalMax, curMax)
                    curMax = 0
        return globalMax