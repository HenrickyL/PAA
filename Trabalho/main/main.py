from match import Match
from datetime import datetime
from random import randint

getTime = lambda : int(datetime.now().timestamp() * 10**6)



class Data:
    def __init__(self, length: int, pattern: str, text: str, result: bool, dTime: float = 0) -> None:
        self.length = length
        self.pattern = pattern
        self.text = text
        self.result = result
        self.dTime = dTime

    def getResultString(self)->str:
        return f'{self.length}\t{self.dTime}'

    def getValuesString(self)->str:
        return f'{self.length}\t{self.result}\t{self.text}\t{self.pattern}\t{self.dTime}'



def GenerateData(isTrueResult= True):
    lengs = [x for x in range(1,500,3)]
    nMedia = 5
    data: list[Data] = []
    dataDP: list[Data] = []
    #generate data
    for n in lengs:
        aux = n + randint(0,3)
        pattern = Match.patternGenerateBySize(n)
        anotherPattern = Match.patternGenerateBySize(n)
       
        text = Match.stringGenerateByPatternAndSize(pattern, aux)
        res = False 
        #calculate (I)
        sumTime = 0
        for _ in range(nMedia):
            if(not isTrueResult):
                pattern = anotherPattern
            ini = getTime()
            res = Match.isMatch(text, pattern)
            fin = getTime()
            sumTime += fin - ini
            print(f' {fin-ini}')
        dtime = sumTime/nMedia
        data.append(Data(length=n, pattern=pattern, text=text, result=res, dTime=dtime))
    
    with open(f'data{True if isTrueResult else False}.txt', 'w') as file:
        for d in data:
            file.write(d.getResultString()+'\n')
    with open(f'data{True if isTrueResult else False}Info.txt', 'w') as file:
        for d in data:
            file.write(d.getValuesString()+'\n')

if __name__ == "__main__" :
    n= 700
    p = Match.patternGenerateBySize(n)
    p2 = Match.patternGenerateBySize(n)
    t = Match.stringGenerateByPatternAndSize(p2,n+30)
    print(f'pattern: {p2}\t\ttext: {t}')
    a = getTime()
    res = Match.isMatch(t,p)
    b = getTime()
    print(b-a, res)
    # GenerateData()
    # GenerateData(False)
