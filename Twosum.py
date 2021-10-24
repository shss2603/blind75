"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
"""
Python lists have the power of in keyword because of which we do not need to create a hashmap. 
We can just search the difference between the target and each iterated element of the list in the remaining list. 
In other languages, you would need to save the list of numbers in a hashmap to search.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return i,nums[i+1:].index(target-nums[i])+(i+1)
