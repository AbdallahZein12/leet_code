def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        placeholder = []
        hashset = set(nums)
        for i in hashset:
            placeholder.append((nums.count(i), i))
            
        placeholder.sort(key=lambda i: i[0], reverse=True)
        placeholder = placeholder[:k]
        
        ans = [i[1] for i in placeholder]
        return ans
        
            
        
    

        
        # my_keys = list(my_dict.keys())
        # my_keys.sort(reverse=True)
        # my_keys = my_keys[:k]
        
        # ans = [my_dict[i] for i in my_keys]
        
        # return ans 
    
topKFrequent([1,1,2],2)

