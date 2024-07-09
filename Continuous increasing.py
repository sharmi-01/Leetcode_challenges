class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i=0
        j=1
        diff=-1
        while j<len(nums):
            if nums[i]<nums[j]:
                diff=max(nums[j]-nums[i],diff)
            elif nums[i]>nums[j]:
                i=j
            j+=1
        return diff