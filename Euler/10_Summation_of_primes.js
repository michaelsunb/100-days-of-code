function isPrime(num) {
    if (num % 2 === 0) {
        return false
    }
    for (let i = 3; i < Math.sqrt(num)+1; i = i+2) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}

function sumPrimeBelow(n) {
    if (n <= 0) throw 'n must be a positive number!';
    if (n == 1) return 0;
    if (n == 2) return 2;

    let sum = 2;

    for (let i = 3; i <= n; i = i+2) {
        if (isPrime(i)) {
            sum += i;
        }
    }
    return sum;
}

console.log(sumPrimeBelow(10));
console.log(sumPrimeBelow(2000000));