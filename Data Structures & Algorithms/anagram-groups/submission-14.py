class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for i in strs:
            sorted_strs = "".join(sorted(i))

            if sorted_strs not in group:
                group[sorted_strs] = []

            group[sorted_strs].append(i)

        return list(group.values())