class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalVal = 1
        isZero = False
        c = 0
        if all(i == 0 for i in nums):
            print(1)
            return nums
        for i in nums:
            if i == 0:
                isZero = True
                c += 1
                continue
            totalVal *= i
        nums1 = []
        print(totalVal, isZero)
        for i in nums:
            if isZero:
                if i == 0 and c <= 1: 
                    nums1.append(totalVal)
                else:
                    nums1.append(0)
            else:
                nums1.append(int(totalVal/i))
        return nums1

# Question
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Input: nums = [0,0,3]
Output: [0,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""
