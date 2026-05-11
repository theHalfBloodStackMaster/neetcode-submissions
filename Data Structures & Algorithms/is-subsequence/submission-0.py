import re

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        for i in range(1):
            for j in range(len(t)):
                if s[i] == t[j]:
                    i = i+1
                    if i < len(s):
                        continue
                    elif i == len(s):
                        return True
            return False