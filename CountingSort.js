function countingSort(arr) {
    let frequencyArr = [];
    for (let i =0; i < 100; i++) {
        frequencyArr.push(0);
    }
    for (let num of arr){
        frequencyArr[num] += 1
    }
    return frequencyArr

}
