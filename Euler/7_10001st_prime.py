class Solution:
    def nthPrimeNumber(self, n: int) -> int:
        primes = [2, 3]
        if n < 3:
            return primes[n-1]
        count = 3
        num = 3
        isPrime = True

        while len(primes) < n:
            # There are no even numbers that is prime after 2
            num += 2
            # Since every even number is skipped
            # We can iterate from mapped primes
            # to check if they are prime or composite
            for i in primes:
                if i >= int(num/2)+1:
                    break
                # If num is divisible by any number between
                # 2 and num / 2, it is not prime
                if (num % i) == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(num)
            if len(primes) == n:
                return num
            isPrime = True # Reset to True
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.nthPrimeNumber(6))      # 13
    print(s.nthPrimeNumber(10001))  # 104743