class Solution:
    def jump(self, nums: List[int]) -> int:
        r=0
        l=0
        c=0
        for i in range(len(nums)-1):
            r=max(r,i+nums[i])

            if i==l:
                l=r
                c+=1

        return c

# Declare two pointer and count
# traveser through the array
# increement the reach variable to max steps it could each
# then slide the l value if index and last are same
# then increement the count
# return count