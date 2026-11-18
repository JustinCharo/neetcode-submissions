class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # decision: take i + 1 or i + 2 floor
        # optimal substructure
        # dp[i] = min of cost[i+1] or [i+2]
        # dp[i] = min{ dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]}
        # base is min (cost[0] or cost[1])
        # [1, 2, 3]
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]