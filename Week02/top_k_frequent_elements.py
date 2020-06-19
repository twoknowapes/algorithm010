import collections
import heapq


def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    if not nums: return []

    res, heap, lookup = [], [], collections.Counter(nums)
    for num, freq in lookup.items():
        if len(heap) == k:
            if heap[0][0] < freq:
                heapq.heapreplace(heap, (freq, num))
        else:
            heapq.heappush(heap, (freq, num))
    while heap:
        res.append(heapq.heappop(heap)[0])
    return res
