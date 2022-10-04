class Solution:
    def nthPrimeNumber(self, n: int) -> int:
        num = 0
        count = 0
        nonprime = 0
        while count <= n+1:
            num += 1
            # Iterate from 2 to n / 2
            for i in range(2, int(num/2)+1):
                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    nonprime = 1
                    break
            if nonprime == 1:
                nonprime = 0
            else:
                count += 1
            if count == n+1:
                return num
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.nthPrimeNumber(6))      # 13
    print(s.nthPrimeNumber(10001))  # 104743