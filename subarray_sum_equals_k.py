class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap=defaultdict(int)
        s=0
        c=0
        for i in nums:
            s+=i
            if s ==k:
                c+=1
            if (s-k) in hashmap:
                c+=hashmap[s-k]
            hashmap[s]+=1
        return c

# algorithm
# declare hashmap , s, c
# then traverse the nums
# add the i with sum
# if s equals k then increment the count to 1
# and then check s and target diff if it is present in hashmpap
# the add the frequency of the existing diff value to the count
# then increment the frequency to one
