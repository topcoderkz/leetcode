class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        X = [[] for _ in range(len(A) - 1)]
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                X[i].append(A[j] - A[i])
        
        def index(elem, di):
            if elem in di:
                return di[elem]
            return -1

        d = [{} for _ in range(len(X))]
        for i in range(len(X)):
            for j, elem in enumerate(X[i]):
                if elem not in d[i]:
                    d[i][elem] = j
            
        ans = 0
        for i in range(len(X)):
            if ans >= len(X) - i + 1:
                break
            for j in range(len(X[i])):
                row = i + j + 1
                calc = 1
                while row <= len(X) - 1:
                    next_j = index(X[i][j], d[row])
                    if next_j == -1:
                        break
                    row += (next_j + 1)
                    calc += 1
                
                ans = max(ans, calc)
        return ans + 1
