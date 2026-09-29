class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
    
    # For each element in nums1
        for num in nums1:
        # Find position in nums2
            index_in_nums2 = nums2.index(num)
            found = False  # Track if we found greater element
        
        # Search to the right in nums2
            for i in range(index_in_nums2 + 1, len(nums2)):
                if nums2[i] > num:
                    found = True
                    break  # Stop after finding FIRST greater
        
            if found:
                result.append(nums2[i])  # Append the value
            else:
                result.append(-1)  # No greater element found
    
        return result