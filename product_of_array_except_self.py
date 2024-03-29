class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
###

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [1] * length
        left = [1] * length
        right = [1] * length

        left[0] = 1
        for i in range(1,length):
            left[i] = left[i-1] * nums[i-1]

        right[-1] = 1
        for i in range(length-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]

        answer = [x * y for x,y in zip(left,right)]

        return answer
