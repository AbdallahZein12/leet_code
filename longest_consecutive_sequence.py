class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        numset = set(nums)
        numset = sorted(numset)
        
        if not numset:
            return 0 

        i = 1
        max = 1
        sequence = 1
        
        while i < len(numset):
            prev_idx = i - 1
            if numset[i] - numset[prev_idx] == 1:
                sequence += 1
                i += 1 
                if i == len(numset):
                    if sequence > max:
                        max = sequence
            else:
                if sequence > max:
                    max = sequence
                sequence = 1
                i += 1
                
        return max
                
                
solution = Solution()
print(solution.longestConsecutive([1,2,0,1]))            
            
             
        
        