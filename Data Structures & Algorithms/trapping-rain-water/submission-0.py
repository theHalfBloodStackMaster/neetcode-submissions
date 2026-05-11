class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        sum = 0

        for i in range(n):
            leftMax = height[i]
            rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])

            sum += min(leftMax, rightMax) - height[i]
        return sum