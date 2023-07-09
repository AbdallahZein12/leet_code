arr = [1633,2181,7558,2650,1920,809,4903,2223,4271,4110,7564,5428,1730,5970,9640,3185,7564,5040,4344,9479,2070,6569,9849,73,2961,7991,9419,7946,3293,882,4714,3813,278,6121,9244,8248,5424,2377,4270,7656,1983,2928,2876,4746,129,5971,522,349,1239,9493,4777,1421,1763,8419,5696,726,6130,9164,5290,6793,3670,3090,3395,5597,7557,6246,956,7791,677,2284,7280,5309,8274,1760,2383,7003,4094,1681,8885,3010,1551,7419,813,9937,7054,9615,8126,2739,3255,334,587,634,3382,3316,4630,6077,4687,2226,8910,8357,1961,1454,6416,8838,6295,4523,9736,6165,2849,7877]
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.sort()
        d={}
        for i in arr:
            count = bin(i).count('1')
            if count not in d:
                d[count] = [i]
            else:
                d[count].append(i)
        res=[]
        for i in sorted(d.keys()):
            res.extend(d[i])

        return res







# list_of_binary = list(map(lambda item: bin(item)[2:], arr))

# list_of_added_ones = [i.count('1') for i in list_of_binary]

# zipped = list(zip(arr,list_of_added_ones))

# sorted_zipped = sorted(zipped, key=lambda i: i[1])

# answer = [i[0] for i in sorted_zipped]


