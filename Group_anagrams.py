
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        



        ans = []
        placeholder = {}
        for i in strs:
            sorted_anag = "".join(sorted(i))
            if sorted_anag in placeholder.keys():
                placeholder[sorted_anag].append(i)
            else:
                placeholder[sorted_anag] = []
                placeholder[sorted_anag].append(i)
        
        ans = [i for i in placeholder.values()]

        return ans 





##OTHER METHODS THAT DID WORK BUT WITH WORSE ALGO##

strs = ["","",""]





my_dict = {}

for i in strs:
    my_key = i 
    if my_key in my_dict:
        while my_key in my_dict:
            my_key += "_"
    my_dict[my_key] = "".join(sorted(i))
    


    
ans = []
place_holder = []
for i in strs:
    sorted_str = "".join(sorted(i))
    for key, value in my_dict.items():
        if value == sorted_str:
            key = key.replace("_","")
            place_holder.append(key)
            

        
    if place_holder in ans:
        pass 
    else:
        ans.append(place_holder)
    place_holder = []
    
print(ans)
            
            
###

strs = ["eat","tea","tan","ate","nat","bat"]

hashset = {}

for value in strs:
    if tuple(sorted(value)) in hashset:
        hashset[tuple(sorted(value))].append(value)
            
    else: 
        hashset[tuple(sorted(value))] = [value]

print(hashset)