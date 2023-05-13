nums = [-1,0,2,1,3,0]
result = []


def solution():
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    result = [nums[i], nums[j], nums[k]]
                    return result

                

print(solution())