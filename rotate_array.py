class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l=0
        r=len(nums)-1
        k=k % len(nums)
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l=0
        r=k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l=k
        r=len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

# Algorithm
# declare pointer
# assign modulo value to k
# then reverse the arrary
# then set the l value to 0 and r to k-1
# again reverse it
# then set the l value to k and r to last index
# Again reverse it
