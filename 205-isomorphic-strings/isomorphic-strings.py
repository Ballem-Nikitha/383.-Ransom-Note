class Solution(object):
    def isIsomorphic(self, s, t):
        patterns=[]
        patternt=[]
        for i in s:
            patterns.append(s.index(i))
        for i in t:
            patternt.append(t.index(i))
        return patterns==patternt
        