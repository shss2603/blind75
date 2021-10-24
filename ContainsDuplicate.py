"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

"""
In python we can use the concept of sets as they contain only unique elements. If there are duplicates, the length of set of list nums won't be equal to length of nums. 
Another concept is using hashmaps which make it easy to search.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       return len(set(nums))!=len(nums) 
