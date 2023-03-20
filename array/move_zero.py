"""Move all zeros present in an array to the end
Given an integer array, move all zeros present in it to the end. 
The solution should maintain the relative order of items in the array and should not use constant space."""


nums = [6, 0, 8, 2, 3, 0, 4, 0, 1]

def move_zero1(nums: list):

    
    for i, num in enumerate(nums):
        if num == 0:
            ls = range(i, len(nums) -1)
            for n in ls:
                nums[n] = nums[n+1]
            nums[-1] = 0
    print(nums)


def move_zero2(nums):

    k = 0
    for num in nums:
        if num:
            nums[k] = num
            k += 1
    for num in range(k, len(nums)):
        nums[num] = 0
    print(nums)


move_zero1(nums)
move_zero2(nums)