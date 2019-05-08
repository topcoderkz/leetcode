class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def calc(i, j, n, m, grid):
            elems = []
            for k in range(i, n + 1):
                for f in range(j, m + 1):
                    elems.append(grid[k][f])
            
            m = collections.Counter(elems)
            for i in range(1, 10):
                if i not in m or m[i] > 1:
                    return 0
            
            saved_s = 0
            for i in range(3):
                s, j = 0, i
                while j < 9:
                    s += elems[j]
                    j += 3
                if i == 0:
                    saved_s = s
                elif saved_s != s:
                    return 0
            i = 0
            while i < 9:
                s = sum(elems[i : i + 3])
                if s != saved_s:
                    return 0
                i += 3
            
            i, s = 0, 0
            while i < 9:
                s += elems[i]
                i += 4
            if s != saved_s:
                return 0
            i, s = 2, 0
            while i < 7:
                s += elems[i]
                i += 2
            if s != saved_s:
                return 0
            return 1
            
        res = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[i]) - 2):
                res += calc(i, j, i + 2, j + 2, grid)
        return res
