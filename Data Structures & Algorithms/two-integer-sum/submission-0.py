class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 采用哈希表保存之前的所有元素
        # 每次检查target - num[i]是否在哈希表中，如果是在的话即找到
        from collections import defaultdict
        record = defaultdict(int)
        for i, num in enumerate(nums):
            target_minus_res = target - num
            if target_minus_res in record:
                return [record[target_minus_res], i]
            else:
                record[num] = i
        return None
        
        