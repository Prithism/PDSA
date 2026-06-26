class Solution:
    def insertionSort(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # Traverse from 1 to len(nums)
        for i in range(1, n):
            key = nums[i]
            
            # Move elements of nums[0..i-1], that are greater than key,
            # to one position ahead of their current position
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
                
            # Place the key at its correct position
            nums[j + 1] = key
            
        return nums

# Example usage:
solution = Solution()
print(solution.insertionSort([5, 2, 3, 1]))       # Output: [1, 2, 3, 5]
print(solution.insertionSort([5, 1, 1, 2, 0, 0])) # Output: [0, 0, 1, 1, 2, 5]