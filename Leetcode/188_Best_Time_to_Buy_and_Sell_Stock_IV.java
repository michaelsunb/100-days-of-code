import java.util.ArrayList;
import java.util.List;

class Solution {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int k = 2;

        int[] prices = {2,4,1};
        System.out.println("Output: " + solution.maxProfit(k, prices));

        int[] newPrices = {3,2,6,5,0,3};
        System.out.println("Output: " + solution.maxProfit(k, newPrices)); 
    }
    public int maxProfit(int k, int[] prices) {
        if (prices.length == 0) {
            return 0;
        }
        int N = prices.length;
        int[] dp = new int[N];

        if (k > N) {
            List<Integer> B = new ArrayList<Integer>(); 
            for (int i = 1; i < N; i++) {
                B.add(i, prices[i]-prices[i-1]);
            } 
            int sum = 0;
            for (Integer b : B) {
                if (b > 0) {
                    sum += b;
                }
            }
            return sum;
        }

        for (int i = 0; i < k; i++) {
            int pos = -prices[0];
            int profit = 0;

            for (int j = 1; j < N; j++) {
                pos = Math.max(pos, dp[j]-prices[j]);
                profit = Math.max(profit, pos+prices[j]);
                dp[j] = profit;
            }
        }
        return dp[dp.length-1];
    }
}