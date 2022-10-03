/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
 var minCost = function(colors, neededTime) {
    let grpSum = 0;
    let grpMax = 0;
    let res = 0;

    for (let i = 0; i < colors.length; i++) {
        if (i > 0 && colors.charAt(i) !== colors.charAt(i - 1)) {
            res += grpSum - grpMax;
            grpMax = 0;
            grpSum = 0;
        }
        grpSum += neededTime[i];
        grpMax = Math.max(grpMax, neededTime[i]);
    }

    return (res + grpSum - grpMax);
};

console.log(minCost("abaac", [1,2,3,4,5]));
console.log(minCost("abc", [1,2,3]));
console.log(minCost("aabaa", [1,2,3,4,1]));