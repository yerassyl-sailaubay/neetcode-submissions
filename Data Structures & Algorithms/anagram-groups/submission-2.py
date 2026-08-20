from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for strr in strs:
            if ''.join(sorted(strr)) in groups:
                groups[''.join(sorted(strr))].append(strr)
            else:
                groups[''.join(sorted(strr))] = [strr]

        
        
        return list(groups.values())
                    
            