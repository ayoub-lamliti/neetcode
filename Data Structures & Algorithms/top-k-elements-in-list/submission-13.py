class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
    
        # ليستة ديال لي ليست خاويين، الطول ديالها N+1
        freq = [[] for _ in range(len(nums) + 1)]
        
        # كنعمروا الـ Buckets: الـ Index هو التكرار، والقيمة هي الرقم
        for num, c in count.items():
            freq[c].append(num)
            
        res = []
        
        # كنقراو الليستة بالمقلوب (من أكبر تكرار لأصغر تكرار)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # غير كنوصلو لـ k كنحبسو وكنرجعو النتيجة
                if len(res) == k:
                    return res