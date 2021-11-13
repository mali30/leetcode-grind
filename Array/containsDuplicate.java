import java.util.HashSet;

public class containsDuplicate {

    /**
     * Given an integer array nums, return true if any value appears at least twice
     * in the array, and return false if every element is distinct.
     * 
     *  Input: nums = [1,2,3,1]
     *  Output: true
     */

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 1 };
        System.out.println(containsDuplicate(arr));

    }

    public static boolean containsDuplicate(int[] arr) {

        if (arr.length < 0 || arr == null) {
            return false;
        }

        HashSet<Integer> set = new HashSet<>();

        for (int i = 0; i < arr.length; i++) {
            if (set.contains(arr[i])) {
                return true;
            } else {
                set.add(arr[i]);
            }
        }

        return false;
    }

}