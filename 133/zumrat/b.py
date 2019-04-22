class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for cost in costs:
            cost.insert(0, max(cost) - min(cost))
        
        costs = sorted(costs, reverse=True)
        n = m = len(costs) // 2
        res = 0
        for cost in costs:
            if cost[1] < cost[2]:
                if n > 0:
                    n -= 1
                    res += cost[1]
                else:
                    m -= 1
                    res += cost[2]
            elif m > 0:
                m -= 1
                res += cost[2]
            else:
                n -= 1
                res += cost[1]

        return res
