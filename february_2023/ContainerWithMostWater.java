class Solution {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length - 1;
        List<Integer> areas = new ArrayList<>();
        int counter = 0;
        while (i != j){
            int area = Math.min(height[i], height[j]) * (j - i);
            areas.add(area);
            if (height[i] > height[j]){
                j -= 1;
            }
            else {
                i += 1;
            }
            counter += 1;
        }
        int max = 0;
        for (int num : areas){
            if (num > max){
                max = num;
            }
        }
        return max;
    }
}
