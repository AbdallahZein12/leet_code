def solution():
    input1 = [0,1,0,3,12]
    
    for i in input1:
        if i == 0:
            input1.remove(i)
            input1.append(0)



####OTHER METHOD####

def solution():
    nums = [0,1,0,3,12]
    
    prev_idx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            hold = nums[prev_idx]
            nums[prev_idx] = nums[i]
            nums[i] = hold
            prev_idx+=1


            
        
            