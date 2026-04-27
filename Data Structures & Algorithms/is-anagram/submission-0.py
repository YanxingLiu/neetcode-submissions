class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 直接进行sort
        # sort之后如果相同就相同
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        
        