def max_sum(nums):
    # 初始化两个变量
    max_current = nums[0]  # 当前子数组的最大和
    max_global = nums[0]  # 全局最大和

    # 从第二个元素开始遍历数组
    for i in range(1, len(nums)):
        # 对于当前元素，判断是加上前面的子数组和更大，还是单独成为新的子数组更大
        max_current = max(nums[i], max_current + nums[i])

        # 更新全局最大和
        if max_current > max_global:
            max_global = max_current

    return max_global

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum(nums))  # 输出: 6