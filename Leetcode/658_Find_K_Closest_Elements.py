from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # l, r = 0, len(arr) - k
        left = 0
        right = len(arr) - k

        while left < right:
            m = (left + right) // 2
            if x - arr[m] > arr[m + k] - x:
                left = m + 1
            else:
                right = m

        return arr[left:left+k]

if __name__ == "__main__":
    s = Solution()
    print(s.findClosestElements([1,2,3,4,5], 4, 3))
    print(s.findClosestElements([1,2,3,4,5], 4, -1))