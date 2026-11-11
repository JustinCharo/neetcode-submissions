class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        arr = []
        for num, count in count_map.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            count, num = arr.pop()
            res.append(num)

        return res
