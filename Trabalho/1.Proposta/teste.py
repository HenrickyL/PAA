from itertools import count
from typing import List
class Solution:
    countPalind = 0
    count = 0

    def longestPalindrome(self,s: str):
        memo = {}
        self.countPalind = 0
        self.count = 0
        if(self._isPalindrom(s,memo)):
            return s
        return self._longestPalindrome(s,memo)


    def _isPalindrom(self, s:str, memo: dict):
        self.countPalind += 1
        if(len(s)==0): return False
        if(memo.get(s)!=None):
            return True
        else:
            if(len(s)==1 or (len(s)==2 and s[0]==s[-1])): 
                return True
            elif(s[0]==s[-1]):
                if(memo.get(s[1:-1])!= None):
                    memo[s] = len(s)
                    return True
                isPalind = self._isPalindrom(s[1:-1],memo)
                if(isPalind):
                    memo[s[1:-1]] = len(s[1:-1])
                    memo[s] = len(s)
                    return True
            return False
            

    def _longestPalindrome(self, s: str, memo:dict):
        self.count+=1
        if(memo.get(s) != None):
            return s
        if(len(s) > 2):
            if(s[0] == s[-1]):
                if(memo.get(s[1:-1]) != None or self._isPalindrom(s[1:-1],memo)):
                    return s  
            # if(self._isPalindrom(s[1:],memo)):
            #     return s[1:]                  
            # if(self._isPalindrom(s[:-1],memo)) :
            #     return s[:-1]                  
            if(self._isPalindrom(s[1:-1],memo)):
                return s[1:-1]                  
            x = self._longestPalindrome(s[1:],memo) #bcd
            y = self._longestPalindrome(s[:-1],memo)#abc
            return  x if len(x)> len(y) else y 
        return s if s[0]==s[-1] else s[0]

S = Solution()
# print(S.longestPalindrome("xabba"))
# print(S.countPalind, S.count)
# print(S.count)
# print(S.longestPalindrome("xabba"))
# print(S.count)
# print(S.longestPalindrome("zABBAzzABAtu_ABcBA_"))
# print(S.countPalind, S.count)

# print(S.longestPalindrome("cbbd"))
# print(S.countPalind, S.count)
memo = {}
print(S._isPalindrom("abcdedcba",memo))
print(S._isPalindrom("bcdedcb",memo))
print(S._isPalindrom("cdedc",memo))
print(S.countPalind, S.count)


print(S.longestPalindrome("abb"))
print(S.countPalind,'\t\t', S.count)
print(S.longestPalindrome("zABBAzzABAtu_ABcBA_"))
print(S.countPalind,'\t\t', S.count)











