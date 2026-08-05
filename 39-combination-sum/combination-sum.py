class Solution:
    def findCombinations(self, i, candidates, target, ans, ds):
        if i==len(candidates):
            if target==0:
                ans.append(ds[:])
            return
        
        if candidates[i]<=target:
            ds.append(candidates[i])
            self.findCombinations(i, candidates, target-candidates[i], ans, ds)
            ds.pop(len(ds)-1)
        
        self.findCombinations(i+1, candidates, target, ans, ds)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.findCombinations(0, candidates, target, ans, [])
        return ans