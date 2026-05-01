class Solution:

    def encode(self, strs: List[str]) -> str:
        # 如果是空的字符串，字节返回空字符串
        if not strs:
            return ""
        #采用游程编码
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        # 按照size,str #的格式来编码
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
