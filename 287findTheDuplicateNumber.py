"""
problem 287 Find the Duplicate Number

Description:
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
1. You must not modify the array (assume the array is read only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than O(n2).
4. There is only one duplicate number in the array, but it could be repeated more than once.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
"""

#use array as hash table
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = [0] * len(nums)
        for num in nums:
            counter[num-1] += 1
            if counter[num-1] > 1:
                return num
        return None