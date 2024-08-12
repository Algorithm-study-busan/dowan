class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        def dfs(city):
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)  # 방문한 도시를 기록
                    dfs(neighbor)  # 인접한 도시를 계속 탐색


        visited = set()  # 방문한 도시를 추적하기 위한 집합
        provinces = 0

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)  # 방문하지 않은 도시에서 DFS 시작
                provinces += 1  # 새로운 프로빈스가 발견될 때마다 1씩 증가

        return provinces