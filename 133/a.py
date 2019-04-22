class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def dist(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        x = []
        for i in range(R):
            for j in range(C):
                x.append((dist(i, j, r0, c0), i, j))
        
        return [[elem[1], elem[2]] for elem in sorted(x)]
