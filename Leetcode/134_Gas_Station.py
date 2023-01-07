from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        start = 0
        remaining = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            remaining += gas[i] - cost[i]
            if remaining < 0:
                start = i + 1
                remaining = 0
        if total_gas < 0: 
            return -1
        return start

if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
    print(s.canCompleteCircuit([2,3,4], [3,4,3])) # -1