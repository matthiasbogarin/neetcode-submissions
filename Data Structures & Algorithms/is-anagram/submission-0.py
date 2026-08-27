class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check length condition first, if not the same then return false
        if len(s) != len(t):
            return False

        # Convert strings to hash tables with char as key,
        # value is the count of characters
        d1, d2 = {}, {}
        for c in s:
            d1[c] = d1.get(c, 0) + 1
        for c in t:
            d2[c] = d2.get(c, 0) + 1

        # Check if each character has the same count if yes then
        # return true else return false as soon as you find character
        # that doesnt have the same count
        for char in d1:
            if d1[char] != d2.get(char, 0):
                return False
        return True
