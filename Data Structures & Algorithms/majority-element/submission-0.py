class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}

        # for num in nums:
        #     count[num] = count.get(num, 0) + 1

        #     if count[num] > len(nums) // 2:
        #         return num
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate