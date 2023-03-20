"""Given an unsorted integer array, find a pair with the given sum in it."""



nums = [7, 2, 5, 3, 1]
target = 10


def find_pair(nums:list, target:int) -> str:
    ls = []
    for num1 in nums[:-1]:
        for num2 in nums[nums.index(num1)+1:]:
            if num2 == target - num1:
                print('Pair found', (num1, num2))
                return
    print('Pair not found')


def find_pair2(nums:list, target:int) -> str:
    ls = {}
    for i, e in enumerate(nums):
        if target - e in ls:
            print('Pair found', (nums[ls.get(target - e)], nums[i]))
            return
        ls[e] = i
    print('Pair not found')


def find_pair3(nums, target) -> str:
    nums.sort()
    low, high = 0, len(nums) - 1
    while low < high:
        if nums[low] + nums[high] == target:
            print('Pair found', (nums[low], nums[high]))
            return
        if nums[low] + nums[high] < target:
            low = low + 1
        else:
            high = high - 1
    print('Pair not found')



find_pair(nums, target)
find_pair2(nums, target)
find_pair3(nums, target)