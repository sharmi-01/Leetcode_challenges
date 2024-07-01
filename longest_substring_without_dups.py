class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==0:
            return 0

        i=0
        j=0
        seen=set()
        max_count=0

        while j<len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j+=1
                max_count=max(max_count,j-i)
            else:
                while s[i]!=s[j]:
                    seen.remove(s[i])
                    i+=1
                seen.remove(s[i])
                i+=1


        return max_count

# Algorithm
#     First check the len of nums if 0 return 0
# then initialize i,j pointer and also set
# then declare the while loop and check if s[j] is in set
# if yes na remove that
# if not the add that to set
# calculate the max count
# return the max_count
