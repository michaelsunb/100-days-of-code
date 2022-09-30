import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    private static final int MOD = 1_000_000_007;
    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 6;
        int[] speed1 = {2,10,3,1,5,8};
        int[] efficiency1 = {5,4,3,9,7,2};
        int k = 2;

        System.out.println("Output: " + solution.maxPerformance(n, speed1, efficiency1, k));

        n = 6;
        int[] speed2 = {2,10,3,1,5,8};
        int[] efficiency2 = {5,4,3,9,7,2};
        k = 3;

        System.out.println("Output: " + solution.maxPerformance(n, speed2, efficiency2, k));

        n = 6;
        int[] speed3 = {2,10,3,1,5,8};
        int[] efficiency3 = {5,4,3,9,7,2};
        k = 4;

        System.out.println("Output: " + solution.maxPerformance(n, speed3, efficiency3, k));
    }
    
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        long[][] matrix = new long[n][3];
        for(int i=0;i<n;i++){
            matrix[i][0] = efficiency[i];
            matrix[i][1] = speed[i];
        }
        Arrays.sort(matrix,(m1,m2)->(int)(m1[0]-m2[0]));
        Queue<Long> minHeap = new PriorityQueue<>();
        long maxSum = 0;
        for(int i=n-1;i>n-k;i--){
            maxSum += matrix[i][1];
            minHeap.offer(matrix[i][1]);
            matrix[i][2] = maxSum;
        }
        for(int i=n-k;i>=0;i--){
            matrix[i][2] = maxSum+matrix[i][1];
            if(!minHeap.isEmpty() && matrix[i][1]>minHeap.peek()){
                maxSum -= minHeap.remove();
                maxSum += matrix[i][1];
                minHeap.offer(matrix[i][1]);
            }
        }
        long max = 0L;
        for(int i=0;i<n;i++) max = Math.max(max,matrix[i][0]*matrix[i][2]);
        return (int)(max%MOD);
    }
}