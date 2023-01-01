var minPairSum = function(nums) {
    var sums = 0;
    nums.sort((a, b)=>a-b);
    for (let index = 0; index < nums.length / 2; index++){
        sums = Math.max(sums, (nums[index] + nums[nums.length - 1 - index]));
    }
    return sums;
    
};
