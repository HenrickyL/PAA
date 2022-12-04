from match import Match


if __name__ == "__main__" :
    n = 20
    pattern = Match.patternGenerateBySize(n)
    print(f'pattern: {pattern}')
    print(Match.stringGenerateByPattern(pattern, n))
