class Solution:      
    def dfs(self, grid,i,j):
        row = len(grid)
        col = len(grid[0])
        
        if grid[i][j] == '1':
            grid[i][j] = '0'

            #check connected for lands
            if i-1 >= 0:
                self.dfs(grid,i-1,j)
            if i + 1 < row:
                self.dfs(grid,i+1,j)
            if j-1 >= 0:
                self.dfs(grid,i,j-1)
            if j + 1 < col:
                self.dfs(grid,i,j+1)
                
    def numIslands(self, grid: List[List[str]]) -> int:
        #lands = set()
        count = 0
        row = len(grid)
        col = len(grid[0])
                
        for i in range(row):
            for j in range(col):
                # found land
                if grid[i][j] == '1':
                    count += 1
                    #sink other land connected
                    self.dfs(grid,i,j)
        return count
