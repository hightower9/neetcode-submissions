class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
    
        main_s = {}

        for char in s:

            main_s[char] = main_s.get(char, 0) + 1

        for char in t:

            if char not in main_s:
                return False

            main_s[char] -= 1

            if main_s[char] < 0:
                return False

        return True
