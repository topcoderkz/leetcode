class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a,b,c = sorted([a,b,c])
        if a + 1 == b and b + 1 == c:
            return [0,0]
        if a + 1 == b and b + 1 < c:
            return [1, c - b - 1]
        if a + 1 < b and b + 1 == c:
            return [1, b - a - 1]
        if a + 1 < b and b + 1 < c:
            if a + 2 == b or b + 2 == c:
                return [1, b - a - 1 + c - b - 1]
            return [2, b - a - 1 + c - b - 1]
