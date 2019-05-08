class Solution:
    def get_max(self, que: List[tuple], x: int, y: int) -> int:
        if not que:
            return 0
        res = 0
        for elem in que:
            i, j, val = elem[0], elem[1], elem[2]
            if i < x and j < y and val > res:
                res = val
        return res
                
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        que = []
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    que.append((i, j, self.get_max(que, i, j) + 1))
    
        return self.get_max(que, len(A) + 1, len(B) + 1)
