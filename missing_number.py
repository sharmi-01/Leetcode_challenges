class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)


# Algorithm
#
# 1. Sort the list of numbers.
# 2. Loop through each index i from 0 to the length of the list
#    - If the number at index i is not equal to i, return i as the missing number.
# 3. If all numbers match their indices, return the length of the list as the missing number.
