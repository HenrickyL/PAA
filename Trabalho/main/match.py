from random import randint 
class Match:
    @staticmethod
    def isMatchDP(text: str, pattern: str)-> bool:
        memo = {}
        def match(i: int, j: int)-> bool:
            if((i,j) in memo):
                return memo[(i,j)]
            if (j == len(pattern)):
                memo[(i,j)] = ( i == len(text) )
                return memo[(i,j)]
            first_match = i < len(text) and pattern[j] in {text[i], '.'}
            if (j+1 < len(pattern) and pattern[j+1] == '*'):
                memo[(i,j)] = match(i, j+2) or (first_match and match(i+1, j))
                return memo[(i,j)]
            else:
                memo[(i,j)] = first_match and match(i+1, j+1)
                return memo[(i,j)]
        return match(0,0)

    @staticmethod
    def isMatch(text, pattern):
        def dp(i, j):
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans =  dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)

            return ans
        return dp(0, 0)


    @staticmethod
    def patternGenerateBySize(size: int)->str :
        res = ''
        options = ['.']+list(map(chr, range(97, 123))) + ['.']
        get = lambda  : options[randint(0,len(options)-1)] 
        for i in range(size):
            if(i == 0 or res[-1] == '*'):
                res += get()
            else:
                res += get() if randint(0,100)%5 !=0 else '*'
        return res