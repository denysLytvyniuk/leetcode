class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost) > sum(gas):
            return -1
        if cost == gas:
            return 0
        diffs = []
        for j in range(len(gas)):
            diffs.append(gas[j] - cost[j])
        indexed_diffs = list(enumerate(diffs))
        for idx, item in sorted(indexed_diffs, key=lambda x: x[1], reverse=True):
            if self.check_arr(diffs[idx:] + diffs[:idx]):
                return idx

    def check_arr(self, arr):
        temp = arr[0]
        for i in range(1, len(arr)):
            if temp < 0:
                return False
            temp += arr[i]
        return True

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(Solution().canCompleteCircuit(gas, cost))
