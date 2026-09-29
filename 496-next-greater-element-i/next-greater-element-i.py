class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []           # Stores values waiting for their next greater element
        result_map = {}      # Hash map: value → next greater element
    
    # Traverse nums2 from RIGHT to LEFT
        for num in reversed(nums2):
        # Pop elements from stack that are smaller than current
            while stack and num >= stack[-1]:
                stack.pop()
        
        # Top of stack is the next greater element (if exists)
            if stack:
                result_map[num] = stack[-1]
            else:
                result_map[num] = -1
        
        # Push current number onto stack
            stack.append(num)
    
    # Build answer array using nums1 lookup
        ans = [result_map[num] for num in nums1]
    
        return ans