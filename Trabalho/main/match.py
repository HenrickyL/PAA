from random import randint 
class Match:
    _count = 0

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
                return i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    return  dp(i, j+2) or (first_match and dp(i+1, j))
                else:
                    return first_match and dp(i+1, j+1)
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
    
    @classmethod
    def stringGenerateByPatternAndSize(cls, pattern: str, size: int)-> str:
        cls._count = size
        stackCharStar = []
        lenP = len(pattern)
        alphabet = list(map(chr, range(97, 123)))
        get = lambda  : alphabet[randint(0,len(alphabet)-1)] 
        def gen(i:int)->str:
            if(cls._count<0):
                raise Exception(f'impossivel criar uma string de tamanho {size} com o patthern {pattern}')
            if(i>= len(pattern)):
             return ''
            if(i+1 < lenP and pattern[i+1]=='*'):
                stackCharStar.append(pattern[i])
                next = gen(i+2)
                currentSize = 0
                if(len(stackCharStar)>1):
                    currentSize = randint(0,cls._count)
                else:
                    currentSize = cls._count
                stackCharStar.pop()
                cls._count -= currentSize
                current = pattern[i]*currentSize if currentSize >0 else ''
                if(pattern[i]=='.'):
                    current = ''.join([get() for _ in current])
                prev = current
                return prev + next
            else:
                value = get() if pattern[i]=='.' else pattern[i]
                cls._count -= 1
                return value + gen(i+1)
        return gen(0)

    @classmethod
    def stringGenerateByPattern(cls, pattern: str)-> str:
        def gen(i: int):
            if(i>= len(pattern)):
                return ''
            alphabet = list(map(chr, range(97, 123)))
            if(i+1 < len(pattern) and pattern[i+1] == '*'):
                current = pattern[i]*randint(0,10)
                if(pattern[i] == '.'):
                    current = ''.join(
                        [alphabet[randint(0,len(alphabet)-1)] for _ in current])
                return current + gen(i+2)

            return (pattern[i] if pattern[i] != '.' else alphabet[randint(0,len(alphabet)-1)])  + gen(i+1)
        return gen(0)