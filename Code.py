class Solution:
    def findLHS(self, nums: List[int]) -> int:
        s = list(set(nums))
        t = [nums.count(x)+nums.count(x+1) for x in s if (len(s) != 1) and (x+1 in s)]
        t.append(0)
        return max(t)
