class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        c = 0
        s = 0
        e = -1
        n = len(nums)
        maxi = nums[0]
        mini = nums[n - 1]
        while c < len(nums):
            maxi = max(maxi, nums[c])
            if nums[c] < maxi:
                e = c
            c += 1

        c = n - 1
        while c >= 0:
            mini = min(mini, nums[c])
            if nums[c] > mini:
                s = c
            c -= 1

        r = e - s + 1
        return r if e != -1 else 0
#
# Algorithm
# take start and end pointer and max and min
# find put the check for max value from left to right traversal
# If there is not the case then assing the end pointer value to current index
# the use another loop to find min value from right to left
# if there is not the case then assign the start pointer value to the current value
# finally keep result as sstart - end to get the length of the array add one
# finally return the array