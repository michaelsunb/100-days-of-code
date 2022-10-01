/**
 * @param {string} s
 * @return {number}
 */
 var numDecodings = function(s) {
    const len = s.length
    let dp = [];
    dp.length = len;
    dp[len] = 1;

    const dfs = function(index) {
        if (dp[index] !== undefined) {
            return dp[index];
        }
        if (s[index] === "0") {
            return 0;
        }

        let res = dfs(index + 1);
        if ((index + 1) < len && 
        (s[index] === "1" || 
        (s[index] === "2" && s[index + 1].match(/[0-6]/))
        )) {
          res += dfs(index + 2);  
        }
        dp[index] = res;
        return res;
    }
    return dfs(0);
};

console.log(numDecodings("12"));
console.log(numDecodings("226"));
console.log(numDecodings("06"));