function findSM(low, high) {
    for (let i = high; i <= (high * low); i += high) {
        if (i % low === 0) {
            return i;
        }
    }
    return 0;
}

function smallestMultiple(arr) {
    let low = Math.min(...arr);
    let high = Math.max(...arr);
    let sm = findSM(low, high);

    for (let x = low; x < high; x++) {
        if (sm % x !== 0) {
            sm = findSM(sm, x);
        }
    }
    return sm;
}

console.log(smallestMultiple([1,4]));