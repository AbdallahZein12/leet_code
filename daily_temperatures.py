
### O(n)

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackInd = stack.pop()[1]
                res[stackInd] = i-stackInd
            stack.append([t,i])

        return res


### O(n^2) DO NOT USE

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        idx = 1
        init_val = 0 
        dist = 0

        while init_val < len(temperatures):
            if idx >= len(temperatures):
                init_val += 1 
                idx = init_val + 1
                
            elif temperatures[idx] > temperatures[init_val]:
                dist = idx-init_val
                res[init_val] = dist
                dist = 0
                init_val += 1 
                idx = init_val + 1

            else:
                idx += 1 

        


        # if len(res) != len(temperatures):
        #     res.extend([0] * (len(temperatures) - len(res)))

        return res