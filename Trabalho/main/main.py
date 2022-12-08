from match import Match
from time import time_ns as time
from random import randint
#time_ns
#perf_counter_ns
getMedia = lambda sum, n : (int)((sum/n))
getTime = lambda : time()



class Data:
    def __init__(self, pattern: str,
                     text: str, 
                     result: bool, 
                     dTime: float = 0) -> None:
        self.pattern = pattern
        self.text = text
        self.result = result
        self.dTime = dTime


    def getResultString(self)->str:
        return f'{len(self.text)}\t{len(self.pattern)}\t{self.dTime}'

    def getValuesString(self)->str:
        return f'{len(self.text)}\t{len(self.pattern)}\t{self.result}\t{self.text}\t{self.pattern}\t{self.dTime}'



def GenerateData(isTrueResult= True):
    lengs = [x for x in range(1,500)]
    nMedia = 50
    data: list[Data] = []
    dataDP: list[Data] = []
    #generate data
    for n in lengs:
        pattern = Match.patternGenerateBySize(n)
        anotherPattern = Match.patternGenerateBySize(n)
       
        text = Match.stringGenerateByPattern(pattern)
        res = False 
        #calculate (I)
        sumTime = 0
        if(not isTrueResult):
            pattern = anotherPattern
        for _ in range(nMedia):
            ini =getTime()
            res = Match.isMatch(text, pattern)
            fin = getTime()
            sumTime += (fin - ini)
        dtime = getMedia(sumTime,nMedia)
        data.append(Data(pattern=pattern, text=text, result=res, dTime=dtime))
        #calculate (II)
        sumTime = 0
        if(not isTrueResult):
            pattern = anotherPattern
        for _ in range(nMedia):
            ini = getTime()
            res = Match.isMatchDP(text, pattern)
            fin = getTime()
            sumTime += (fin - ini)
        dtime = getMedia(sumTime,nMedia)
        dataDP.append(Data(pattern=pattern, text=text, result=res, dTime=dtime))
    
    with open(f'IsMatch_With_Result_{True if isTrueResult else False}.txt', 'w') as file:
        for d in data:
            file.write(d.getResultString()+'\n')
    with open(f'IsMatch_With_Result_{True if isTrueResult else False}_Info.txt', 'w') as file:
        for d in data:
            file.write(d.getValuesString()+'\n')
    with open(f'IsMatch_With_Result_{True if isTrueResult else False}_in_DP.txt', 'w') as file:
        for d in dataDP:
            file.write(d.getResultString()+'\n')
    with open(f'IsMatch_With_Result_{True if isTrueResult else False}_in_DP_Info.txt', 'w') as file:
        for d in dataDP:
            file.write(d.getValuesString()+'\n')


if __name__ == "__main__" :
    GenerateData()
    GenerateData(False)
