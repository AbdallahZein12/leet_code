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
            