def Soultion(target, nums):
    for x in nums:
        for i in nums:
            if target - i == x:
                print(nums.index(i), nums.index(x))
            else:
                pass
