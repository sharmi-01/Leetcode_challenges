class Solution:
    def maxLen(self, n, arr):
        ans, add = 0, 0
        seen = {0: -1}
        for i in range(n):
            add += arr[i]
            if add in seen:
                ans = max(ans, i-seen[add])
            else:
                seen[add] = i
        return ans

n=8
arr = [1, -1, 3, 2, -2, -3, 4, -4]

sol = Solution()
result = sol.maxLen(n, arr)
print(result)