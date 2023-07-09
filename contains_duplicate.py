arr = [0,1,2,3]
hashset = set()

def answer(arr):
    for i in arr:
        if i in hashset:
            return True
        else:
            hashset.add(i)
        
    return False
    
print(answer(arr=arr))