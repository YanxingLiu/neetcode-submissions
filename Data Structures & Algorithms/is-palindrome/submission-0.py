class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 首先进行小写
        # 然后只保留a->z,0-9的数字
        # reverse之后如果和原始的一样那就是回文
        s_n = ""
        for c in s:
            if c.isalnum():
                s_n += c.lower()
        return s_n[::-1] == s_n
        