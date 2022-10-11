/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var increasingTriplet = function(nums) {
    if (nums.length < 3) return false;
    let i = Number.MAX_VALUE;
    let j = Number.MAX_VALUE;
    for (let x = 0; x < nums.length; x++) {
        if (nums[x] <= i) i = nums[x];
        else if (nums[x] <= j) j = nums[x];
        else return true;
    }
    return false;
};
console.log(increasingTriplet([5,4,3,2,1]));         // false
console.log(increasingTriplet([2,1,5,0,4,6]));       // true
console.log(increasingTriplet([20,100,10,12,5,13])); // true
console.log(increasingTriplet([5,1,6]));             // false
console.log(increasingTriplet([1,2,1,3]));           // true