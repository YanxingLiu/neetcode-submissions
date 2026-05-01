class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step1:计算自己前面所有元素的乘积
        # Step2: 计算自己后面所有元素的乘积
        n = len(nums)

        pre = [1] * n
        post = [1] * n

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]

        ans = []
        for i in range(n):
            ans.append(pre[i] * post[i])

        return ans