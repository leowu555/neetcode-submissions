class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int a = 0; a < nums.length; a++) {
            for (int i = a + 1; i < nums.length; i++) {
                if (nums[a] == nums[i]) {
                    return true;
                }
            } 
        }
        return false;
    }
}