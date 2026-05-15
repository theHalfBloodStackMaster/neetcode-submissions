class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        numsSet = set(nums)
        maxCount = 0
        for num in numsSet:
            curr = num
            count = 0
            while curr in numsSet:
                count += 1
                curr += 1
            maxCount = max(maxCount,count)
        
        return maxCount