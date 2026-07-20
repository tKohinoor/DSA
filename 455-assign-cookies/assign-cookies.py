class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        index = 0
        while(index<len(s) and child<len(g)):
            if(s[index]>=g[child]):
                child += 1
            index += 1
        return child