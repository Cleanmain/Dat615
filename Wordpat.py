def match_pattern(p,w):
    combo = p.split()
    wordcombo = w.split()
    i = 0
    if len(str(w)) == len(str(p)):
        while i < len(str(w)):
            if combo[0][i] == "-" or combo[0][i] == wordcombo[0][i]:
                i = i + 1
            else: 
                return False
        return True
    else: 
        return False





wo = "--e-n-"
match_pattern(wo,"forena")