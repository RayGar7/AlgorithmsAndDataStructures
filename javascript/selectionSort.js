// implements selection sort
function mySort(arr) {
    // create a shallow copy of arr (so as to not override the original array and return a totally new array)
    let sortedArr = [...arr];
    
    for (let i = 0; i < sortedArr.length; i++) {
        let min = i;
        for (let j = i + 1; j < sortedArr.length; j++) {
            if (sortedArr[min] > sortedArr[j]) {
                min = j;
            }
        }
        if (min !== i) {
            swap(sortedArr, min, i);
        }
    }
    return sortedArr;
}

// todo import from a module
function swap(arr, a, b) {
    let temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}