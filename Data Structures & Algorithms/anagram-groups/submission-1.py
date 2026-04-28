class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 采用sort之后的字符串作为key，set作为item
        from collections import defaultdict
        record = defaultdict(list)
        for x in strs:
            sorted_x = "".join(sorted(x))
            record[sorted_x].append(x)
        result = [list(v) for k,v in record.items()]
        return result