from typing import List
from math import sqrt

class Solution:
    def findFirstTriangularNumberOverX(self, overX: int) -> int:
        half = overX / 2
        squared = half * half
        start = sqrt(squared)

        numOfDivisors = 0
        trianglarNumber = 0
        i = start
        while numOfDivisors < overX:
            trianglarNumber = self.nthTriangularNumber(i)
            numOfDivisors = self.findNoOfDivisors(trianglarNumber)
            i=i+1
        
        return trianglarNumber

    def nthTriangularNumber(self, n: int) -> int:
        return int(((n*n+n) / 2))

    def findNoOfDivisors(self, triangularNumber: int) -> int:
        factors = []
        temp = 0
        for a in range(1, int(sqrt(triangularNumber))):
            if triangularNumber % a == 0:
                factors.append(a)
                temp = triangularNumber / a
                if a != temp:
                    factors.append(temp)
        return len(factors)


if __name__ == "__main__":
    s = Solution()
    print(s.findFirstTriangularNumberOverX(6)) # 28
    print(s.findFirstTriangularNumberOverX(500)) # 76576500

# package Euler;
# import java.util.ArrayList;
# import java.util.List;
# class Solution {
#     public static void main(String[] args) {
#         Solution solution = new Solution();
#         System.out.printf("Expect %d, got: %d\n", 1, solution.findNoOfDivisors(1));
#         System.out.printf("Expect %d, got: %d\n", 2, solution.findNoOfDivisors(3));
#         System.out.printf("Expect %d, got: %d\n", 4, solution.findNoOfDivisors(6));
#         System.out.printf("Expect %d, got: %d\n", 4, solution.findNoOfDivisors(10));
#         System.out.printf("Expect %d, got: %d\n", 4, solution.findNoOfDivisors(15));
#         System.out.printf("Expect %d, got: %d\n", 4, solution.findNoOfDivisors(21));
#         System.out.printf("Expect %d, got: %d\n", 6, solution.findNoOfDivisors(28));
#         System.out.printf("Result: %d\n", solution.findFirstTriangularNumberOverX(6));
#         System.out.printf("Result: %d\n", solution.findFirstTriangularNumberOverX(500));
#     }
#     /**
#      * @param overX
#      * @return (int) first Triangular Number over param
#      */
#     public int findFirstTriangularNumberOverX(int overX) {
#         int half = overX / 2;
#         int squared = half * half;
#         int start = (int) Math.sqrt(squared);
#         int numOfDivisors = 0;
#         int trianglarNumber = 0;
#         for (int i = start; numOfDivisors < overX; i++) {
#             trianglarNumber = this.nthTriangularNumber(i);
#             numOfDivisors = this.findNoOfDivisors(trianglarNumber);
#         } 
#         return trianglarNumber;
#     }
#     /**
#      * (n(n+1))/2
#      * @param factorResult
#      * @return (int)
#      */
#     public int nthTriangularNumber(int n) {
#         return (int)((n*n+n) / 2);
#     }
#     /**
#      * @param triangularNumber
#      * @return int
#      */
#     public int findNoOfDivisors(int triangularNumber) {
#         List<Integer> factors = new ArrayList<Integer>();
#         int temp = 0;
#         for (int a = 1; a <= Math.sqrt(triangularNumber); a++) {
#             if (triangularNumber % a == 0) {
# 				factors.add(a);
#                 /**
#                  * if input is 24 and:
#                  * a is 1 then 24 / 1 = 24 which would be the otherside of the factor
#                  * a is 2 then 24 / 2 = 12 which would be the otherside of the factor
#                  * a is 3 then 24 / 3 = 8 which would be the otherside of the factor
#                  * a is 4 then 24 / 4 = 6 which would be the otherside of the factor
#                  * a is 5 then 24 / 5 = 4.8 but 5 is not a factor so no otherside
#                  * and 5 is greater than Math.sqrt(24) so loop would have already broke by then
#                  */
# 				temp = triangularNumber / a;
# 				if (a != temp) {
# 					factors.add(temp);
# 				}
#             }
#         }
#         return factors.size();
#     }
# }