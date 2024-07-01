class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m={}
        for i in nums:
            m[i]=m.get(i,0)+1
            if m[i]>len(nums)/2:
                return i

# algorithm
# declare dict
# tranverse through nums
# then set the key  and value
# if the value become greater than half len of num then return i
