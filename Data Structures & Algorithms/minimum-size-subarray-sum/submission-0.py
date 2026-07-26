class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        minLength = len(nums) + 1
        currSum = 0

        for right in range(len(nums)):

            currSum +=nums[right]

            while currSum >= target:
                minLength = min(minLength, right - left + 1)
                currSum -= nums[left]
                left += 1
            
        return 0 if minLength == len(nums) + 1 else minLength