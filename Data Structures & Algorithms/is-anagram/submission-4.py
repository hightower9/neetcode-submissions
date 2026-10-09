class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if len(s) != len(t):
        #     return False
    
        # main_s = {}

        # for char in s:

        #     main_s[char] = main_s.get(char, 0) + 1

        # for char in t:

        #     if char not in main_s:
        #         return False

        #     main_s[char] -= 1

        #     if main_s[char] < 0:
        #         return False

        # count = [0] * 26

        # print(count)

        # return True

        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        return all(c == 0 for c in count)
