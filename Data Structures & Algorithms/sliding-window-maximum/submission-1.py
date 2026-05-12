class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = k
        count = 0
        n = len(nums)
        loopCount = (n - k) + 1
        maxList = []
        maxNum = nums[0]

        if k == 1:
            return nums
        while(count < loopCount):
            for i in range(start, end):
                if nums[i] > maxNum:
                    maxNum = nums[i]
            maxList.append(maxNum)
            start = start + 1
            maxNum = nums[start]
            if (end + 1) <= n:
                end = end + 1
            count = count + 1

        return maxList
            
        