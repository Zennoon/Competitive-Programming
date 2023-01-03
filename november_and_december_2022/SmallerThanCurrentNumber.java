class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
       int[] result = new int[nums.length];
        int index = 0;
        for (int num : nums){
        int counter = 0;
            for (int otherNum : nums){
                if (otherNum < num){
                    counter += 1;
                }
            }
            result[index] = counter;
            index += 1;
            
        }
        return result;
    }
}
