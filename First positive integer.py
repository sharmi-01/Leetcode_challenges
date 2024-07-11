class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if val >= 1 and val <= len(nums):
                a = val - 1
                if nums[a] == 0:
                    nums[a] = -1 * (len(nums) + 1)
                elif nums[a] >= 0:
                    nums[a] *= -1

        for i in range(len(nums)):
            if nums[i] < 0:
                continue
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1

# Algorithm
# Fisrt check any negative value present in the array if yes then change it to  0
# then check if the value is present btw the range of the length of the array
# if yes the minus 1 from the value to gets it actual index the replace the number present that index with negative sign
# if the value is 0 then change the value to len of the array + 1 so that it will not affect the futher element
# then finally check the updated array if all elemnt is negative then return with len +1
# else return the index+1 where it has the positive number