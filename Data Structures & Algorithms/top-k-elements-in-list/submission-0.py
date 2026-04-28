class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        rec = defaultdict(int)
        for num in nums:
            rec[num] += 1
        # 计算哈希表的第k大的元素。
        arr = []
        for num, cnt in rec.items():
            arr.append([cnt,num])
        # 根据cnt来sort
        arr.sort()
        
        #
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res