class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap1 = {}
        for i , n in enumerate(nums):
            d = target - n
            if d in hashmap1:
                return [hashmap1[d],i]
            hashmap1[n]=i
        return

# Algorithm
# declare the hashmap
# itereate through nums where i is the index and n is the value
# check the difference between target and value
# if the d is in the hashtable then return the indexes
# else set key of hashmap with its index as value