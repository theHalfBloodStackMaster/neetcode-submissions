class Solution:
    def trap(self, height: List[int]) -> int:
        # this solution uses prefix and sufix approach
        n = len(height)
        if n == 0:
            return 0
            
        leftArr = [0] * n
        rightArr = [0] * n 
        waterArea = 0

        leftArr[0] = height[0]

        for i in range(1, n):
            leftArr[i] = max(leftArr[i-1], height[i])

        rightArr[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            rightArr[i] = max(rightArr[i+1], height[i])

        for i in range(1,n-1):
            minHeight = min(leftArr[i], rightArr[i])
            waterArea += minHeight - height[i]

        return waterArea
