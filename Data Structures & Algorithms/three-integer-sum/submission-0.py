class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 先排序下，过滤掉一些corner case
        nums.sort()
        if nums[0]>0 or nums[-1]<0:
            return []
        result = []
        seen_triplets = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = - nums[i]
            # 要求右边两数之后为-nums[i]
            rec = set()
            for j in range(i+1,len(nums)):
                target2 = target - nums[j]
                if target2 in rec:
                    triplet = tuple(sorted([nums[i],nums[j],target2]))
                    if triplet not in seen_triplets:
                        result.append([nums[i],nums[j],target2])
                        seen_triplets.add(triplet)
                rec.add(nums[j])
        return result
