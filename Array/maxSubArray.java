public class maxSubArray {

    /**
     * Given an integer array nums, find the contiguous subarray (containing at
     * least one number) which has the largest sum and return its sum. A subarray is
     * a contiguous part of an array.
     * 
     * Input: nums = [-2,1,-3,4,-1,2,1,-5,4] Output: 6 Explanation: [4,-1,2,1] has
     * the largest sum = 6.
     * 
     */

    public static void main(String[] args) {
        int[] arr = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        System.out.println(maxSubArray(arr));
    }

    public static int maxSubArray(int[] nums) {

        if (nums.length < 0 || nums == null) {
            return -1;
        }

        if (nums.length < 1) {
            return nums[0];
        }

        int minSum = nums[0];
        int maxSum = minSum;

        for (int i = 1; i < nums.length; i++) {
            minSum = Math.max(nums[i] + minSum, nums[i]);
            maxSum = Math.max(minSum, maxSum);
        }

        return maxSum;
    }

}