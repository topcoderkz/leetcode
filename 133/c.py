class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, R: int) -> int:
        def okay(l, r):
            l1, r1 = l[1], l[2]
            l2, r2 = r[1], r[2]
            return r1 < l2 or r2 < l1
        s = list(itertools.accumulate(A))
        ls = [] 
        for i in range(L - 1, len(s)):
            if i - L >= 0:
                prev = s[i - L]
            else:
                prev = 0
            ls.append([s[i] - prev, i - L + 1, i])
            
                      
        rs = [] 
        for i in range(R - 1, len(s)):
            if i - R >= 0:
                prev = s[i - R]
            else:
                prev = 0
            rs.append([s[i] - prev, i - R + 1, i])
            
        ls = sorted(ls, reverse=True)
        rs = sorted(rs, reverse=True)
        
        res = 0
        for l in ls:
            for r in rs:
                if okay(l, r):
                    res = max(res, l[0] + r[0])
        return res
