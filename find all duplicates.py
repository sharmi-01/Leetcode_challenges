class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        m = {}
        l = []
        for i in nums:
            m[i] = m.get(i, 0) + 1
            if m[i] > 1:
                l.append(i)
        return l

# Algorithm
# decalre a hashset and list
# traverse the array and check whether the element present in the hashset
# if it present then it increment the value +1
# and check if the value of the key is greater than 1 then appen it in list list
# return the list