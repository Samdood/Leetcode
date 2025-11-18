class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def recurse(lo: int, hi: int) -> Tuple[int, int, int, int]:
            if lo == hi:
                x = nums[lo]
                return x, x, x, x

            mid = (lo + hi) // 2

            l_best, l_Lmax, l_Rmax, l_total = recurse(lo, mid)
            r_best, r_Lmax, r_Rmax, r_total = recurse(mid + 1, hi)

            total = l_total + r_total
            
            cross_max = l_Rmax + r_Lmax
            best = max(l_best, r_best, cross_max)
            Lmax = max(l_Lmax, l_total + r_Lmax)
            Rmax = max(r_Rmax, r_total + l_Rmax)

            return best, Lmax, Rmax, total

        return recurse(0, len(nums) - 1)[0]