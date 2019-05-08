class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        d = [[1,0],[0,1],[0,-1],[-1,0]]
        
        def inside(x, y, n, m):
            return (x >= 0 and x < n and y >= 0 and y < m)
        
        def border(x, y, d, n, m):
            for i in range(len(d)):
                if not inside(x + d[i][0], y + d[i][1], n, m):
                    return True
                if not visited[x + d[i][0]][y + d[i][1]]:
                    return True
            return False
            
        visited = []
        for i in range(len(grid)):
            visited.append([])
            for j in range(len(grid[i])):
                visited[i].append(False)
        
        def dfs(x, y):
            if visited[x][y]:
                return
            visited[x][y] = True
            for i in range(len(d)):
                n_x, n_y = x + d[i][0], y + d[i][1]
                if inside(n_x, n_y, len(grid), len(grid[0])) and grid[x][y] == grid[n_x][n_y]:
                    dfs(n_x, n_y)
            
        dfs(r0, c0)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j] and border(i, j, d, len(grid), len(grid[0])):
                    grid[i][j] = color
        
        return grid
