# Python - 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:     
        return False if len(nums) == len(set(nums)) else True
