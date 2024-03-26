hash = set(nums)

for i in hash:
    if nums.count(i) > 1:
        indexi = nums.index(i)
        indexj = nums.index(i, indexi+1)