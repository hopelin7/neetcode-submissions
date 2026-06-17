class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = dict()
        for i in strs:
            x = tuple(sorted(i))
            if x not in sorted_list:
                sorted_list[x] = []
            sorted_list[x].append(i)
        result = []
        for i in sorted_list.values():
            result.append(i)
        return result

        
        