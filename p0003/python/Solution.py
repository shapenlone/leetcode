#_*_utf-8_*_

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        start = 0
        result = 0
        strdic = {}
        for i in range(len(s)):
            if s[i] in strdic and strdic.get(s[i],0) >= start:
                start = strdic[s[i]] + 1
            else:
                result = max(result,i-start+1)
            strdic[s[i]] = i
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("bbtablud"))