class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r=0
        for num in nums:
            r^=num
        return r


# Algorithm
# 1. Initialize a variable r to 0.
# 2. Loop through each number in the list:
#    - XOR the current number with the current value of r.
#    - Update r with the result of the XOR operation.
# 3. After processing all the numbers, r will contain the number that appears only once.
# 4. Return the value of r.