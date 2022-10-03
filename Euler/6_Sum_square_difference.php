<?php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    public function sumSquareDiffernce($num) {
        $squareOfSum = 0;
        $sum = 0;
        $res = 0;
        
        for ($i = 1; $i <= $num; $i++) {
            $squareOfSum += pow($i, 2);
            $sum += $i;
        }

        return pow($sum, 2) - $squareOfSum;
    }
}

$s = new Solution();
echo $s->sumSquareDiffernce(100,100);