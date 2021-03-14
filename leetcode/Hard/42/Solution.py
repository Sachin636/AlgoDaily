class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_right = []

        # Build the left to right arr
        m = 0
        for i in range(n):
            if height[i] <= m:
                left_right.append(m)
            else:
                m = height[i]
                left_right.append(m)

        # Build the right to left arr
        m = 0
        right_left = []
        for i in range(n-1, -1, -1):
            if height[i] >= m:
                m = height[i]
                right_left.insert(0, m)
            else:
                right_left.insert(0, m)

        # Find the total trapped water
        trapped_water = 0
        for i in range(n):
            w = min(left_right[i], right_left[i]) - height[i]
            trapped_water += w

        return trapped_water
