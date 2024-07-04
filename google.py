def two_sum_closest(nums, target):
    nums.sort()

    left, right = 0, len(nums) - 1

    closest_sum = nums[left]+nums[right]
    result = 0

    while left < right:
        current_sum = nums[left] + nums[right]

        if abs(current_sum - target) < abs( closest_sum - target):
            closest_sum = current_sum
            result = [nums[left], nums[right]]

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            break

    return result



nums1 = [-1,2,1,-4]
target1 = 4
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {two_sum_closest(nums1, target1)}")


























































































































