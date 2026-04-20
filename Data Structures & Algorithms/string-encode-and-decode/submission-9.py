class Solution:

    def encode(self, strs: list[str]) -> str:
        list_str = [s for s in strs]
        if list_str:
            return "split".join(list_str)
        return "None"

    def decode(self, s: str) -> list[str]:
        if s == "None":
            return []
        return s.split("split")
