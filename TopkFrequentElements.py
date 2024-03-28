from collections import Counter

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


########## Different Solution

nums = [1,2]
k=2
hset = set(nums)

hdict = {}

for i in hset:
    hdict[i] = nums.count(i)
    

sorted_hdict = sorted(hdict.items(), key=lambda x: x[1])


ans = [i[0] for i in sorted_hdict[-k:]]


###### Shortest solution

counter = Counter(nums)
print([num for num, _ in counter.most_common(k)])

