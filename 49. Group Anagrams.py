from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for org in strs:
            sorted_org = "".join(sorted(org))
            res[sorted_org].append(org)
        return list(res.values())