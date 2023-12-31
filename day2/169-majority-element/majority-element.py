class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return nums[0]

        n = len(nums)//2
        count = {}

        for i in nums:
            if i in count and count[i] == n:
                return i
            count[i] = count.get(i,0) + 1         
        
        return -1

                