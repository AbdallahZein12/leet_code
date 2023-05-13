class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans = nums[i] + nums[j]
                if ans == target:
                    return[i,j]


          
          
          
            # if bro in nums:
            #     for j in range(len(nums)-1,-1,-1):
            #         if j == bro:
            #             return[nums.index(i),nums.index(j)]
            
            
####OTHER METHOD###

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d:
                return [d[r], i]
            d[j] = i
            