class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = sorted(tuple(s))
        t_set = sorted(tuple(t))
        print(f"s_set = {s_set}, t_set = {t_set}")
        if s_set == t_set:
            return True
        else:
            return False
        