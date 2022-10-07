package Euler;

class Solution {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.printf("Output: %d\n", solution.findProductOfABC(12));
        System.out.printf("Output: %d\n", solution.findProductOfABC(1000));
    }
    
    public int findProductOfABC(int sumOfABC) {
        for (int a = 1; a < (sumOfABC - 2); a++) {
            for (int b = a + 1; b < (sumOfABC - 2); b++) {
                double cSquare = Math.pow(a, 2) + Math.pow(b, 2);
                double c = Math.sqrt(cSquare);

                if (c % 1 == 0 && ((a + b + c) == sumOfABC)) {
                    System.out.printf("a: %d \nb: %d \nc: %d \n", a, b, (int) c);
                    return (int) (a * b * c);
                }
            }
        }
        
        return 0;
    }
}