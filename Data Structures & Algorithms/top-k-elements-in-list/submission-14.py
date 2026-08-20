class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        max = 0
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        srt = sorted(count, key = lambda value: count[value], reverse=True)

        return srt[:k]