def apply_patterns(p,ws):
    i = 0
    passed = []
    combo = p.split()
    for word in ws:
        wordcombo = word.split()
        if len(str(word)) == len(str(p)): 
            while i < len(str(p)):
                if combo[0][i] == "-" or combo[0][i] == wordcombo[0][i]:
                    i = i + 1
                else: 
                    i = 0
            passed.append(word)
            i = 0
        else:
            i = 0
    print(passed)






p = '--r-n-'
ws = ['förena', 'arena', 'forint', 'marina']
apply_patterns(p,ws)