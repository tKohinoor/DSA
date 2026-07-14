class Solution:
    def rev(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums.reverse()
        self.rev(nums, 0, k-1)
        self.rev(nums, k, n-1)
