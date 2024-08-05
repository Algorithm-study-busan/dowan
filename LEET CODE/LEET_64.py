class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)] 
        #dp = [[0]*n]*m 배열복사하면 주소가 복사되서 오류남

        dp[0][0] = grid[0][0]

        for i in range(1,n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for row in range(1,m):
            for col in range(1,n):

                dp[row][col] = min(dp[row][col-1]+grid[row][col],dp[row-1][col]+grid[row][col])

        print(dp)
        return dp[m-1][n-1]