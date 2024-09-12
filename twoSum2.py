class Solution:
    def twoSum(self, nums, target):
        numMap={}
        n=len(nums)

        for i in range(n):
            numMap[nums[i]] =i

        for i in range(n):
            complement=target-nums[i]
            if complement in numMap and numMap[complement] !=i:
                return [i,numMap[complement]]
        return []
        
solution=Solution()
nums=[2,7,11,15]
target=9
result=solution.twoSum(nums,target)
print(result)