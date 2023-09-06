class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            if target-num in seen:
                return ([i,seen[target-num]])
            else:
                seen[num]=i
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

"""
Different approaches:
1. Brute force method iterating over arrays with two variables.
2. Sorting and two-pointers technique
    Let an array be {1, 4, 45, 6, 10, -8} and sum to find be 16
    After sorting the array 
    A = {-8, 1, 4, 6, 10, 45}
    Now, increment ‘l’ when the sum of the pair is less than the required sum and decrement ‘r’ when the sum of the pair is more than the required sum. 
    This is because when the sum is less than the required sum then to get the number which could increase the sum of pair, start moving from left to right(also sort the array) thus “l++” and vice versa.
    Initialize l = 0, r = 5 
    A[l] + A[r] ( -8 + 45) > 16 => decrement r. Now r = 4 
    A[l] + A[r] ( -8 + 10) increment l. Now l = 1 
    A[l] + A[r] ( 1 + 10) increment l. Now l = 2 
    A[l] + A[r] ( 4 + 10) increment l. Now l = 3 
    A[l] + A[r] ( 6 + 10) == 16 => Found candidates (return 1)
3. Hashing
    Follow the steps below to solve the problem:

    Initialize an empty hash table s.
    Do the following for each element A[i] in A[] 
    If s[x – A[i]] is set then print the pair (A[i], x – A[i])
    Insert A[i] into s.
"""
