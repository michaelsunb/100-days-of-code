class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dice = n
        face = k
        dp = [[0] * (target+1) for _ in range(dice+1)]
        dp[0][0] = 1

        for d in range(1, dice+1):
            for t in range(1, target+1):
                for f in range(1, min(t, face)+1):
                    dp[d][t] += dp[d-1][t-f]
        return dp[dice][target] % (10**9 + 7)


if __name__ == "__main__":
    s = Solution()
    print(s.numRollsToTarget(1, 6, 3))
    print(s.numRollsToTarget(2, 6, 12))
    print(s.numRollsToTarget(30, 30, 500))