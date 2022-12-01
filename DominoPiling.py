def domino():
    dimension = input()
    nums = dimension.split(" ")
    return (int(nums[0]) * int(nums[1])) // 2


print(domino())
