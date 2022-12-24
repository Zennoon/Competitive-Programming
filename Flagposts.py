    import math
    def flagport():
        dimension = input()
        nums = dimension.split(" ")
        m = int(nums[0])
        n = int(nums[1])
        a = int(nums[2])
        return math.ceil(m / a) * math.ceil(n / a)
     
    print(flagport())

