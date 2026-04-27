class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 同样采用哈希表来保存之前的所有元素
        # 每次迭代，查看当前item是否在之前的元素中。
        record = set()
        for num in nums:
            if num in record:
                return True
            else:
                record.add(num)
        return False
        