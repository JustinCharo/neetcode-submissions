class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        # index = count, list for each number with that count
        frequency = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        for num, count in count_map.items():
            frequency[count].append(num)
        
        # Set up, now need to create a res array and then return the k most frequent elements
        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res
