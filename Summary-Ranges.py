class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, n = 0, len(nums)
        res = []
        while i < n:
            j = i + 1
            prev = nums[i]
            while j < n and nums[j] == prev + 1:
                prev = nums[j]
                j += 1
            if prev == nums[i]:
                res.append(str(prev))
            else:
                res.append(str(nums[i]) + "->" + str(prev))
            i = j
        return res