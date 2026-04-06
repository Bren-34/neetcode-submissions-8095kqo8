from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        # 1. count frequency
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        # 2. sort by frequency (descending)
        sorted_items = sorted(seen.items(), key=lambda item: item[1], reverse=True)

        # 3. take top k
        answer = []
        for i in range(k):
            answer.append(sorted_items[i][0])

        return answer
