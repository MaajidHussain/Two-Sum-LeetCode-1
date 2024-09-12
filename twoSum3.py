class Solution:
    def twoSum(self, nums, target):
        numMap={}
        n=len(nums)

        for i in range(n):
            complement=target-nums[i]
            if complement in numMap:
                return [numMap[complement],i]
            numMap[nums[i]]=i
        return []
solution=Solution()
nums=[2,7,11,15]
target=9
result=solution.twoSum(nums,target)
print(result)