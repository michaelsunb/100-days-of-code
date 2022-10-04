class Solution:
    def nthPrimeNumber(self, n: int) -> int:
        num = 0
        count = 0

        if n <= 3:
            return n
        if n > 3:
            count = 3
            num = 3

        nonprime = False
        while count <= n+1:
            # There are no even numbers that is prime after 2
            num += 2
            # Iterate from 2 to n / 2
            for i in range(2, int(num/2)+1):
                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    nonprime = True
                    break
            if nonprime != 1:
                count += 1
            if count == n+1:
                return num
            nonprime = False
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.nthPrimeNumber(6))      # 13
    print(s.nthPrimeNumber(10001))  # 104743