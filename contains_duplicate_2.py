class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashset = {}
        for index, value in enumerate(nums):
            if value in hashset and abs(index - hashset[nums[index]])  <=k:
                return True

            hashset[nums[index]] = index
        return False