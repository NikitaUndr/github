def canJump(nums):
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
    return max_reach >= len(nums) - 1

nums1 = [2, 3, 1, 1, 4]
print(canJump(nums1))

