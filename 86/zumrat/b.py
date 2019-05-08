class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:        
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in rooms[i]:
                dfs(j)

        visited = set()
        dfs(0)
        n = 0
        for l in rooms:
            if l:
                n = max(n, max(l))
        for i in range(n + 1):
            if i not in visited:
                return False
        return True
