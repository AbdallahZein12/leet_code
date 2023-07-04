
list_of_sums = set()
def answer(n):
    while n not in list_of_sums:
        list_of_sums.add(n)
        n_split = str(n).strip()
        n_split = list(n_split)


        for i in range(len(n_split)):
            n_split[i] = int(n_split[i]) ** 2
            
        n = sum(n_split)
        if n == 1:
            return True
        
        
    return False


print(answer(55))



    
    