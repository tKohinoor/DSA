class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort(reverse=True)

        total = 0
        for col in range(len(nums[0])):
            max_val = 0
            for row in range(len(nums)):
                max_val = max(max_val, nums[row][col])
            total += max_val

        return total