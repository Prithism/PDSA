class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        temp = [0] * len(nums)
        
        def merge_sort(left: int, right: int):
            if left >= right:
                return
            
            mid = left + (right - left) // 2
            
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            
            i = left
            j = mid + 1
            k = left
            
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1
                
            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1
                
            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1
                
            for idx in range(left, right + 1):
                nums[idx] = temp[idx]

        merge_sort(0, len(nums) - 1)
        return nums

# Example usage:
solution = Solution()
print(solution.sortArray([5, 2, 3, 1]))       # Output: [1, 2, 3, 5]
print(solution.sortArray([5, 1, 1, 2, 0, 0])) # Output: [0, 0, 1, 1, 2, 5]