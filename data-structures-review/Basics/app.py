# my_list = [-2,3,2,-1]

# # Maximum Sub Array Problem
# # Time is O(N)
# def kadaneAlgo(an_array):
#     start = 0
#     max_start = an_array[0]
#     for val in range(1, len(an_array) - 1):
#         start = max(an_array[start], an_array[start] + an_array[val])
#         if start > max_start:
#             max_start = start
#     return max_start

# print(kadaneAlgo(my_list))

# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.



# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# def longest_substring_with_k_distinct(str1, k):

#   left, maxSub = 0, 0
#   hashMap = {}

#   for right in range(len(str1)):
#     current = str1[right]

#     if current not in hashMap:
#       hashMap[current] = 0
#     hashMap[current] += 1
  

#     while len(hashMap) > k:
#       leftChar = str1[left]
#       hashMap[leftChar] -= 1

#       if hashMap[leftChar] == 0:
#         del hashMap[leftChar]
#       left += 1
  
#     maxSub = max(maxSub, right - left + 1)

#   return maxSub
    

# def max_sub_array_of_size_k(k, arr):
 
#  if k is None or arr is None:
#    return -1
 
#  left, maxSum, current = 0, 0, 0
 
#  for right in range(len(arr)):
#    # calculating sum as we move through our array for k elements
#    current += arr[right]
 
#  # met the condition to stop expanding
#    if right > k - 1:
#      current -= arr[left]
#      left += 1
#    maxSum = max(maxSum, current)
 
#  return maxSum




# def partition(arr, k):
#   if arr is None or len(arr) == 0:
#     return []
  

#   start, end = 0, len(arr) - 1
#   pointer = 0

#   while pointer < end:
#     curr = arr[pointer]

#     while curr < k:
#       while arr[traversal]
#       arr[curr], arr[pointer] = arr[end], arr[]
  

def lengthOfLastWord(s: str) -> int:

        
  """
  how do you know your on last word
  loop through word.
  for every character keep a count
  when you see a space updae the maxWord variable to be max(maxWord, currWordLength)
  
  """

  if s is None:
    return -1
  
  currCount = 0
  maxSoFar = float('-inf')
    
  for element in s:
      if element != " ":
          currCount += 1
      
      if element == " ":
          currCount = 0
      maxSoFar = currCount 

  return maxSoFar
        


print(lengthOfLastWord("luffy is still joyboy"))