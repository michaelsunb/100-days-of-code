<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function largestPerimeter($nums) {
        sort($nums);
        for ($i = count($nums)-3; $i >= 0 ; $i--) { 
            if ($nums[$i] + $nums[$i+1] > $nums[$i+2]) {
                return $nums[$i] + $nums[$i+1] + $nums[$i+2];
            }
        }
        return 0;
    }
}

$s = new Solution();
echo $s->largestPerimeter([2,1,2]);
echo "\n----------\n";
echo $s->largestPerimeter([1,2,1]);
echo "\n----------\n";