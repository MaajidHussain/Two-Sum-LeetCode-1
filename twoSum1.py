# Import the List type from typing
from typing import List

# Define the Solution class with the twoSum method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Create an instance of the Solution class
solution = Solution()

# Define the input list and target value
nums = [2, 7, 11, 15]
target = 9

# Call the twoSum method and store the result
result = solution.twoSum(nums, target)

# Print the result
print(result)  # Output should be [0, 1]
