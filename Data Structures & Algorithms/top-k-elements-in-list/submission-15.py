class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rep = {}
        tup = []

        # Count frequencies
        for num in nums:
            if num in rep:
                rep[num] += 1
            else:
                rep[num] = 1

        # Store (frequency, number)
        for key, value in rep.items():
            tup.append((value, key))

        # Highest frequency first
        tup.sort(reverse=True)

        result = []

        # Take first k numbers
        for n in range(k):
            result.append(tup[n][1])

        return result
        