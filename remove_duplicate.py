class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        while i<=j and j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[i+1]=nums[j]
                i+=1
        return i+1

# Algorithm
#
# 1. Initialize two pointers, i and j, both set to 0 and 1 respectively.
# 2. Iterate through the list using a while loop until i is less than or equal to j and < len of nums
# 3. Check if the element at nums[i] is equal to the element at nums[j].
#    - If they are equal, increment j to move to the next element.
#    - If they are not equal, increment i and set nums[i+1] to the value of nums[j].
# 4. Continue looping until all elements have been checked.
# 5. Return i + 1, which represents the length of the array with duplicates removed.
