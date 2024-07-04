class Solution:

    def equilibriumPoint(self, arr):
        t = sum(arr)
        l = 0
        for i, num in enumerate(arr):
            r = t - l - num

            if l == r:
                return i + 1

            l += num

        return -1

# find the total sum
# then find the right sum by subtracting the leftsum and current numbers
# if left sum and right sum is equal return for i
# upgrade the leftsum with the num in the ith index
