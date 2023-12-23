class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        lookLeft = True
        left = 0
        i = 0
        while i < len(height):
            if lookLeft:
                if i == len(height) - 2:
                    break
                if height[i] > height[i + 1]:
                    left = i
                    lookLeft = False
                i += 1
            else:
                max_h = max(height[left:])
                idx = height.index(max_h)
                if max_h > height[left + 1]:
                    result += self.calc(height[left:idx + 1])
                    lookLeft = True
                    i = idx
                else:
                    result += self.trap(height[left + 1:])
                    break

        return result

    def calc(self, arr):
        h = min(arr[0], arr[len(arr) - 1])
        res = 0
        for i in range(1, len(arr) - 1):
            res += (h - arr[i])
        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height2 = [8, 2, 4]
print(Solution().trap(height))
