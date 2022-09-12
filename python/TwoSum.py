
1. Two Sum

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

Soluntion : 
##create a dictionary
##use remaing and check if the number is not there in the dictionary, then append value and i
## else return the index of the remaining and i 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()        
        for i , value in enumerate(nums):
            remaining = target - value
            if remaining not in d:            
                d[value] = i
            else:
                return [d[remaining],i]
