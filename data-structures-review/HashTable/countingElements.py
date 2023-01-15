"""
iven an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

 

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
 

Constraints:

1 <= arr.length <= 1000
0 <= arr[i] <= 1000
"""

class Solution:
    # O(N^2) time
    def countingElements(self, nums):
        # under assumption its sorted array

        if nums is None:
            return -1

        counter = 0
        
        for element in range(0, len(nums) - 1):
    
                
            if nums[element] + 1 in nums:
                counter += 1
        
        return counter
    
    # O(N) time O(N) space
    def countingElementsImproved(self, nums):

        hashMap = {}
        counter = 0

        for item in nums:
            if item not in hashMap:
                hashMap[item] = 1
            hashMap[item] += 1
        
        for item in nums:
            if hashMap.get(item + 1, 0) > 0:
                counter += 1

        return counter 


sol = Solution()
print(sol.countingElementsImproved([1,2,3]))
print(sol.countingElementsImproved([1,1,3,3,5,5,7,7]))
