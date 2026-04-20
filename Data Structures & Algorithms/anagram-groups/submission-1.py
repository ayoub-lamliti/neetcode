class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
    
        for s in strs:
            # عوض Sorting، استعمل Tuple ديال عدد الحروف (26 حرف)
            # هادي هي الطريقة اللي كتخلي الـ Complexity هي O(n * k)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Tuple كيكون هو الـ Key لأنه Immutable
            res[tuple(count)].append(s)
            
        return list(res.values())