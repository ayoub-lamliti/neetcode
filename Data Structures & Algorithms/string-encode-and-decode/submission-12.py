class Solution:

    def encode(self, strs):
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s):
        res, i = [], 0
        while i < len(s):
            index_length = s.index("#", i)
            length = int(s[i:index_length])
            res.append(s[index_length + 1: index_length + length + 1])
            i = index_length + length + 1
        return res