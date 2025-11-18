class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max_sum = float('-inf')
        curr_min_sum = float('inf')
        max_sum = float('-inf')
        min_sum = float('inf')

        total_sum = 0
        for num in nums:
            total_sum += num

            curr_max_sum = max(num, curr_max_sum + num)
            curr_min_sum = min(num, curr_min_sum + num)

            max_sum = max(curr_max_sum, max_sum)
            min_sum = min(curr_min_sum, min_sum)

        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)