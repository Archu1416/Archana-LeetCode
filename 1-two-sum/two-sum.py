class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        hash={}
        for i,v in enumerate(arr):
            r=target-v
            if r in hash:
                return [hash[r],i]
            hash[v]=i