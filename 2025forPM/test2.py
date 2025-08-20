def prdct(nums):
    res = 1
    for val in nums:
        res *= val
    return res
def test(nums):
    res = [1 for i in nums]
    for i in range(len(nums)):
        if i == 0 or i+1 >= len(nums):
            continue
        else:
            res[i+1] = res[i-1] * nums[i]
    print(res)

    for i in range(len(nums)-1,-1,-1):
        print(nums[i])



nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]

test(nums)