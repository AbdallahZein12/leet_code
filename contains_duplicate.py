from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False
    

arr = [0,1,2,3]
hashset = set()

def answer(arr):
    for i in arr:
        if i in hashset:
            return True
        hashset.add(i)
        
    return False
    
print(answer(arr=arr))


####

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return Counter(nums).most_common(1)[0][1] > 1
    
solution = Solution()
print(solution.containsDuplicate(nums=[1,2,3,4,4]))
    
####


## Time O(n^2) Space O(1)
class containsDuplicate:
    def solution(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[:i] + nums[i+1:]:
                return True
        return False 
    
cls = containsDuplicate()
print(cls.solution(nums=[1,1,2,3,4,5]))

## Time O(n) Space O(n)
class containsDuplicate:
    def solution(self, nums: list[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False 
    
    
    
    
             
                
            