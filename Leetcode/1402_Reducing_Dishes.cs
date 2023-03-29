using System;

class Solution {
    static void Main(string[] args) {
        Solution solution = new Solution();
        Console.WriteLine(solution.MaxSatisfaction(new int[] {-1, -8, 0, 5, -9}));  // Output: 14
        Console.WriteLine(solution.MaxSatisfaction(new int[] {4, 3, 2}));  // Output: 20
        Console.WriteLine(solution.MaxSatisfaction(new int[] {-1, -4, -5}));  // Output: 0
    }
    
    public int MaxSatisfaction(int[] satisfaction) {
        // Sort the satisfaction array in non-decreasing order
        Array.Sort(satisfaction);
        
        // Initialize the maximum sum of like-time coefficient and current sum to 0
        int max_sum = 0;
        int current_sum = 0;
        
        // Iterate through the satisfaction array in reverse order
        for (int i = satisfaction.Length - 1; i >= 0; i--) {
            // Calculate the like-time coefficient
            int like_time_coefficient = current_sum + satisfaction[i];
            
            // If the like-time coefficient is positive, update the current sum and maximum sum
            if (like_time_coefficient > 0) {
                current_sum += satisfaction[i];
                max_sum += like_time_coefficient;
            }
            // Otherwise, stop iterating as the dishes will not increase the maximum sum
            else {
                break;
            }
        }
        
        return max_sum;
    }
}