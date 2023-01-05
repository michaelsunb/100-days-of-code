import java.util.Arrays;

class Solution {
    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][] points1 = {{1,2},{3,4},{5,6},{7,8}};
        System.out.println("Output: " + solution.findMinArrowShots(points1)); // 4
        int[][] points2 = {{10,16},{2,8},{1,6},{7,12}};
        System.out.println("Output: " + solution.findMinArrowShots(points2)); // 2
        int[][] points3 = {{1,2},{4,5},{1,5}};
        System.out.println("Output: " + solution.findMinArrowShots(points3)); // 2
    }

    public int findMinArrowShots(int[][] points) {
        // intially arrow will be 1 (see constraint 1 <= points.length <= 10^5)
        // atleast 1 ballon will be required so, arrow = 1
        
        int result = 1; // we will require atleast 1 arrow to burst the ballons
        
        // as we said, sort it on the basis of starting point
        Arrays.sort(points, (a, b) -> Integer.compare(a[0],b[0]));
        
        //intially start and end position will be of zero index
        int start = points[0][0];
        int end = points[0][1];
        
         // Run the loop i.e from (1 to n)
        for(int i = 1; i < points.length; i++)
        {
            if(points[i][0] > end) // active set and ith index interval does not overlap
            {
                // so we have to create new active set
                start = points[i][0];
                end = points[i][1];
                
                result++; // and also now we need one more arrow
            }
            else // if  active set and ith index interval does overlap
            {
                // we just rearranging our active set
                start = Math.max(start, points[i][0]);
                end = Math.min(end, points[i][1]);
            }
        }
        
        return result; // finally, loop ends return count of arrow
    }
}