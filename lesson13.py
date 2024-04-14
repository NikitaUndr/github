
#1-ая задача
def foo(nums):

    if len(nums) == 1:
        return [nums]
    result = []

    for i in range(len(nums)):
        current_num = nums[i]
        remaining_nums = nums[:i] + nums[i + 1:]

        for perm in foo(remaining_nums):
            result.append([current_num] + perm)

    return result


nums1 = [1, 2, 3]
print(foo(nums1))

