class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # Traverse through all array elements
        for i in range(n):
            # Find the minimum element in remaining unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
                    
            # Swap the found minimum element with the first element
            # of the unsorted part
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            
        return nums

# Example usage:
solution = Solution()
print(solution.sortArray([5, 2, 3, 1]))       # Output: [1, 2, 3, 5]
print(solution.sortArray([5, 1, 1, 2, 0, 0])) # Output: [0, 0, 1, 1, 2, 5]