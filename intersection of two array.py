class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                seen.add(nums1[i])

        return seen

# Algorithm
# create the set
# tranverse the array
# check nums[i] present is num[2]
# if yes then add that to the set
# return set