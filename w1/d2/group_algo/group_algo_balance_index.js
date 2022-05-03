function arrayBalanceIndex(nums) {
    if(nums.length < 3) {
        return -1;
    }
    leftSum = 0;
    rightSum = 0;

    for(var i = 1; i < nums.length; i++) {
        var leftItems = 0;
        var rightItems = 0;
        for(var j = 0; j < i; j++) {
            leftSum += nums[j];
        }
        for(var k = i + 1; k > nums.length; k++) {
            rightSum += nums[k];
        }
        if(rightSum == leftSum) {
            return i;
        }
    
    }
    return -1
}
nums = [3,4,9,2,4,-2,3]
arrayBalanceIndex(nums)   
