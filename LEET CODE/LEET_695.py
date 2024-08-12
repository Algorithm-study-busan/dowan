#아이디어
#1을 발견하면 탐색시작, 1의 상하좌우를 재귀적으로 탐색한다.
#1의 상하좌우 중, 0 or 범위밖 or 이미 탐색한 경우는 탐색을 종료한다.



class Solution:
    def maxAreaOfIsland(self, grid: list[List[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            # 범위를 벗어나거나 0  -> 종료
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            # 현재 셀을 방문한 것으로 표시
            grid[x][y] = 0
            area = 1
            # 상하좌우로 DFS 호출
            area += dfs(x + 1, y)
            area += dfs(x - 1, y)
            area += dfs(x, y + 1)
            area += dfs(x, y - 1)
            return area
        
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
